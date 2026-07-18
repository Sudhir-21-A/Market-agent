from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFrame
from PySide6.QtCore import Qt
from .search_bar_widget import SearchBarWidget


class UserWidget(QWidget):
    def __init__(self):
        super(). __init__()
        user_frame=QFrame()
        self.searchbar=SearchBarWidget()
        user_frame.setFrameShape(QFrame.Shape.Box)
        user_frame_layout=QVBoxLayout(user_frame)
        self.userlabel=QLabel('Username ABCD')
        user_frame_layout.addWidget(self.userlabel)
        user_frame_layout.addWidget(self.searchbar)
        user_layout=QVBoxLayout(self)
        user_layout.setContentsMargins(10,0,10,0)
        company_frame=QFrame()
        company_frame.setFrameShape(QFrame.Shape.Box)
        company_layout=QVBoxLayout(company_frame)
        self.company_name_label=QLabel()
        self.company_symbol_label=QLabel()
        self.company_country_label=QLabel()
        self.company_industry_label=QLabel()
        company_layout.addWidget(self.company_name_label)
        company_layout.addWidget(self.company_symbol_label)
        company_layout.addWidget(self.company_country_label)
        company_layout.addWidget(self.company_industry_label)
        company_layout.setContentsMargins(0,0,0,70)
        company_layout.setAlignment(Qt.AlignCenter)
        company_layout.setSpacing(10)
        user_frame_layout.addWidget(company_frame)
        user_layout.addWidget(user_frame)
    

    def update_company_info(self,company):
        self.company_name_label.setText(f'Company Name: {company['Name']}')
        self.company_symbol_label.setText(f'Company Symbol: {company['Symbol']}')
        self.company_country_label.setText(f'Company Country: {company['Country']}')
        self.company_industry_label.setText(f'Company Industry: {company['Industry']}')
