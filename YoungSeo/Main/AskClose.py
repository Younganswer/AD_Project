from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
)


# 창을 닫을 것인 지 확인하는 클래스
class AskClose(QWidget):

    def __init__(self, scene):
        QWidget.__init__(self)
        self.scene = scene
        self.initUI()
    
    def initUI(self):
        okButton     = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        okButton.clicked.connect(self.buttonClicked)
        cancelButton.clicked.connect(self.buttonClicked)

        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        askLabel = QLabel("Do you want to close?")

        grid.addWidget(askLabel, 0, 0, 1, 4) # 시작 좌표 (0, 0) && 차지하는 칸의 개수 (1, 2)
        grid.addWidget(okButton, 1, 3)
        grid.addWidget(cancelButton, 1, 4)

        self.move(300, 300)
        self.setWindowTitle('Really?')
        # self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.scene.view.close()
            self.close()

    def buttonClicked(self):

        button = self.sender()
        key = button.text()
        
        if key == "Cancel":
            self.close()

        elif key == "OK":
            self.scene.view.close()
            self.close()