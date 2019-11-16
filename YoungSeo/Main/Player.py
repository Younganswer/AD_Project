from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsPixmapItem

path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/YoungSeo/'


PLAYER_SPEED  = 3   # pix/frame
DEAD_FRAME    = 3000 / 16
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# 플레이어 설정 클래스
class Player(QGraphicsPixmapItem):

    IS_DEAD = False
    sound = QSound(path+'Bonus/sfx_shieldDown.wav')

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(path+'PNG/playerShip1_blue.png'))
        self.deadFrame = DEAD_FRAME
        # Player로 만들어진 객체에 image를 옮겨준다. QPixmap클래스의 메소드.

    def game_update(self, keys_pressed, enemy, life):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed:
            dx += PLAYER_SPEED
        if Qt.Key_Up in keys_pressed:
            dy -= PLAYER_SPEED
        if Qt.Key_Down in keys_pressed:
            dy += PLAYER_SPEED
        
        if not self.IS_DEAD:

            if 0 <= self.x()+dx <= 695 and 0 <= self.y()+dy <= 520:
                self.setPos(self.x()+dx, self.y()+dy)

            if (enemy.x() <= self.x() <= enemy.x() + 90 or enemy.x() <= self.x() + 90 <= enemy.x() + 90)\
                and (enemy.y() <= self.y() <= enemy.y() + 90 or enemy.y() <= self.y() + 90 <= enemy.y() + 90):
                self.setPixmap(QPixmap(path+'PNG/Damage/playerShip1_damage2'))
                life.life -= 1
                self.sound.play()
                self.IS_DEAD = True

        elif self.IS_DEAD:
            dx, dy = 0, 0
            self.deadFrame -= 1
            if self.deadFrame < 0:
                self.setPixmap(QPixmap(path+'PNG/playerShip1_blue.png'))
                self.setPos((SCREEN_WIDTH-self.pixmap().width())/2,
                            (SCREEN_HEIGHT-self.pixmap().height())/2)
                self.deadFrame = DEAD_FRAME
                self.IS_DEAD = False