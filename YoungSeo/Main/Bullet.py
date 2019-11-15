from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem



SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
BULLET_SPEED  = 10  # pix/frame
BULLET_FRAMES = 50


# 총알 설정 클래스
class Bullet(QGraphicsPixmapItem):

    def __init__(self, offset_x, offset_y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap('PNG/Lasers/laserBlue07.png'))
        # bullet이미지 할당.
        self.offset_x = offset_x
        self.offset_y = offset_y
        # bullet 좌표 설정.
        self.active = False
        self.frames = 0

    def game_update(self, keys_pressed, player):
        if not self.active:
            if Qt.Key_Space in keys_pressed:
                self.active = True
                self.setPos(player.x()+self.offset_x, player.y()+self.offset_y)
                self.frames = BULLET_FRAMES
        else:
            self.setPos(self.x(), self.y()-BULLET_SPEED)
            self.frames -= 1
            if self.frames <= 0:
                self.active = False
                self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                # 0.8초 동안 화면에서 날아감 (0.016 * 50)