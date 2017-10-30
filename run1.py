import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random





class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)


        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(self.width, self.height)
        for i in range(1, 1024):
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            self.m.appendData(x, y)
        self.show()

    def drawPoints(self):
        for i in range(1, 2):
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            self.m.appendData(x, y)


class dataset():
    def __init__(self):
        self.color = Qt.white
        self.list = []

    def setColor(self, color):
        self.color = color

    def append(self, x, y):
        self.list.append(x, y)


class PaintWidget(QWidget):
    datalist = []
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(self.color)

        for i in range(1, self.datalist.__len__()-500):
            x = self.datalist[i][0]
            y = self.datalist[i][1]
            qp.drawPoint(x, y)

        qp.setPen(Qt.red)

        for i in range(self.datalist.__len__()-499, self.datalist.__len__()):
            x = self.datalist[i][0]
            y = self.datalist[i][1]
            qp.drawPoint(x, y)

    def appendData(self, x, y):
        self.datalist.append([x, y])

    def setColor(self, color):
        self.color = color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.m.setColor(Qt.blue)
    ex.drawPoints()
    print(ex.m.datalist.__len__())
    sys.exit(app.exec_())
