from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QFrame,QDockWidget
from PySide6.QtCore import Qt,Slot
import webbrowser
from widgets.user_widget import UserWidget
from widgets.watch_list_widget import WatchListWidget
from widgets.recent_news_widget import RecentNewsWidget
from widgets.ai_explanation_widget import ExplanationDockWidget
from services.finnhub_client import FinnhubClient
from services.newsapi_client import NewsApiClient
from services.gemini_llm_client import GeminiClient



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


    def handle_article_doubleclicked(self,url):
        webbrowser.open_new(url)
    

    @Slot(dict)
    def handle_watch_list_news(self,overview):
        for company in self.watch_list_widget.company_list:
            if company['overview']['Symbol'] == overview['Symbol']:
                self.user_widget.company_info_widget.clear_company_info()
                return
        
        quote=self.finnhubclient.get_quote(overview['Symbol'])
        articles=self.newsapiclient.get_news(overview['Name'])
        company_info={
            'overview':overview,
            'quote':quote,
            'articles':articles
        }
        self.watch_list_widget.add_to_watch_list(company_info)
        self.recent_widget.show_added_company_article(company_info)
        self.user_widget.company_info_widget.clear_company_info()


    def handle_ai_explanation(self,company_info):
        self.ai_explanation_widget.show()
        explanation=self.geminiclient.get_gemini_explanation(company_info)
        if explanation is None:
            self.ai_explanation_widget.hide()
            return
        else:
            self.ai_explanation_widget.show_info(explanation)


    @Slot(list)
    def handle_refresh(self,company_list):
        new_company_list=[]
        for company in company_list:
            company['quote']=self.finnhubclient.get_quote(company['overview']['Symbol'])
            news=self.newsapiclient.get_news(company['overview']['Name'])
            company_info={
                'overview': company['overview'],
                'quote': company['quote'],
                'articles': news
            }
            new_company_list.append(company_info)


        self.watch_list_widget.refresh_watch_list(new_company_list)
        self.recent_widget.show_articles_refresh(new_company_list)



    def handle_delete(self,company_list):
        self.recent_widget.display_after_delete(company_list)
         

    

    def __init__(self):
        super().__init__()
        self.finnhubclient=FinnhubClient()
        self.newsapiclient=NewsApiClient()
        self.geminiclient=GeminiClient()
        maincontainer=QWidget()
        self.setWindowTitle('Home')
        self.setCentralWidget(maincontainer)
        self.user_widget=UserWidget()
        self.watch_list_widget=WatchListWidget()
        self.recent_widget=RecentNewsWidget()
        self.ai_explanation_widget=ExplanationDockWidget()
        main_layout=QVBoxLayout(maincontainer)
        main_layout.addWidget(self.user_widget)
        main_layout.addWidget(self.watch_list_widget)
        main_layout.addWidget(self.recent_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,self.ai_explanation_widget)
        main_layout.setContentsMargins(20,20,20,20)
        main_layout.setSpacing(30)
        self.user_widget.searchbar.companySearched.connect(self.handle_company_search)
        self.user_widget.company_info_widget.addToWatchListRequested.connect(self.handle_watch_list_news)
        self.watch_list_widget.refreshRequested.connect(self.handle_refresh)
        self.user_widget.search_results_widget.companySelected.connect(self.handle_search_item_clicked)
        self.recent_widget.doubleclickedArticle.connect(self.handle_article_doubleclicked)
        self.recent_widget.explanationAsked.connect(self.handle_ai_explanation)
        self.watch_list_widget.deleteRequested.connect(self.handle_delete)