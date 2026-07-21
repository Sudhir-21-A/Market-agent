from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame
from PySide6.QtCore import Qt,Slot



class WatchListWidget(QWidget):
    def __init__(self):
        super(). __init__()
        self.company_list=[]
        Frame=QFrame()
        Frame.setFrameShape(QFrame.Shape.Box)
        watchlistFrameLayout=QVBoxLayout(Frame)
        watchlabel=QLabel('Current Watchlist:')
        layout=QVBoxLayout(self)
        self.watch_list=QListWidget()
        watchlistFrameLayout.addWidget(watchlabel)
        watchlistFrameLayout.addWidget(self.watch_list)
        watchlistFrameLayout.setSpacing(20)
        layout.addWidget(Frame)
    
    def display_watch_list(self,list):
        self.watch_list.clear()
        for company in list:
            self.watch_list.addItem(f'{company['overview']['Name']} \t({company['overview']['Symbol']}) \tCurrent Price: ${company['quote']['CurrentPrice']}   \tChange Percent: {company['quote']['ChangePercent']}%')
    

    def add_to_watch_list(self,company):
        self.company_list.append(company)
        self.display_watch_list(self.company_list)

        