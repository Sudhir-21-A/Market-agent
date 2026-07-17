from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame
from PySide6.QtCore import Qt



class WatchListWidget(QWidget):
    def __init__(self):
        super(). __init__()
        Frame=QFrame()
        Frame.setFrameShape(QFrame.Shape.Box)
        watchlistFrameLayout=QVBoxLayout(Frame)
        watchlabel=QLabel('Current Watchlist:')
        layout=QVBoxLayout(self)
        self.watch_list=QListWidget()
        self.watch_list.addItems(['Nvidia +3.167%','Microsoft +2.71%'])
        watchlistFrameLayout.addWidget(watchlabel)
        watchlistFrameLayout.addWidget(self.watch_list)
        watchlistFrameLayout.setSpacing(20)
        layout.addWidget(Frame)