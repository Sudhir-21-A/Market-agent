from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFrame
from PySide6.QtCore import Qt
from .search_bar_widget import SearchBarWidget


class UserWidget(QWidget):
    def __init__(self):
        super(). __init__()
        Frame=QFrame()
        Frame.setFrameShape(QFrame.Shape.Box)
        FrameLayout=QVBoxLayout(Frame)
        Layout=QVBoxLayout(self)
        self.userlabel=QLabel('Username ABCD')
        FrameLayout.addWidget(self.userlabel)
        searchbar=SearchBarWidget()
        FrameLayout.addWidget(searchbar)
        FrameLayout.setSpacing(40)
        Layout.setContentsMargins(10,0,10,0)
        Layout.addWidget(Frame)
