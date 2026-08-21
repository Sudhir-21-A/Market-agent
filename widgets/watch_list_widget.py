from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget,QFrame,QPushButton,QHBoxLayout,QListWidgetItem
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QFont



class WatchListWidget(QWidget):

    refreshRequested=Signal(list)
    companyRemoved=Signal(str)

    def __init__(self):
        super(). __init__()
        self.company_list=[]
        self.current_company=""
        Frame=QFrame()
        Frame.setFrameShape(QFrame.Shape.Box)
        watchlistFrameLayout=QVBoxLayout(Frame)
        buttonWidget=QWidget()
        buttonlayout=QHBoxLayout(buttonWidget)
        watchlabel=QLabel('Current Watchlist:')
        watchlabel_font=watchlabel.font()
        watchlabel_font.setPointSize(12)
        watchlabel_font.setWeight(QFont.DemiBold)
        watchlabel.setFont(watchlabel_font)
        layout=QVBoxLayout(self)
        self.watch_list=QListWidget()
        self.refresh_button=QPushButton('Refresh')
        self.delete_button=QPushButton('Delete')
        buttonlayout.addWidget(self.refresh_button,alignment=Qt.AlignLeft)
        buttonlayout.addWidget(self.delete_button,alignment=Qt.AlignRight)
        self.refresh_button.hide()
        self.delete_button.hide()
        watchlistFrameLayout.addWidget(self.watch_list)
        watchlistFrameLayout.addWidget(buttonWidget)
        watchlistFrameLayout.setSpacing(20)
        layout.addWidget(watchlabel)
        layout.addWidget(Frame)
        self.refresh_button.clicked.connect(self.to_refresh)
        self.watch_list.itemClicked.connect(self.enable_delete)
        self.delete_button.clicked.connect(self.delete_company)
    
    def display_watch_list(self,list):
        self.watch_list.clear()
        for company in list:
            item=QListWidgetItem(f'{company['overview']['Name']} \t({company['overview']['Symbol']}) \tCurrent Price: ${company['quote']['CurrentPrice']}   \tChange Percent: {company['quote']['ChangePercent']}%',self.watch_list)
            item.setData(Qt.ItemDataRole.UserRole,company['overview']['Symbol'])
        self.refresh_button.show()
        self.delete_button.show()
        self.delete_button.setEnabled(False)
        self.refresh_button.setEnabled(True)
        self.refresh_button.setText('Refresh')
        self.delete_button.setText('Delete')

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


    def enable_delete(self,item):
        selected=self.watch_list.selectedItems()
        if selected is None:
            self.delete_button.setEnabled(False)
            return
        item=selected[0]
        self.current_company=item.data(Qt.ItemDataRole.UserRole)
        self.delete_button.setEnabled(True)


    def delete_company(self):
        self.delete_button.setEnabled(False)
        self.delete_button.setText('Deleting...')
        self.refresh_button.setEnabled(False)
        for company in self.company_list:
            if company['overview']['Symbol']==self.current_company:
                self.company_list.remove(company)
                break
        self.show_after_delete()
        self.companyRemoved.emit(self.current_company)

    

    def show_after_delete(self):
        if not self.company_list:
            self.back_to_default()

        else:
            self.display_watch_list(self.company_list)


    def show_on_startup(self,company_info_list:list):
        self.company_list=company_info_list
        self.display_watch_list(self.company_list)

    def back_to_default(self):
        self.watch_list.clear()
        self.refresh_button.hide()
        self.delete_button.hide()


        