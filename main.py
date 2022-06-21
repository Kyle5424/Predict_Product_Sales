import sys

from PyQt5 import QtCore
import model
import docx2txt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QPlainTextEdit,QLabel,QFileDialog

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "Phân loại văn bản"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 200
        self.text=""
        self.classify = model.classification()
        self.initMyUI()
    def initMyUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QIcon("book.png"))
        self.txt_content= QPlainTextEdit(self)
        self.txt_content.setPlaceholderText("Nhập nội dung văn bản")
        self.txt_content.move(20,20)
        self.txt_content.setMinimumSize(360,100)
        self.txt_content.setMaximumSize(360,100)

        btn_pre =QPushButton(self)
        btn_pre.move(300,140)
        btn_pre.setText("Phân loại")
        btn_pre.setMinimumWidth(80)
        btn_pre.setMinimumHeight(30)
        btn_pre.setStyleSheet("background-color:blue; border-radius:15px; color:white;")

        btn_file = QPushButton(self)
        btn_file.move(200, 140)
        btn_file.setText("Mở tệp")
        btn_file.setMinimumWidth(80)
        btn_file.setMinimumHeight(30)
        btn_file.setStyleSheet("background-color:blue; border-radius:15px; color:white;")

        btn_pre.clicked.connect(self.on_click)
        btn_file.clicked.connect(self.on_click_file)
        self.lbl_res= QLabel(self)
        self.lbl_res.setText("Kết quả")
        self.lbl_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_res.move(20, 140)
        self.lbl_res.setMinimumWidth(80)
        self.lbl_res.setMinimumHeight(30)
        self.lbl_res.setStyleSheet("background-color:blue; border-radius:15px; color:white;")
        self.show()
    @pyqtSlot()
    def on_click_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn một tệp", "",
                                                      "All Files (*);;Text Files (*.txt);;Document (*.doc or *.docx)", options=options)
        if fileName:
            import textLib
            if ("docx" or "dox") in fileName:
                text = docx2txt.process(fileName)
                text= textLib.Text(text).str
            if "txt" in fileName:
                with open(fileName, encoding="utf-8") as f:
                    text = f.read()
                    text = textLib.Text(text).str
            self.txt_content.setPlainText(text)
    @pyqtSlot()
    def on_click(self):
        text=self.txt_content.toPlainText()
        self.lbl_res.setText("Vui long doi")
        res=self.classify.sk_predictions(text)
        self.lbl_res.setText(res[0])
ui = QApplication(sys.argv)
ex =App()
sys.exit(ui.exec())