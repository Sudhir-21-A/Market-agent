from PySide6.QtWidgets import QWidget,QListWidget,QFrame,QVBoxLayout,QListWidgetItem
from PySide6.QtCore import Qt,Signal



class SearchResultsWidget(QWidget):
    companySelected=Signal(str)
    def __init__(self):
        super().__init__()
        search_results_frame=QFrame()
        search_results_frame.setFrameShape(QFrame.Shape.Box)
        search_results_frame_layout=QVBoxLayout(search_results_frame)
        search_results_main_layout=QVBoxLayout(self)
        self.search_results_list=QListWidget()
        search_results_frame_layout.addWidget(self.search_results_list)
        search_results_main_layout.addWidget(search_results_frame)
        self.search_results_list.itemClicked.connect(self.item_clicked)



    def show_results(self,query_list):
        self.search_results_list.clear()
        count=0
        for result in query_list:
            count+=1
            item=QListWidgetItem(f'{count}) {result['description']}\t({result['symbol']})')
            item.setData(Qt.ItemDataRole.UserRole,result['symbol'])
            self.search_results_list.addItem(item)


    def item_clicked(self,item):
        symbol=item.data(Qt.ItemDataRole.UserRole)
        self.companySelected.emit(symbol)

    

