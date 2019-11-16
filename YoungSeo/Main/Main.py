import os
os.chdir('C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/YoungSeo')
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



# 메인 클래스
class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        # bg = QGraphicsRectItem()
        # bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)
        # bg.setBrush(QBrush(Qt.black))
        self.bg = BackGround()
        self.addItem(self.bg)

        self.player = Player()
        self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2,
                           (SCREEN_HEIGHT-self.player.pixmap().height())/2)
        self.addItem(self.player)


        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                        Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                        Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
        for b in self.bullets:
            b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.addItem(b)

        self.enemies = [Enemy()]
        self.enemies[0].setPos(SCREEN_WIDTH, 0)
        self.addItem(self.enemies[0])
        self.idx = [0]

        self.EXP = EXP()
        self.EXP.score = 8
        self.EXP.setPos(SCREEN_WIDTH-40, 20)
        self.addItem(self.EXP)

        self.EXP1 = EXP()
        self.EXP1.score = 1
        self.EXP1.setPos(SCREEN_WIDTH-60, 20)
        self.addItem(self.EXP1)


        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

        self.ask = AskClose(self)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())
        if event.key() == Qt.Key_Escape:
            self.ask.show()
            

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for b in self.bullets:
            b.game_update(self.keys_pressed, self.player)
        self.enemies[self.idx[0]].game_update(self.enemies, self.idx, self.bullets, self.EXP)
        self.EXP.game_update(self.EXP1)
        self.EXP1.game_update(self.EXP1)

        if self.enemies[-1] == 1:
            self.enemies[-1] = Enemy()
            self.enemies[-1].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.addItem(self.enemies[-1])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())