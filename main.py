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
        self.value1 = randint(1, 300)
        self.value2 = randint(1, 300)
        self.value3 = randint(1, 300)
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
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 2, Qt.SolidLine))
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(60, 60, self.value1, self.value1)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(200, 200, self.value2, self.value2)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(500, 500, self.value3, self.value3)
        painter.setBrush(QColor(255, 255, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
