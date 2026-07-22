from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame,QPushButton
from PySide6.QtCore import Qt,Signal



class WatchListWidget(QWidget):

    refreshRequested=Signal(list)


    def __init__(self):
        super(). __init__()
        self.company_list=[]
        Frame=QFrame()
        Frame.setFrameShape(QFrame.Shape.Box)
        watchlistFrameLayout=QVBoxLayout(Frame)
        watchlabel=QLabel('Current Watchlist:')
        layout=QVBoxLayout(self)
        self.watch_list=QListWidget()
        self.refresh_button=QPushButton('Refresh')
        self.refresh_button.hide()
        watchlistFrameLayout.addWidget(watchlabel)
        watchlistFrameLayout.addWidget(self.watch_list)
        watchlistFrameLayout.addWidget(self.refresh_button,alignment=Qt.AlignRight)
        watchlistFrameLayout.setSpacing(20)
        layout.addWidget(Frame)
        self.refresh_button.clicked.connect(self.to_refresh)
    
    def display_watch_list(self,list):
        self.watch_list.clear()
        for company in list:
            self.watch_list.addItem(f'{company['overview']['Name']} \t({company['overview']['Symbol']}) \tCurrent Price: ${company['quote']['CurrentPrice']}   \tChange Percent: {company['quote']['ChangePercent']}%')
        
        self.refresh_button.show()
        self.refresh_button.setEnabled(True)
        self.refresh_button.setText('Refresh')

    def add_to_watch_list(self,company):
        self.company_list.append(company)
        self.display_watch_list(self.company_list)

    
    def to_refresh(self):
        self.refresh_button.setEnabled(False)
        self.refresh_button.setText('Refreshing...')
        self.refreshRequested.emit(self.company_list)

    def refresh_watch_list(self,new_list):
        self.company_list=new_list
        self.display_watch_list(self.company_list)
        