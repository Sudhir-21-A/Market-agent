from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFrame,QPushButton
from PySide6.QtCore import Qt,Signal


class CompanyInfoWidget(QWidget):
    addToWatchListRequested=Signal(dict)

    def __init__(self):
        super(). __init__()
        self.current_company={}
        company_info_frame=QFrame()
        company_info_frame.setFrameShape(QFrame.Shape.Box)
        company_info_layout=QVBoxLayout(company_info_frame)
        self.company_name_label=QLabel()
        self.company_symbol_label=QLabel()
        self.company_country_label=QLabel()
        self.company_industry_label=QLabel()
        self.add_to_watchlist_button=QPushButton('Add to WatchList')
        self.add_to_watchlist_button.hide()
        company_info_layout.addWidget(self.company_name_label)
        company_info_layout.addWidget(self.company_symbol_label)
        company_info_layout.addWidget(self.company_country_label)
        company_info_layout.addWidget(self.company_industry_label)
        company_info_layout.setContentsMargins(0,0,0,70)
        company_info_layout.setAlignment(Qt.AlignCenter)
        company_info_layout.setSpacing(10)
        company_main_layout=QVBoxLayout(self)
        company_main_layout.addWidget(company_info_frame)
        company_main_layout.addWidget(self.add_to_watchlist_button)
        self.add_to_watchlist_button.clicked.connect(self.to_add_company)
    

    def update_company_info(self,company):
        self.company_name_label.setText(f'Company Name: {company.get('Name','Not found')}')
        self.company_symbol_label.setText(f'Company Symbol: {company.get('Symbol','-')}')
        self.company_country_label.setText(f'Company Country: {company.get('Country','-')}')
        self.company_industry_label.setText(f'Company Industry: {company.get('Industry','-')}')
        self.current_company=company
        self.add_to_watchlist_button.show()
        self.add_to_watchlist_button.setEnabled(True)
        self.add_to_watchlist_button.setText('Add to Watchlist')


    def clear_company_not_found(self):
        self.company_name_label.setText(f'Company Name: -')
        self.company_symbol_label.setText(f'Company Symbol: -')
        self.company_country_label.setText(f'Company Country: -')
        self.company_industry_label.setText(f'Company Industry: -')
        self.current_company={}
        self.add_to_watchlist_button.hide()
    
    def show_company_not_found(self):
        self.clear_company_not_found()

    def to_add_company(self):
        self.addToWatchListRequested.emit(self.current_company)
        self.add_to_watchlist_button.setEnabled(False)
        self.add_to_watchlist_button.setText('Adding...')