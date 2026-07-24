from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame,QTreeWidget,QTreeWidgetItem
from PySide6.QtCore import Qt,Signal


class RecentNewsWidget(QWidget):
    doubleclickedArticle=Signal(str)
    def __init__(self):
        super(). __init__()
        recentFrame=QFrame()
        recentFrame.setFrameShape(QFrame.Shape.Box)
        recentFrameLayout=QVBoxLayout(recentFrame)
        recentlabel=QLabel('Recent Changes:')
        recent_layout=QVBoxLayout(self)
        self.recent_list=QTreeWidget()
        self.recent_list.setHeaderLabels(['Articles','Published'])
        recentFrameLayout.addWidget(recentlabel)
        recentFrameLayout.addWidget(self.recent_list)
        recentFrameLayout.setSpacing(20)
        recent_layout.addWidget(recentFrame)
        self.recent_list.itemDoubleClicked.connect(self.show_article_doubleclicked)



    def show_articles(self,company_list):
        self.recent_list.clear()
        self.recent_list.setColumnCount(2)
        for company in company_list:
            company_item=QTreeWidgetItem(self.recent_list,[company['overview']['Name']])
            for article in company['articles']:
                article_item=QTreeWidgetItem(company_item,[article['Title'],f'{article['Name']}\t{article['Published']}'])
                article_item.setData(0,Qt.ItemDataRole.UserRole,article['Url'])


    def show_article_doubleclicked(self,item):
        if item.parent() is None:
            return
        
        url=item.data(0,Qt.ItemDataRole.UserRole)
        self.doubleclickedArticle.emit(url)

            
