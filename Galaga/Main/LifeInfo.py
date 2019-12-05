from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Galaga/'

class PlayerIcon(QGraphicsPixmapItem):
    
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(path+'PNG/UI/playerLife1_blue'))



class XIcon(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(path+'PNG/UI/numeralX'))



class Life(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(path+'PNG/UI/numeral3'))
        self.life = 3

    def game_update(self):
        if self.life == 2:
            self.setPixmap(QPixmap(path+'PNG/UI/numeral2'))
        
        elif self.life == 1:
            self.setPixmap(QPixmap(path+'PNG/UI/numeral1'))
        
        elif self.life == 0:
            self.setPixmap(QPixmap(path+'PNG/UI/numeral0'))
        
