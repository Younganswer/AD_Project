import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem


# 게임 배경 설정 클래스
class BackGround(QGraphicsPixmapItem):

    mapArray    = []
    mapBlack    = 'Backgrounds/black.png'
    mapBlue     = 'Backgrounds/blue.png'
    mapDarkBlue = 'Backgrounds/darkPurple.png'
    mapPurple   = 'Backgrounds/purple.png'
    mapArray.extend([mapBlack, mapBlue, mapDarkBlue, mapPurple])

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        mapColor = random.randint(0, 3)
        self.setPixmap(QPixmap(self.mapArray[mapColor]))
        self.setPos(0, 0)