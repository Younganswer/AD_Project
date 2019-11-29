import random
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsPixmapItem


path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Help_Choose/'

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
ENEMY_SPONE_X = 800
ENEMY_SPONE_Y = 600
ENEMY_FRAMES  = 500

imageWidth=128
dx=60
dy=15

# 음식 설정 클래스
class FoodInfo(QGraphicsPixmapItem):

    sound = QSound(path+'Bonus/sfx_retro_spaceship_explosion.wav')
    foodLocation = [(100, 100), (100+dx, 100-dy), (100+dx*2, 100-dy*2), (100+dx*3, 100-dy*3),
                    (700-imageWidth-dx*3, 100-dy*3), (700-imageWidth-dx*2, 100-dy*2), (700-imageWidth-dx, 100-dy), (700-imageWidth, 100),
                    (700-imageWidth, 164), (700-imageWidth-dx, 164+dy), (700-imageWidth-dx*2, 164+dy*2), (700-imageWidth-dx*3, 164+dy*3),
                    (100+dx*3, 100+dy*3), (100+dx*2, 100+dy*2), (100+dx, 164+dy), (100, 164)]
                
                          
    def __init__(self, image, food, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(path+image))
        self.pos = 0
        self.food = food
        
    def game_update(self, bullets):
        self.pos += 1
        if (self.pos > len(self.foodLocation)-1):
            self.pos -= len(self.foodLocation)
        x, y = self.foodLocation[self.pos][0], self.foodLocation[self.pos][1]
        self.setPos(x, y)
        for i in range(len(bullets)):
            if (self.x() <= bullets[i].x() <= self.x() + self.pixmap().width() and self.y() <= bullets[i].y() <= self.y() + self.pixmap().width()):
                bullets[0].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[1].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[2].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                return True

