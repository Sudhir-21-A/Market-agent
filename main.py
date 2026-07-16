from PySide6.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
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


class UserWidget(QWidget):
    def __init__(self):
        super(). __init__()
        userLayout=QVBoxLayout(self)
        userlabel=QLabel('Username ABCD')
        userLayout.addWidget(userlabel)
        userLayout.addWidget(SearchBarWidget())


class WatchListWidget(QWidget):
    def __init__(self):
        super(). __init__()
        watchlabel=QLabel('Current Watchlist:')
        watchlist_layout=QVBoxLayout(self)
        wlabel1=QLabel('Nvidia  +3.111%')
        watchlist_layout.addWidget(watchlabel)
        watchlist_layout.addWidget(wlabel1)




class RecentWidget(QWidget):
    def __init__(self):
        super(). __init__()
        recentlabel=QLabel('Recent Changes:')
        recent_layout=QVBoxLayout(self)
        rlabel1=QLabel('Nvidia  goes up by 5%....')
        recent_layout.addWidget(recentlabel)
        recent_layout.addWidget(rlabel1)




class SearchBarWidget(QWidget):
    def __init__(self):
        super(). __init__()
        search_bar_layout=QHBoxLayout(self)
        searchbox=QLineEdit()
        searchbox.setPlaceholderText('Company Name:')
        search_button=QPushButton('SEARCH')
        search_bar_layout.addWidget(searchbox)
        search_bar_layout.addWidget(search_button)





        

app=QApplication()
window=MainWindow()

window.show()
app.exec()