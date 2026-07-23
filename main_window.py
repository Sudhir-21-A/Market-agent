from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QFrame
from PySide6.QtCore import Qt,Slot
from widgets.user_widget import UserWidget
from widgets.watch_list_widget import WatchListWidget
from widgets.recent_widget import RecentWidget
from services.finnhub_client import FinnhubClient



class MainWindow(QMainWindow):
    @Slot(str)
    def handle_company_search(self,symbol):
        profile=self.finnhubclient.get_company_profile(symbol)
        if profile is None:
            query=self.finnhubclient.get_symbol(symbol)
            self.user_widget.show_search_results(query)
        else:
            self.user_widget.show_company_profile(profile)


    def handle_search_item_clicked(self,symbol):
        profile=self.finnhubclient.get_company_profile(symbol)
        if profile is None:
            self.user_widget.company_info_widget.show_company_not_found()
            return 

        self.user_widget.show_company_profile(profile)
    

    @Slot(dict)
    def handle_watch_list(self,overview):
        for company in self.watch_list_widget.company_list:
            if company['overview']['Symbol'] == overview['Symbol']:
                self.user_widget.company_info_widget.clear_company_info()
                return
        
        quote=self.finnhubclient.get_quote(overview['Symbol'])
        company_info={
            'overview':overview,
            'quote':quote
        }
        self.watch_list_widget.add_to_watch_list(company_info)
        self.user_widget.company_info_widget.show_company_not_found()
    

    @Slot(list)
    def handle_refresh(self,company_list):
        for company in company_list:
            company['quote']=self.finnhubclient.get_quote(company['overview']['Symbol'])
        
        self.watch_list_widget.refresh_watch_list(company_list)

         

    

    def __init__(self):
        super().__init__()
        self.finnhubclient=FinnhubClient()
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
        self.user_widget.searchbar.companySearched.connect(self.handle_company_search)
        self.user_widget.company_info_widget.addToWatchListRequested.connect(self.handle_watch_list)
        self.watch_list_widget.refreshRequested.connect(self.handle_refresh)
        self.user_widget.search_results_widget.companySelected.connect(self.handle_search_item_clicked)