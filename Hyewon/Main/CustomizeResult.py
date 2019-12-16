import sys
import random
import time
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import (
    Qt,
    QBasicTimer
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap
)
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)
path = '/home/user/PycharmProjects/AD_Project/Hyewon/'

class CustomizeResult(QGraphicsPixmapItem):
    def __init__(self, image, main, parent = None):
        super().__init__(parent)
        self.setPixmap(QPixmap(path+image))
        self.main = main
