from PySide6.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        maincontainer=QWidget()
        self.setWindowTitle('Home')
        self.setCentralWidget(maincontainer)
        main_layout=QVBoxLayout(maincontainer)
        main_layout.addWidget(UserWidget())
        main_layout.addWidget(WatchListWidget())
        main_layout.addWidget(RecentWidget())
        main_layout.setContentsMargins(20,20,20,20)
        main_layout.setSpacing(50)


class UserWidget(QWidget):
    def __init__(self):
        super(). __init__()
        userLayout=QVBoxLayout(self)
        self.userlabel=QLabel('Username ABCD')
        userLayout.addWidget(self.userlabel)
        userLayout.addWidget(SearchBarWidget())
        userLayout.setSpacing(40)
        userLayout.setContentsMargins(0,0,0,0)

class WatchListWidget(QWidget):
    def __init__(self):
        super(). __init__()
        watchlabel=QLabel('Current Watchlist:')
        watchlist_layout=QVBoxLayout(self)
        watch_list=QListWidget()
        watch_list.addItems(['Nvidia +3.167%','Microsoft +2.71%'])
        watchlist_layout.addWidget(watchlabel)
        watchlist_layout.addWidget(watch_list)
        watchlist_layout.setSpacing(50)




class RecentWidget(QWidget):
    def __init__(self):
        super(). __init__()
        recentlabel=QLabel('Recent Changes:')
        recent_layout=QVBoxLayout(self)
        recent_list=QListWidget()
        recent_list.addItems(['Nvidia goes up due to increased demand','Microsoft announces new windows features increasing value'])
        recent_layout.addWidget(recentlabel)
        recent_layout.addWidget(recent_list)
        recent_layout.setSpacing(50)




class SearchBarWidget(QWidget):
    def __init__(self):
        super(). __init__()
        search_bar_layout=QHBoxLayout(self)
        searchbox=QLineEdit()
        searchbox.setPlaceholderText('Company Name:')
        search_button=QPushButton('SEARCH')
        search_bar_layout.addWidget(searchbox)
        search_bar_layout.addWidget(search_button)
        search_bar_layout.setSpacing(0)
        search_bar_layout.setContentsMargins(0,0,0,40)





        

app=QApplication()
window=MainWindow()

window.show()
app.exec()