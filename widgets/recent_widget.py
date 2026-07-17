from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame
from PySide6.QtCore import Qt


class RecentWidget(QWidget):
    def __init__(self):
        super(). __init__()
        recentFrame=QFrame()
        recentFrame.setFrameShape(QFrame.Shape.Box)
        recentFrameLayout=QVBoxLayout(recentFrame)
        recentlabel=QLabel('Recent Changes:')
        recent_layout=QVBoxLayout(self)
        recent_list=QListWidget()
        recent_list.addItems(['Nvidia goes up due to increased demand','Microsoft announces new windows features increasing value'])
        recentFrameLayout.addWidget(recentlabel)
        recentFrameLayout.addWidget(recent_list)
        recentFrameLayout.setSpacing(20)
        recent_layout.addWidget(recentFrame)