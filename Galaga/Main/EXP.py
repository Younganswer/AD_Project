from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Galaga/'

class EXP(QGraphicsPixmapItem):

    numArray = [path+'PNG/UI/numeral0', path+'PNG/UI/numeral1', path+'PNG/UI/numeral2',
                path+'PNG/UI/numeral3', path+'PNG/UI/numeral4', path+'PNG/UI/numeral5',
                path+'PNG/UI/numeral6', path+'PNG/UI/numeral7', path+'PNG/UI/numeral8', path+'PNG/UI/numeral9']

    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(self.numArray[0]))
        self.score = 0
    
    def game_update(self, exp1):
        if self.score >= 10:
            self.score -= 10
            exp1.score += 1
        self.setPixmap(QPixmap(self.numArray[self.score]))
        
        