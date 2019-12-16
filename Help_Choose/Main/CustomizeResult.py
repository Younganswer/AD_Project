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
path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Help_Choose/'
#path = '/home/user/PycharmProjects/AD_Project/Hyewon/'
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
class CustomizeResult(QGraphicsPixmapItem):
    def __init__(self, image, main, parent = None):
        super().__init__(parent)
        self.setPixmap(QPixmap(path+image))
        self.main = main


class CustomizeRetry(QGraphicsPixmapItem):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(path + 'PNG/Food_Info/retry.png'))
        self.main = main

    def game_update(self, bullets):
        for i in range(len(bullets)):
            if (self.x() <= bullets[i].x() <= self.x() + self.pixmap().width() and bullets[
                i].y() <= self.y() + self.pixmap().height()):
                bullets[0].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[1].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[2].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.main.screen = "CustomizeScreen"
                self.main.initUI = True
                self.main.isInitialized = False
                self.main.clear()
                return True