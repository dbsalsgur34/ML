import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random
import time

width = 300
height = 300
numofk = 3

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = width
        self.height = height
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
        self.show()


class PaintWidget(QWidget):
    datalist = []
    points = []
    clusters = []

    def paintEvent(self, event):
        qp = QPainter(self)
        colors = [Qt.blue, Qt.red, Qt.green, Qt.cyan, Qt.magenta, Qt.yellow]

        for k in range(0, self.clusters.__len__()):
            qp.setPen(colors[k])

            for i in range(0, self.clusters[k].__len__()):
                qp.drawPoint(self.datalist[self.clusters[k][i]][0], self.datalist[self.clusters[k][i]][1])


    def appendData(self, x, y):
        self.datalist.append([x, y])

    def setDatalist(self, newdatalist):
        self.datalist = newdatalist

    def setPoints(self, newpoints):
        self.points = newpoints

    def setClusters(self, clusters):
        self.clusters = clusters


def function1():
    def y(x):
        return x

    newdatalist = []

    for i in range(0, width):
        newdatalist.append([i, y(i) + random.randint(-20, 20)])
    return newdatalist


def function2():
    def y(x):
        return (x/40)**2 + height/10

    newdatalist = []

    for i in range(0, width):
        newdatalist.append([i, y(i) + random.randint(-20, 20)])
    return newdatalist


def kmeans(k, data):
    #p = random.randint(-width//2, width//2-k)
    p = 0
    points = []
    newpoints = []
    clusters = []

    for initpoint in range(k):
        points.append(data[p + initpoint])
        clusters.append([])


    while True:

        for index in range(0, data.__len__()):
            distance = []
            for initpoint in range(0, k):
                distance.append((data[index][0] - points[initpoint][0]) ** 2 +
                                (data[index][1] - points[initpoint][1]) ** 2)

            result = closest(distance)
            clusters[result].append(index)

        for i in range(k):
            sumX = 0
            sumY = 0
            for index in range(clusters[i].__len__()):
                sumX += data[clusters[i][index]][0]
                sumY += data[clusters[i][index]][1]

            newpoints.append([sumX//(clusters[i].__len__()), sumY//(clusters[i].__len__())])
        print(points, newpoints)
        if points.__eq__(newpoints):
            break
        else:
            clusters = [[], [], []]
            points = newpoints
            newpoints = []


    print(clusters.__len__())
    return clusters


def closest(distances):
    clst = distances[0]
    index = 0

    for i in range(1, distances.__len__()):
        if distances[i] < clst:
            clst = distances[i]
            index = i

    return index


if __name__ == '__main__':
    app = QApplication(sys.argv)

    datalist1 = function1()
    ex1 = App()
    ex1.m.setDatalist(datalist1)
    ex1.m.setClusters(kmeans(numofk, datalist1))

    datalist2 = function2()
    ex2 = App()
    ex2.m.setDatalist(datalist2)
    ex2.m.setClusters(kmeans(numofk, datalist2))
    sys.exit(app.exec_())
