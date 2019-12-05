import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class CustomizeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,400,100)
        self.setWindowTitle('Customize Screen')
        # grid = QGridLayout()
        # self.setLayout(grid)

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
        saveButton = QPushButton("Save")
        cancelButton = QPushButton("Cancel")


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
        self.hbox12.addWidget(saveButton)
        self.hbox12.addWidget(cancelButton)

        self.addButton.clicked.connect(self.Click_addButton)
        saveButton.clicked.connect(self.Click_saveButton)
        cancelButton.clicked.connect(self.Click_cancelButton)


        self.delButtonList = [self.delButton1, self.delButton2, self.delButton3, self.delButton4, self.delButton5, self.delButton6, self.delButton7, self.delButton7, self.delButton8, self.delButton9, self.delButton10]
        self.LEList = [self.LE1, self.LE2, self.LE3, self.LE4, self.LE5, self.LE6, self.LE7, self.LE8, self.LE9, self.LE10]
        self.lblList = [self.lbl1, self.lbl2, self.lbl3, self.lbl4, self.lbl5, self.lbl6, self.lbl7, self.lbl8, self.lbl9, self.lbl10]

        #button.clicked.connect(lambda state, x=idx: self.button_pushed(x))
        for idx in range(10):
            self.delButtonList[idx].clicked.connect(lambda state,x=idx:self.Click_delButton(x))
        # self.delButton1.clicked.connect(lambda state, x=idx: self.Click_delBuuton(x))
        # self.delButton2.clicked.connect(self.Click_delButton2)
        # self.delButton3.clicked.connect(self.Click_delButton3)
        # self.delButton4.clicked.connect(self.Click_delButton4)
        # self.delButton5.clicked.connect(self.Click_delButton5)
        # self.delButton6.clicked.connect(self.Click_delButton6)
        # self.delButton7.clicked.connect(self.Click_delButton7)
        # self.delButton8.clicked.connect(self.Click_delButton8)
        # self.delButton9.clicked.connect(self.Click_delButton9)
        # self.delButton10.clicked.connect(self.Click_delButton10)

        self.setLayout(self.vbox3)
        self.show()

        self.customizeList = []

    def Click_addButton(self):
        #리스트에 넣기, 클래스 이용
        if (self.initialized<10):
            self.vbox1.addLayout(self.hboxList[self.initialized])
            self.initialized+=1
        else:
            self.addButton.hide()
            self.vbox2.removeItem(self.hbox11)

    def Click_delButton(self, x):
        self.LEList[x].setText("")
        self.LEList[x].hide()
        self.lblList[x].hide()
        self.delButtonList[x].hide()
        self.vbox1.removeItem(self.hboxList[x])
        self.addButton.show()
        self.LEList.append(self.LEList[x])
        self.lblList.append(self.lblList[x])
        self.delButtonList.append(self.delButtonList[x])
        del self.LEList[x]
        del self.lblList[x]
        del self.delButtonList[x]


    # def Click_delButton2(self):
    #     pass
    #
    # def Click_delButton3(self):
    #     pass
    #
    # def Click_delButton4(self):
    #     self.LE4.setText("")
    #     self.vbox1.removeItem(self.hbox4)
    #     self.LE4.hide()
    #     self.lbl4.hide()
    #     self.delButton4.hide()
    #     self.addButton.show()
    #     self.initialized-=1
    #
    # def Click_delButton5(self):
    #     self.LE5.setText("")
    #     self.vbox1.removeItem(self.hbox5)
    #     self.LE5.hide()
    #     self.lbl5.hide()
    #     self.delButton5.hide()
    #     self.addButton.show()
    #     self.initialized -= 1
    #
    # def Click_delButton6(self):
    #     self.LE6.setText("")
    #     self.hbox6.hide()
    #     self.addButton.show()
    #     self.initialized -= 1
    #
    # def Click_delButton7(self):
    #     self.LE7.setText("")
    #     self.hbox7.hide()
    #     self.addButton.show()
    #     self.initialized -= 1
    #
    # def Click_delButton8(self):
    #     self.LE8.setText("")
    #     self.hbox8.hide()
    #     self.addButton.show()
    #     self.initialized -= 1
    #
    # def Click_delButton9(self):
    #     self.LE9.setText("")
    #     self.hbox9.hide()
    #     self.addButton.show()
    #     self.initialized -= 1
    #
    # def Click_delButton10(self):
    #     self.LE10.setText("")
    #     self.hbox10.hide()
    #     self.addButton.show()
    #     self.initialized -= 1

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
