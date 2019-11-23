import sys
import random
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

from AskClose   import AskClose
from BackGround import BackGround
from Bullet     import Bullet
from Enemy      import Enemy
from Player     import Player
from EXP        import EXP
from LifeInfo   import PlayerIcon, XIcon, Life

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
PLAYER_BULLET_X_OFFSETS = [0, 45, 90]
PLAYER_BULLET_Y         = 15
BULLET_SPEED            = 10  # pix/frame
BULLET_FRAMES           = 50
FRAME_TIME_MS           = 16  # ms/frame
# frame * ms/frame = ms  =>  frame(y) = whole_ms(x) / frame_ms(16)
ENEMY_SPONE_X           = 800
ENEMY_SPONE_Y           = 600
ENEMY_FRAMES            = 500
CHANGE_FRAMES           = 180


class Stage(QGraphicsPixmapItem):

    stageArray = []
    stage1 = ""
    stage2 = ""
    stage3 = ""
    stageArray.extend(["", stage1, stage2, stage3])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stage = 1
        self.frame = 0
        self.change = False
        self.stageUp = False
        self.setPixmap(QPixmap(self.stageArray[self.stage]))
    
    def game_update(self, exp):
        if not self.change:
            if exp == 0 and not self.stageUp:
                self.change  = True
                self.stageUp = True
                self.stage = 1
                self.frame = CHANGE_FRAMES
                self.setPixmap(QPixmap(self.stageArray[self.stage]))
                self.setPos((SCREEN_WIDTH-self.pixmap().width())/2,
                            (SCREEN_HEIGHT-self.pixmap().height())/2)
            
            elif 0 < exp < 10:
                self.stageUp = False


            elif exp == 10 and not self.stageUp:
                self.change = True
                self.stageUp = True
                self.stage = 2
                self.frame = CHANGE_FRAMES
                self.setPixmap(QPixmap(self.stageArray[self.stage]))
                self.setPos((SCREEN_WIDTH-self.pixmap().width())/2,
                            (SCREEN_HEIGHT-self.pixmap().height())/2)
            elif 10 < exp < 20:
                self.stageUp = False

            elif exp == 20 and not self.stageUp:
                self.change = True
                self.stageUp = True
                self.stage = 3
                self.frame = CHANGE_FRAMES
                self.setPixmap(QPixmap(self.stageArray[self.stage]))
                self.setPos((SCREEN_WIDTH-self.pixmap().width())/2,
                            (SCREEN_HEIGHT-self.pixmap().height())/2)
            
            elif exp > 20:
                self.stageUp = False

        else:
            self.frame -= 1
            if self.frame < 0:
                self.change = False