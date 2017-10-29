from PyQt5.QtWidgets import *


class myWidget(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # 레이블,Edit,버튼 컨트롤
        label1 = QLabel("images.jpeg")

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(label1)

        # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)


app = QApplication([])
dialog = myWidget()
dialog.show()
app.exec_()