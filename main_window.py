from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QFrame
from PySide6.QtCore import Qt,Slot
from widgets.user_widget import UserWidget
from widgets.watch_list_widget import WatchListWidget
from widgets.recent_widget import RecentWidget
from services.alpha_vantage_client import AlphaVantageClient



class MainWindow(QMainWindow):
    @Slot(str)
    def handle_company_symbol(self,symbol):
        company=self.alphaclient.get_company_overview(symbol)
        if company is None:
            self.user_widget.company_info_widget.show_company_not_found()
            return

        self.user_widget.company_info_widget.update_company_info(company)
    

    @Slot(dict)
    def handle_watch_list(self,overview):
        for company in self.watch_list_widget.company_list:
            if company['overview']['Symbol'] == overview['Symbol']:
                self.user_widget.company_info_widget.clear_company_not_found()
                return
        
        quote=self.alphaclient.get_global_quote(overview['Symbol'])
        company_info={
            'overview':overview,
            'quote':quote
        }
        self.watch_list_widget.add_to_watch_list(company_info)
        self.user_widget.company_info_widget.show_company_not_found()
         

    

    def __init__(self):
        super().__init__()
        self.alphaclient=AlphaVantageClient()
        maincontainer=QWidget()
        self.setWindowTitle('Home')
        self.setCentralWidget(maincontainer)
        self.user_widget=UserWidget()
        self.watch_list_widget=WatchListWidget()
        self.recent_widget=RecentWidget()
        main_layout=QVBoxLayout(maincontainer)
        main_layout.addWidget(self.user_widget)
        main_layout.addWidget(self.watch_list_widget)
        main_layout.addWidget(self.recent_widget)
        main_layout.setContentsMargins(20,20,20,20)
        main_layout.setSpacing(30)
        self.user_widget.searchbar.companySearched.connect(self.handle_company_symbol)
        self.user_widget.company_info_widget.addToWatchListRequested.connect(self.handle_watch_list)