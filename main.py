import sys

from PyQt5 import uic
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag()
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self):
        value1 = randint(1, 300)
        value2 = randint(1, 300)
        value3 = randint(1, 300)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.drawEllipse(60, 60, value1, value1)
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.drawEllipse(200, 200, value2, value2)
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.drawEllipse(500, 500, value3, value3)
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
