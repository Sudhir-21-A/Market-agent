from PySide6.QtWidgets import QWidget,QLabel,QTextEdit,QVBoxLayout,QFrame,QDockWidget
from PySide6.QtCore import Qt


class ExplanationDockWidget(QDockWidget):
    def __init__(self):
        super(). __init__()
        self.setWindowTitle('AI Explanation')
        explanation_frame=QFrame()
        explanation_frame.setFrameShape(QFrame.Shape.Box)
        explanation_frame_layout=QVBoxLayout(explanation_frame)
        self.ai_explanation_text=QTextEdit()
        self.ai_explanation_text.setReadOnly(True)
        explanation_frame_layout.addWidget(self.ai_explanation_text,alignment=Qt.AlignTop)
        self.setWidget(explanation_frame)
        self.hide()


    def show_info(self,text):
        self.ai_explanation_text.setText(text)

        