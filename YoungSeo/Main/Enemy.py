import random
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsPixmapItem


path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/YoungSeo/'

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
ENEMY_SPONE_X           = 800
ENEMY_SPONE_Y           = 600
ENEMY_FRAMES            = 500



# 적 설정 클래스
class Enemy(QGraphicsPixmapItem):

    enemyArray = []
    enemyBlack = path+'PNG/Enemies/enemyBlack1.png'
    enemyBlue  = path+'PNG/Enemies/enemyBlue2.png'
    enemyGreen = path+'PNG/Enemies/enemyGreen3.png'
    enemyRed   = path+'PNG/Enemies/enemyRed4.png'
    enemyArray.extend([enemyBlack, enemyBlue, enemyGreen, enemyRed])

    damageArray = []
    damage1 = path+'PNG/Damage/playerShip1_damage3'
    damage2 = path+'PNG/Damage/playerShip2_damage2'
    damage3 = path+'PNG/Damage/playerShip3_damage1'
    damageArray.extend([damage1, damage2, damage3])

    sound = QSound(path+'Bonus/sfx_retro_spaceship_explosion.wav')

    enemyPosArray = [(0, 0),   (100, 0),   (200, 0),   (300, 0),   (400, 0),   (500, 0),   (600, 0),   (700, 0),
                     (0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)]
                          
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        enemy  = random.randint(0, 3)
        self.setPixmap(QPixmap(self.enemyArray[enemy]))
        self.spone  = False
        self.frames = 0
        self.IS_DEAD = False
        self.check  = 0

    def game_update(self, enemies, idx, bullets, exp):

        if not self.spone:
            self.spone = True
            enemyPos = random.randint(0, 15)
            Pos_x, Pos_y = self.enemyPosArray[enemyPos][0], self.enemyPosArray[enemyPos][1]
            self.setPos(Pos_x, Pos_y)
            self.frames = ENEMY_FRAMES
            enemies.append(1)
            print("I'm here!", idx[0], self.frames, self.spone, Pos_x, Pos_y, " <")
        
        else:
            self.frames -= 1

            for i in range(3):
                if self.x() <= bullets[i].x() <= self.x() + 90 and bullets[i].y() <= self.y() + 50 and self.IS_DEAD == False:
                    bullets[0].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    bullets[1].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    bullets[2].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.frames = 200
                    damage = random.randint(0, 2)
                    self.setPixmap(QPixmap(self.damageArray[damage]))
                    self.sound.play()
                    exp.score += 1
                    self.IS_DEAD = True
                    break;

            if 1 < self.frames <= 100:
                self.setPos(SCREEN_WIDTH, 0)
                self.enemy = random.randint(0, 3)

            elif self.frames < 0:
                idx[0] += 1