from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFrame,QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt,Signal
from .search_bar_widget import SearchBarWidget
from .company_widget import CompanyInfoWidget
from .search_results_widget import SearchResultsWidget


class UserWidget(QWidget):

    
    def __init__(self):
        super(). __init__()
        user_frame=QFrame()
        self.searchbar=SearchBarWidget()
        self.company_info_widget=CompanyInfoWidget()
        self.search_results_widget=SearchResultsWidget()
        user_frame.setFrameShape(QFrame.Shape.Box)
        user_frame_layout=QVBoxLayout(user_frame)
        self.user_label=QLabel('Username ABCD')
        user_label_font=self.user_label.font()
        user_label_font.setWeight(QFont.DemiBold)
        user_label_font.setPointSize(15)
        self.user_label.setFont(user_label_font)
        user_frame_layout.addWidget(self.searchbar)
        user_frame_layout.addWidget(self.search_results_widget)
        user_frame_layout.addWidget(self.company_info_widget)
        user_layout=QVBoxLayout(self)
        user_layout.setContentsMargins(10,0,10,0)
        user_layout.addWidget(self.user_label)
        user_layout.addWidget(user_frame)
        self.search_results_widget.hide()



    def show_search_results(self,query_list):
        self.search_results_widget.show()
        self.company_info_widget.hide()
        self.search_results_widget.show_results(query_list)


    def show_company_profile(self,company_profile):
        self.search_results_widget.hide()
        self.company_info_widget.show()
        self.company_info_widget.update_company_info(company_profile)
    

