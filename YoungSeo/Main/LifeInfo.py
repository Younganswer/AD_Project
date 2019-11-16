from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem


class PlayerIcon(QGraphicsPixmapItem):
    
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap('PNG/UI/playerLife1_blue'))



class XIcon(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap('PNG/UI/numeralX'))



class Life(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap('PNG/UI/numeral3'))

    def game_update(self):
        pass
        
