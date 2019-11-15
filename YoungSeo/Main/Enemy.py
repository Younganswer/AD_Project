import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
ENEMY_SPONE_X           = 800
ENEMY_SPONE_Y           = 600
ENEMY_FRAMES            = 500



# 적 설정 클래스
class Enemy(QGraphicsPixmapItem):

    enemyArray = []
    enemyBlack = 'PNG/Enemies/enemyBlack1.png'
    enemyBlue  = 'PNG/Enemies/enemyBlue2.png'
    enemyGreen = 'PNG/Enemies/enemyGreen3.png'
    enemyRed   = 'PNG/Enemies/enemyRed4.png'
    enemyArray.extend([enemyBlack, enemyBlue, enemyGreen, enemyRed])

    enemyPosArray = [(0, 0),   (100, 0),   (200, 0),   (300, 0),   (400, 0),   (500, 0),   (600, 0),   (700, 0),
                     (0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)]
                          
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.enemy = random.randint(0, 3)
        self.setPixmap(QPixmap(self.enemyArray[self.enemy]))
        self.spone = False
        self.frames = 0

    def game_update(self, enemies, idx):
        if not self.spone:
            self.spone = True
            enemyPos = random.randint(0, 15)
            Pos_x, Pos_y = self.enemyPosArray[enemyPos][0], self.enemyPosArray[enemyPos][1]
            self.setPos(Pos_x, Pos_y)
            self.frames = ENEMY_FRAMES
            enemies.append(1)
        
        else:
            self.frames -= 1
            if 1 < self.frames <= 100:
                self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.enemy = random.randint(0, 3)
            
            elif 0 < self.frames <= 1:
                print(enemies, idx)

            elif self.frames < 0:
                idx += 1