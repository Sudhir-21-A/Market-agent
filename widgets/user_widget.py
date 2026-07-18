from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFrame,QPushButton
from PySide6.QtCore import Qt,Signal
from .search_bar_widget import SearchBarWidget
from .company_widget import CompanyInfoWidget


class UserWidget(QWidget):

    
    def __init__(self):
        super(). __init__()
        user_frame=QFrame()
        self.searchbar=SearchBarWidget()
        self.company_info_widget=CompanyInfoWidget()
        user_frame.setFrameShape(QFrame.Shape.Box)
        user_frame_layout=QVBoxLayout(user_frame)
        self.userlabel=QLabel('Username ABCD')
        user_frame_layout.addWidget(self.userlabel)
        user_frame_layout.addWidget(self.searchbar)
        user_frame_layout.addWidget(self.company_info_widget)
        user_layout=QVBoxLayout(self)
        user_layout.setContentsMargins(10,0,10,0)
        user_layout.addWidget(user_frame)
    

