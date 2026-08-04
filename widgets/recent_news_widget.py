from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame,QTreeWidget,QTreeWidgetItem,QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt,Signal


class RecentNewsWidget(QWidget):
    doubleclickedArticle=Signal(str)
    explanationAsked=Signal(dict)
    def __init__(self):
        super(). __init__()
        self.company_info_list=[]
        self.current_selected={}
        recentFrame=QFrame()
        recentFrame.setFrameShape(QFrame.Shape.Box)
        recentFrameLayout=QVBoxLayout(recentFrame)
        recentlabel=QLabel('Recent Changes:')
        recentlabel_font=recentlabel.font()
        recentlabel_font.setPointSize(12)
        recentlabel_font.setWeight(QFont.DemiBold)
        recentlabel.setFont(recentlabel_font)
        recent_layout=QVBoxLayout(self)
        self.recent_list=QTreeWidget()
        self.recent_list.setHeaderLabels(['Articles','Published',""])
        self.recent_list.setColumnCount(3)
        self.explanation_button=QPushButton()
        self.explanation_button.setEnabled(False)
        self.explanation_button.setText('AI Analysis:')
        self.explanation_button.setToolTip("Select a company to generate AI analysis.")
        recentFrameLayout.addWidget(self.recent_list)
        recentFrameLayout.addWidget(self.explanation_button,alignment=Qt.AlignRight)
        recentFrameLayout.setSpacing(20)
        recent_layout.addWidget(recentlabel)
        recent_layout.addWidget(recentFrame)
        self.recent_list.itemDoubleClicked.connect(self.show_article_doubleclicked)
        self.recent_list.itemSelectionChanged.connect(self.enable_explanation_button)
        self.explanation_button.clicked.connect(self.explanation_requested)



    def show_articles_refresh(self,company_list:list):
        self.recent_list.clear()
        self.company_info_list=company_list
        for company in self.company_info_list:
                company_item=QTreeWidgetItem(self.recent_list,[company['overview']['Name']])
                company_item.setData(0,Qt.ItemDataRole.UserRole,company['overview']['Symbol'])
                for article in company['articles']:
                        article_item=QTreeWidgetItem(company_item,[article['Title'],f'{article['Name']}\t{article['Published']}'])
                        article_item.setData(0,Qt.ItemDataRole.UserRole,article['Url'])


    def show_added_company_article(self,company_info:dict):
        self.company_info_list.append(company_info)
        company_item=QTreeWidgetItem(self.recent_list,[company_info['overview']['Name']])
        company_item.setData(0,Qt.ItemDataRole.UserRole,company_info['overview']['Symbol'])
        for article in company_info['articles']:
            article_item=QTreeWidgetItem(company_item,[article['Title'],f'{article['Name']}\t{article['Published']}'])
            article_item.setData(0,Qt.ItemDataRole.UserRole,article['Url'])


    def show_article_doubleclicked(self,item):
        if item.parent() is None:
            return
        
        url=item.data(0,Qt.ItemDataRole.UserRole)
        self.doubleclickedArticle.emit(url)


    def enable_explanation_button(self):
        self.current_selected={}
        selected=self.recent_list.selectedItems()
        if not selected:
            self.explanation_button.setEnabled(False)
            return

        item=selected[0]

        if item.parent() is None:
            self.explanation_button.setEnabled(True)
            selected_symbol=item.data(0,Qt.ItemDataRole.UserRole)
            for company in self.company_info_list:
                if selected_symbol == company['overview']['Symbol']:
                    self.current_selected=company

        else:
            self.explanation_button.setEnabled(False)

    def explanation_requested(self):
        self.explanation_button.setEnabled(False)
        self.explanationAsked.emit(self.current_selected)

    def display_after_delete(self,company_list):
        if not company_list:
            self.back_to_default()

        else:
            self.show_articles_refresh(company_list)
            
    def back_to_default(self):
        self.recent_list.clear()
        self.explanation_button.setEnabled(False)
         

            
