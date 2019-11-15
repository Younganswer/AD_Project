from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

class EXP(QGraphicsPixmapItem):

    numArray = ['PNG/UI/numeral0', 'PNG/UI/numeral1', 'PNG/UI/numeral2',
                'PNG/UI/numeral3', 'PNG/UI/numeral4', 'PNG/UI/numeral5',
                'PNG/UI/numeral6', 'PNG/UI/numeral7', 'PNG/UI/numeral8', 'PNG/UI/numeral9']

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(self.numArray[0]))
        self.score = 0
    
    def game_update(self, exp1):
        if self.score >= 10:
            self.score -= 10
            exp1.score += 1
        self.setPixmap(QPixmap(self.numArray[self.score]))
        
        