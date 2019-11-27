import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class CustomizeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,100,100)
        self.setWindowTitle('Customize Screen')

        lbl1 = QLabel('입력: ')
        lbl2 = QLabel('입력: ')
        lbl3 = QLabel('입력: ')

        self.LE1 = QLineEdit()
        self.LE2 = QLineEdit()
        self.LE3 = QLineEdit()

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        saveButton = QPushButton("Save")
        cancelButton = QPushButton("Cancel")

        addButton.clicked.connect(self.Click_addButton)
        delButton.clicked.connect(self.Click_delButton)
        saveButton.clicked.connect(self.Click_saveButton)
        cancelButton.clicked.connect(self.Click_cancelButton)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()

        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)

        vbox2.addLayout(hbox4)
        vbox1.addLayout(hbox5)

        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)

        hbox1.addWidget(lbl1)
        hbox1.addWidget(self.LE1)
        hbox2.addWidget(lbl2)
        hbox2.addWidget(self.LE2)
        hbox3.addWidget(lbl3)
        hbox3.addWidget(self.LE3)

        hbox4.addWidget(addButton)
        hbox4.addWidget(delButton)

        hbox5.addWidget(saveButton)
        hbox5.addWidget(cancelButton)

        self.setLayout(vbox3)
        self.show()

    def Click_addButton(self):
        pass

    def Click_delButton(self):
        pass

    def Click_saveButton(self):
        pass

    def Click_cancelButton(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = CustomizeScreen()
    sys.exit(app.exec_())




    # def game_update(self):
    #     if (addButton):
    #         lbl5 = QLabel()
    #         hbox1.addWidget(lbl5)





