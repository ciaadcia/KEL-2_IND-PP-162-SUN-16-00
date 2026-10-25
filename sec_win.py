from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from intsr import *
from final_win import *

class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setapper()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton( txt_sendresult, self)
        self.btn_next.cliked.connect(self.next_click)
        layout = QVBoxLayout()
        layout.addWidget(self.btn_next, aligment = Qt.AlignCenter)
        
    def next_click(self):
        self.hide()
        self.fw = finalwin()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize (win_width, win_height)
        self.move(win_x, win_y)
