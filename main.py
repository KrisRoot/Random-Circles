import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Круги')

        self.button = QPushButton('Добавить круги', self)
        self.button.move(150, 350)
        self.button.clicked.connect(self.on_click)
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        dia = random.randint(10, 200)
        x = random.randint(10, 350)
        y = random.randint(10, 300)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(x, y, dia, dia)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
