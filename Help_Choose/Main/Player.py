from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsPixmapItem

#path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Help_Choose/'
path = '/home/user/PycharmProjects/AD_Project/Help_Choose/'

PLAYER_SPEED  = 4   # pix/frame
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# 플레이어 설정 클래스
class Player(QGraphicsPixmapItem):

    sound = QSound(path+'Bonus/player_death.wav')

    def __init__(self, parent=None):
        self.IS_DEAD = False
        super().__init__(parent)
        self.setPixmap(QPixmap(path+'PNG/Player_Images/playerShip1_blue.png'))
        # Player로 만들어진 객체에 image를 옮겨준다. QPixmap클래스의 메소드.

    def game_update(self, keys_pressed):
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

        if 0 <= self.x()+dx <= 695 and 0 <= self.y()+dy <= 520:
            self.setPos(self.x()+dx, self.y()+dy)