import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/YoungSeo/'



# 게임 배경 설정 클래스
class BackGround(QGraphicsPixmapItem):

    mapArray    = []
    mapBlack    = path+'Backgrounds/black.png'
    mapBlue     = path+'Backgrounds/blue.png'
    mapDarkBlue = path+'Backgrounds/darkPurple.png'
    mapPurple   = path+'Backgrounds/purple.png'
    mapArray.extend([mapBlack, mapBlue, mapDarkBlue, mapPurple])

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        mapColor = random.randint(0, 3)
        self.setPixmap(QPixmap(self.mapArray[mapColor]))
        self.setPos(0, 0)