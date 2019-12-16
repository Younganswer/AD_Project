# status를 이용해서 최소 3개이상 이니셜 되어 있어야 한다고 표시


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class CustomizeScreen(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setGeometry(300,300,400,100)
        self.setWindowTitle('Customize Screen')
        # grid = QGridLayout()
        # self.setLayout(grid)
        self.initialized = 3

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

        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()

        self.hboxList = [self.hbox1,self.hbox2,self.hbox3,self.hbox4,self.hbox5,self.hbox6,self.hbox7,self.hbox8,self.hbox9,self.hbox10]

        self.vbox1.addLayout(self.hboxList[0])
        self.vbox1.addLayout(self.hboxList[1])
        self.vbox1.addLayout(self.hboxList[2])

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

        self.initializedList = []
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

        self.customizeList = []

    def Click_addButton(self):
        if self.initialized < 10:
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
        for i in range(10):
            if (len(self.LEList[i].text()) != 0):
                self.customizeList.append(self.LEList[i].text())
                print(self.LEList[i].text())
        print(self.customizeList)
        self.close()

    def Click_cancelButton(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = CustomizeScreen()
    sys.exit(app.exec_())