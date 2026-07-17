from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QFrame
from PySide6.QtCore import Qt
from widgets.user_widget import UserWidget
from widgets.watch_list_widget import WatchListWidget
from widgets.recent_widget import RecentWidget



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
        main_layout.setSpacing(30)