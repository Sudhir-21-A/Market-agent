from PySide6.QtWidgets import QWidget,QHBoxLayout,QLineEdit,QPushButton
from PySide6.QtCore import Qt


class SearchBarWidget(QWidget):
    def __init__(self):
        super(). __init__()
        layout=QHBoxLayout(self)
        self.searchbox=QLineEdit()
        self.searchbox.setPlaceholderText('Company Name:')
        self.search_button=QPushButton('SEARCH')
        self.search_button.clicked.connect(self.search_company)
        self.searchbox.returnPressed.connect(self.search_company)
        layout.addWidget(self.searchbox)
        layout.addWidget(self.search_button)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,40)

    
    def search_company(self):
        search_text=self.searchbox.text().strip()

        if not search_text:
            return 
        
        
        print(f'Searching: {search_text}')