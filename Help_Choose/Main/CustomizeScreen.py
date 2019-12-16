# status를 이용해서 최소 3개이상 이니셜 되어 있어야 한다고 표시
# sender = self.sender()
# self.statusBar().showMessage("")

import sys
import random
import time
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
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QTextEdit,
    QLineEdit,
    QGridLayout,
    QLabel,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)

imageWidth=128
dx=60
dy=15

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/Youngseo/'
#path = '/home/user/PycharmProjects/AD_Project/Hyewon/'

class CustomizeScreen(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

    def initUI(self):
        self.setGeometry(300,300,400,100)
        self.setWindowTitle('Customize Screen')
        # grid = QGridLayout()
        # self.setLayout(grid)
        self.initialized = 3
        self.cancel = False

        self.lbl1 = QLabel('입력: ')
        self.lbl2 = QLabel('입력: ')
        self.lbl3 = QLabel('입력: ')
        self.lbl4 = QLabel('입력: ')
        self.lbl5 = QLabel('입력: ')
        self.lbl6 = QLabel('입력: ')
        self.lbl7 = QLabel('입력: ')
        self.lbl8 = QLabel('입력: ')
        self.lbl9 = QLabel('입력: ')
        self.lbl10 = QLabel('입력: ')
        self.lbl11 = QLabel('')
        self.lbl11.setAlignment(Qt.AlignCenter)

        self.LE1 = QLineEdit()
        self.LE2 = QLineEdit()
        self.LE3 = QLineEdit()
        self.LE4 = QLineEdit()
        self.LE5 = QLineEdit()
        self.LE6 = QLineEdit()
        self.LE7 = QLineEdit()
        self.LE8 = QLineEdit()
        self.LE9 = QLineEdit()
        self.LE10 = QLineEdit()

        self.delButton1 = QPushButton("Del")
        self.delButton2 = QPushButton("Del")
        self.delButton3 = QPushButton("Del")
        self.delButton4 = QPushButton("Del")
        self.delButton5 = QPushButton("Del")
        self.delButton6 = QPushButton("Del")
        self.delButton7 = QPushButton("Del")
        self.delButton8 = QPushButton("Del")
        self.delButton9 = QPushButton("Del")
        self.delButton10 = QPushButton("Del")

        self.addButton = QPushButton("Add")
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")


        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()
        self.hbox8 = QHBoxLayout()
        self.hbox9 = QHBoxLayout()
        self.hbox10 = QHBoxLayout()

        self.hbox11 = QHBoxLayout()
        self.hbox12 = QHBoxLayout()
        self.hbox13 = QHBoxLayout()

        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()

        self.hboxList = [self.hbox1,self.hbox2,self.hbox3,self.hbox4,self.hbox5,self.hbox6,self.hbox7,self.hbox8,self.hbox9,self.hbox10]

        self.vbox1.addLayout(self.hboxList[0])
        self.vbox1.addLayout(self.hboxList[1])
        self.vbox1.addLayout(self.hboxList[2])

        self.vbox2.addLayout(self.hbox13)
        self.vbox2.addLayout(self.hbox11)
        self.vbox2.addLayout(self.hbox12)

        self.vbox3.addLayout(self.vbox1)
        self.vbox3.addLayout(self.vbox2)

        self.hbox1.addWidget(self.lbl1)
        self.hbox1.addWidget(self.LE1)
        self.hbox1.addWidget(self.delButton1)
        self.hbox2.addWidget(self.lbl2)
        self.hbox2.addWidget(self.LE2)
        self.hbox2.addWidget(self.delButton2)
        self.hbox3.addWidget(self.lbl3)
        self.hbox3.addWidget(self.LE3)
        self.hbox3.addWidget(self.delButton3)
        self.hbox4.addWidget(self.lbl4)
        self.hbox4.addWidget(self.LE4)
        self.hbox4.addWidget(self.delButton4)
        self.hbox5.addWidget(self.lbl5)
        self.hbox5.addWidget(self.LE5)
        self.hbox5.addWidget(self.delButton5)
        self.hbox6.addWidget(self.lbl6)
        self.hbox6.addWidget(self.LE6)
        self.hbox6.addWidget(self.delButton6)
        self.hbox7.addWidget(self.lbl7)
        self.hbox7.addWidget(self.LE7)
        self.hbox7.addWidget(self.delButton7)
        self.hbox8.addWidget(self.lbl8)
        self.hbox8.addWidget(self.LE8)
        self.hbox8.addWidget(self.delButton8)
        self.hbox9.addWidget(self.lbl9)
        self.hbox9.addWidget(self.LE9)
        self.hbox9.addWidget(self.delButton9)
        self.hbox10.addWidget(self.lbl10)
        self.hbox10.addWidget(self.LE10)
        self.hbox10.addWidget(self.delButton10)

        self.hbox11.addWidget(self.addButton)
        self.hbox12.addWidget(self.saveButton)
        self.hbox12.addWidget(self.cancelButton)
        self.hbox13.addWidget(self.lbl11)

        self.addButton.clicked.connect(self.Click_addButton)
        self.saveButton.clicked.connect(self.Click_saveButton)
        self.cancelButton.clicked.connect(self.Click_cancelButton)

        self.infoDic = {0: {'del': self.delButton1, 'le': self.LE1, 'lbl': self.lbl1, 'hbox': self.hbox1},
                        1: {'del': self.delButton2, 'le': self.LE2, 'lbl': self.lbl2, 'hbox': self.hbox2},
                        2: {'del': self.delButton3, 'le': self.LE3, 'lbl': self.lbl3, 'hbox': self.hbox3},
                        3: {'del': self.delButton4, 'le': self.LE4, 'lbl': self.lbl4, 'hbox': self.hbox4},
                        4: {'del': self.delButton5, 'le': self.LE5, 'lbl': self.lbl5, 'hbox': self.hbox5},
                        5: {'del': self.delButton6, 'le': self.LE6, 'lbl': self.lbl6, 'hbox': self.hbox6},
                        6: {'del': self.delButton7, 'le': self.LE7, 'lbl': self.lbl7, 'hbox': self.hbox7},
                        7: {'del': self.delButton8, 'le': self.LE8, 'lbl': self.lbl8, 'hbox': self.hbox8},
                        8: {'del': self.delButton9, 'le': self.LE9, 'lbl': self.lbl9, 'hbox': self.hbox9},
                        9: {'del': self.delButton10, 'le': self.LE10, 'lbl': self.lbl10, 'hbox': self.hbox10}}

        self.starImgList = ['PNG/Number/one.png',   'PNG/Number/two.png',   'PNG/Number/three.png',
                            'PNG/Number/four.png',  'PNG/Number/five.png',  'PNG/Number/six.png',
                            'PNG/Number/seven.png', 'PNG/Number/eight.png', 'PNG/Number/nine.png', 'PNG/Number/ten.png']

        self.initializedList = []
        self.customizeDic = {}
        for i in range(3):
            self.initializedList.append(self.infoDic[i]['hbox'])
        for i in range(3, 10):
            self.infoDic[i]['del'].hide()
            self.infoDic[i]['le'].hide()
            self.infoDic[i]['lbl'].hide()

        for i in range(len(self.infoDic)):
            self.infoDic[i]['del'].clicked.connect(lambda state, x=i: self.Click_delButton(x))

        self.setLayout(self.vbox3)
        self.show()

    def Click_addButton(self):
        for i in range(len(self.infoDic)):
            if self.infoDic[i]['hbox'] not in self.initializedList:
                self.initializedList.append(self.infoDic[i]['hbox'])
                self.vbox1.addLayout(self.infoDic[i]['hbox'])
                self.infoDic[i]['del'].show()
                self.infoDic[i]['le'].show()
                self.infoDic[i]['lbl'].show()
                self.initialized += 1
                break

        if self.initialized >= 10:
            self.lbl11.setText("Up to 10 can be entered.")
            self.addButton.hide()
            self.vbox2.removeItem(self.hbox11)

        print(self.initialized)

    def Click_delButton(self, x):
        if self.initialized > 3:
            self.infoDic[x]['le'].setText("")
            self.infoDic[x]['le'].hide()
            self.infoDic[x]['lbl'].hide()
            self.infoDic[x]['del'].hide()
            self.vbox1.removeItem(self.infoDic[x]['hbox'])
            self.initializedList.remove(self.infoDic[x]['hbox'])

        else:
            print("It has to more than 3.")
            self.lbl11.setText("You must enter at least three")
            return

        if self.initialized == 10:
            self.saveButton.hide()
            self.cancelButton.hide()
            self.vbox2.removeItem(self.hbox12)
            self.vbox2.addLayout(self.hbox11)
            self.addButton.show()
            self.vbox2.addLayout(self.hbox12)
            self.saveButton.show()
            self.cancelButton.show()

        self.initialized -= 1

        print(self.initialized)

    def Click_saveButton(self):
        count = 0
        for i in range(len(self.initializedList)):
            if (len(self.infoDic[i]['le'].text()) != 0):
                count += 1

        if count < 3:
            self.lbl11.setText("You must enter at least three")

        else:
            for i in range(len(self.initializedList)):
                if (len(self.infoDic[i]['le'].text()) != 0):
                    self.customizeDic[i] = {'image': self.starImgList[i], 'text': self.infoDic[i]['le'].text()}
            print(self.customizeDic)
            self.close()
            self.main.customizeDic = self.customizeDic

    def Click_cancelButton(self):
        self.cancel = True
        self.close()


class Customize(QGraphicsPixmapItem):

    selectLocation = [(100, 100), (100+dx, 100-dy), (100+dx*2, 100-dy*2), (100+dx*3, 100-dy*3),
                    (700-imageWidth-dx*3, 100-dy*3), (700-imageWidth-dx*2, 100-dy*2), (700-imageWidth-dx, 100-dy), (700-imageWidth, 100),
                    (700-imageWidth, 164), (700-imageWidth-dx, 164+dy), (700-imageWidth-dx*2, 164+dy*2), (700-imageWidth-dx*3, 164+dy*3),
                    (100+dx*3, 100+dy*3), (100+dx*2, 100+dy*2), (100+dx, 164+dy), (100, 164)]

    def __init__(self, pixmap, text, main=None, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(path+pixmap))
        self.pos = 0
        self.imagePath = pixmap
        self.main = main
        self.select = text


    def game_update(self, bullets):
        self.pos += 1
        if (self.pos > len(self.selectLocation)-1):
            self.pos -= len(self.selectLocation)
        x, y = self.selectLocation[self.pos][0], self.selectLocation[self.pos][1]
        self.setPos(x, y)
        for i in range(len(bullets)):
            if (self.x() <= bullets[i].x() <= self.x() + self.pixmap().width() and bullets[i].y() <= self.y() + self.pixmap().height()):
                bullets[0].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[1].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                bullets[2].setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.main.screen        = self.imagePath
                self.main.selectText    = self.select
                self.main.isInitialized = False
                self.main.clear()
                return True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = CustomizeScreen()
    sys.exit(app.exec_())