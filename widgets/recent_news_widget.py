from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame,QTreeWidget,QTreeWidgetItem
from PySide6.QtCore import Qt


class RecentWidget(QWidget):
    def __init__(self):
        super(). __init__()
        recentFrame=QFrame()
        recentFrame.setFrameShape(QFrame.Shape.Box)
        recentFrameLayout=QVBoxLayout(recentFrame)
        recentlabel=QLabel('Recent Changes:')
        recent_layout=QVBoxLayout(self)
        self.recent_list=QTreeWidget()
        self.recent_list.setHeaderHidden(True)
        recentFrameLayout.addWidget(recentlabel)
        recentFrameLayout.addWidget(self.recent_list)
        recentFrameLayout.setSpacing(20)
        recent_layout.addWidget(recentFrame)



    def show_articles(self,company_list):
        self.recent_list.clear()
        for company in company_list:
            company_item=QTreeWidgetItem(self.recent_list,[company['overview']['Name']])
            for article in company['articles']:
                article_item=QTreeWidgetItem(company_item,[article['Title']])
            
