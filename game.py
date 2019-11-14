#
# Simple start to a game in PyQt5
#   move with arrow keys, spacebar to fire bullets
# Used graphics from https://opengameart.org/content/space-shooter-redux
# (reduced by 50%)
# Got some hints from https://www.youtube.com/watch?v=8ntEQpg7gck series
# and http://zetcode.com/gui/pyqt5/tetris/
#
import sys
import random
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

class AskClose(QWidget):

    def __init__(self):
        super().__init__(self)
        self.initUI()
    
    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(20)

        self.askLabel = QLabel("Do you want to close?")

        grid.addWidget(okButton)
        grid.addWidget(cancelButton)
        grid.addWidget(askLabel)

        self.move(300, 300)
        self.setWindowTitle('Really?')
        self.show()



class BackGround(QGraphicsPixmapItem):
    mapArray = []
    mapBlack = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/Backgrounds/black'
    mapBlue = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/Backgrounds/blue'
    mapDarkBlue = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/Backgrounds/darkPurple'
    mapPurple = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/Backgrounds/Purple'
    mapArray.extend([mapBlack, mapBlue, mapDarkBlue, mapPurple])

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        mapColor = random.randint(0, 3)
        self.setPixmap(QPixmap(self.mapArray[mapColor]))
        self.setPos(0, 0)


class Enemy(QGraphicsPixmapItem):
    enemyArray = []
    enemyBlack = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/Enemies/enemyBlack1'
    enemyBlue  = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/Enemies/enemyBlue2'
    enemyGreen = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/Enemies/enemyGreen3'
    enemyRed   = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/Enemies/enemyRed4'
    enemyArray.extend([enemyBlack, enemyBlue, enemyGreen, enemyRed])

    enemyPosArray = [(0, 0),   (100, 0),   (200, 0),   (300, 0),   (400, 0),   (500, 0),   (600, 0),   (700, 0),
                     (0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)]
                          
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.enemy = random.randint(0, 3)
        self.setPixmap(QPixmap(self.enemyArray[self.enemy]))
        self.spone = False
        self.frames = 0

    def game_update(self):
        if not self.spone:
            self.spone = True
            enemyPos = random.randint(0, 15)
            Pos_x, Pos_y = self.enemyPosArray[enemyPos][0], self.enemyPosArray[enemyPos][1]
            self.setPos(Pos_x, Pos_y)
            self.frames = ENEMY_FRAMES
        
        else:
            self.frames -= 1
            if 0 < self.frames <= 100:
                self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.enemy = random.randint(0, 3)
            elif self.frames <= 0:
                self.setPixmap(QPixmap(self.enemyArray[self.enemy]))
                self.spone = False
        


class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/playerShip1_blue.png"))
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
        self.setPos(self.x()+dx, self.y()+dy)
        # 지정된 객체의 좌표를 정해준다.


class Bullet(QGraphicsPixmapItem):
    def __init__(self, offset_x, offset_y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/File.py/SecondSemester/game/PNG/Lasers/laserBlue07.png"))
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

class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = BackGround()
        # bg = QGraphicsRectItem()
        # bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)
        # bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

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


        self.enemy = Enemy()
        self.enemy.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.addItem(self.enemy)


        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for b in self.bullets:
            b.game_update(self.keys_pressed, self.player)
        self.enemy.game_update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())