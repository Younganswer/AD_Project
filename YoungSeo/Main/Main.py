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
    QPushButton,
    QGridLayout,
    QLabel,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)

from AskClose        import AskClose
from BackGround      import BackGround
from Bullet          import Bullet
from Player          import Player
from Select          import Select
from FoodCategory    import FoodCategory
from FoodChoose      import FoodChoose
from BackButton      import BackButton
from CustomizeScreen import CustomizeScreen, Customize
from FoodInfo        import FoodInfo, Retry, Home, OpenURL
import WholeFood

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



# 메인 클래스
class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)  1000 / 16 == 62.5
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        # bg = QGraphicsRectItem()
        # bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)
        # bg.setBrush(QBrush(Qt.black))

        self.screen = "InitialScreen"
        self.previousScreen = {"FoodScreen": "InitialScreen", "CustomizeScreen": "InitialScreen", "AllFood": "FoodScreen"}
        for categoryKey, value in WholeFood.wholeFoodDic.items():
            self.previousScreen[categoryKey] = "FoodScreen"
            for foodKey in value.keys():
                self.previousScreen[foodKey] = categoryKey
        self.foodImagePath = ""
        self.isAllFood = False
        self.isInitialized = False
        self.initUI = False
        self.customizeDic = {}

        # Enemies
        # self.enemies = [Enemy()]
        # self.enemies[0].setPos(SCREEN_WIDTH, 0)
        # self.addItem(self.enemies[0])
        # self.idx = [0]

        self.customize = CustomizeScreen(self)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

        self.ask = AskClose(self)


    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())
        if event.key() == Qt.Key_Escape:
            self.ask.show()
            

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())


    def timerEvent(self, event):
        self.game_update()
        self.update()


    def game_update(self):
        if self.screen == "InitialScreen":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("Black")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                # Select
                self.foodSelect = Select("PNG/Initial_Screen/fork.png", "FoodScreen", self)
                self.foodSelect.setPos(100, 100)
                self.addItem(self.foodSelect)

                self.customizeSelect = Select("PNG/Initial_Screen/customize.png", "CustomizeScreen", self)
                self.customizeSelect.setPos(700 - self.customizeSelect.pixmap().width(), 100)
                self.addItem(self.customizeSelect)

                self.isInitialized = True
            
            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.foodSelect.game_update(self.bullets):
                    return

                elif self.customizeSelect.game_update(self.bullets):
                    return
        
        elif self.screen == "FoodScreen":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround('Blue')
                self.bg.setPos(0, 0)
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                # FoodCategory
                interval = 33.333333333
                imageWidth = 100
                self.koreanFood = FoodCategory("PNG/Category/KoreanFood.png", "KoreanFood", self)
                self.koreanFood.setPos(100+interval, interval)
                self.addItem(self.koreanFood)

                self.chineseFood = FoodCategory("PNG/Category/ChineseFood.png", "ChineseFood", self)
                self.chineseFood.setPos(100+interval*2 + imageWidth, interval)
                self.addItem(self.chineseFood)

                self.japaneseFood = FoodCategory("PNG/Category/JapaneseFood.png", "JapaneseFood", self)
                self.japaneseFood.setPos(100+interval*3 + imageWidth*2, interval)
                self.addItem(self.japaneseFood)

                self.westernFood = FoodCategory("PNG/Category/WesternFood.png", "WesternFood", self)
                self.westernFood.setPos(100+interval*4 + imageWidth*3, interval)
                self.addItem(self.westernFood)

                self.allFood = FoodCategory("PNG/Category/customize.png", "AllFood", self)
                self.allFood.setPos(100+interval*5 + imageWidth*4, interval)
                self.addItem(self.allFood)

                interval = None
                imageWidth = None

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.koreanFood.game_update(self.bullets):
                    return

                elif self.chineseFood.game_update(self.bullets):
                    return

                elif self.japaneseFood.game_update(self.bullets):
                    return

                elif self.westernFood.game_update(self.bullets):
                    return
                
                elif self.allFood.game_update(self.bullets):
                    return

                elif self.backButton.game_update(self.bullets):
                    return
        
        elif self.screen == "KoreanFood":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("DarkBlue")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodList = []
                # wholeFoodDic = {'koreanFoodDic': koreanFoodDic}
                # koreanFoodDic = {'bibimbab': bibimbab}
                # bibimbab = {'image': , :, :}
                # each == bibimbab
                for key, value in WholeFood.wholeFoodDic[self.screen].items():
                    food = FoodChoose(value['image'], key, self)
                    self.foodList.append(food)
                    food = None

                length = 0
                for food in self.foodList:
                    x, y = FoodChoose.foodLocation[length][0], FoodChoose.foodLocation[length][1]
                    food.setPos(x, y)
                    food.pos = length
                    self.addItem(food)
                    length += len(FoodChoose.foodLocation) // len(self.foodList)

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.foodList)):
                    if self.foodList[i].game_update(self.bullets):
                        print(self.screen)
                        break


        elif self.screen == "ChineseFood":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("DarkBlue")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodList = []
                # wholeFoodDic = {'koreanFoodDic': koreanFoodDic}
                # koreanFoodDic = {'bibimbab': bibimbab}
                # bibimbab = {'image': , :, :}
                # each == bibimbab
                for key, value in WholeFood.wholeFoodDic[self.screen].items():
                    food = FoodChoose(value['image'], key, self)
                    self.foodList.append(food)
                    food = None
                
                length = 0
                for food in self.foodList:
                    x, y = FoodChoose.foodLocation[length][0], FoodChoose.foodLocation[length][1]
                    food.setPos(x, y)
                    food.pos = length
                    self.addItem(food)
                    length += len(FoodChoose.foodLocation) // len(self.foodList)

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.foodList)):
                    if self.foodList[i].game_update(self.bullets):
                        break
                
                

        elif self.screen == "JapaneseFood":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("DarkBlue")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodList = []
                # wholeFoodDic = {'koreanFoodDic': koreanFoodDic}
                # koreanFoodDic = {'bibimbab': bibimbab}
                # bibimbab = {'image': , :, :}
                # each == bibimbab
                for key, value in WholeFood.wholeFoodDic[self.screen].items():
                    food = FoodChoose(value['image'], key, self)
                    self.foodList.append(food)
                    food = None
                
                length = 0
                for food in self.foodList:
                    x, y = FoodChoose.foodLocation[length][0], FoodChoose.foodLocation[length][1]
                    food.setPos(x, y)
                    food.pos = length
                    self.addItem(food)
                    length += len(FoodChoose.foodLocation) // len(self.foodList)

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.foodList)):
                    if self.foodList[i].game_update(self.bullets):
                        break
                
                

        elif self.screen == "WesternFood":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("DarkBlue")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodList = []
                # wholeFoodDic = {'koreanFoodDic': koreanFoodDic}
                # koreanFoodDic = {'bibimbab': bibimbab}
                # bibimbab = {'image': , :, :}
                # each == bibimbab
                for key, value in WholeFood.wholeFoodDic[self.screen].items():
                    food = FoodChoose(value['image'], key, self)
                    self.foodList.append(food)
                    food = None

                
                length = 0
                for food in self.foodList:
                    x, y = FoodChoose.foodLocation[length][0], FoodChoose.foodLocation[length][1]
                    food.setPos(x, y)
                    food.pos = length
                    self.addItem(food)
                    length += len(FoodChoose.foodLocation) // len(self.foodList)

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.foodList)):
                    if self.foodList[i].game_update(self.bullets):
                        break

        elif self.screen == "AllFood":
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("DarkBlue")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodList = []
                # wholeFoodDic = {'koreanFoodDic': koreanFoodDic}
                # koreanFoodDic = {'bibimbab': bibimbab}
                # bibimbab = {'image': , :, :}
                # each == bibimbab
                for each in WholeFood.wholeFoodDic.values():    
                    for key, value in each.items():
                        food = FoodChoose(value['image'], key, self)
                        self.foodList.append(food)
                        food = None
                
                length = 0
                for food in self.foodList:
                    x, y = FoodChoose.foodLocation[length][0], FoodChoose.foodLocation[length][1]
                    food.setPos(x, y)
                    food.pos = length
                    self.addItem(food)
                    length += len(FoodChoose.foodLocation) // len(self.foodList)

                # BackButton
                self.backButton = BackButton(self)
                self.backButton.setPos(10, 20)
                self.addItem(self.backButton)
                self.isAllFood     = True
                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.foodList)):
                    if self.foodList[i].game_update(self.bullets):
                        break

        elif self.screen in WholeFood.wholeFoodList:
            if not self.isInitialized:
                # BackGround
                self.bg = BackGround("Purple")
                self.addItem(self.bg)


                # Player
                self.player = Player()
                self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2, 500)
                self.addItem(self.player)


                # Bullets
                self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y),
                                Bullet(PLAYER_BULLET_X_OFFSETS[1],PLAYER_BULLET_Y - 30),
                                Bullet(PLAYER_BULLET_X_OFFSETS[2],PLAYER_BULLET_Y)]
                for b in self.bullets:
                    b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.addItem(b)
                
                self.foodImage = FoodInfo(self.foodImagePath, self)
                self.foodImage.setPos(100, 100)
                self.addItem(self.foodImage)

                self.homeButton = Home(self)
                self.homeButton.setPos(200-self.homeButton.pixmap().width()//2, 300)
                self.addItem(self.homeButton)

                self.retryButton = Retry(self)
                self.retryButton.setPos(400-self.retryButton.pixmap().width()//2, 300)
                self.addItem(self.retryButton)
                
                self.openUrlButton = OpenURL(self)
                self.openUrlButton.setPos(600-self.openUrlButton.pixmap().width()//2, 300)
                self.addItem(self.openUrlButton)

                self.isInitialized = True

            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.homeButton.game_update(self.bullets):
                    return

                elif self.retryButton.game_update(self.bullets, self.isAllFood):
                    return

                elif self.openUrlButton.game_update(self.bullets):
                    return
                

        elif self.screen == "CustomizeScreen":
            if not self.isInitialized:
                if not self.initUI:
                    self.customize.cancel = False
                    self.customize.initUI()
                    self.initUI = True

                else:
                    if len(self.customizeDic) != 0:
                        self.bg = BackGround("DarkBlue")
                        self.addItem(self.bg)

                        # Player
                        self.player = Player()
                        self.player.setPos((SCREEN_WIDTH - self.player.pixmap().width()) / 2, 500)
                        self.addItem(self.player)

                        # Bullets
                        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y),
                                        Bullet(PLAYER_BULLET_X_OFFSETS[1], PLAYER_BULLET_Y - 30),
                                        Bullet(PLAYER_BULLET_X_OFFSETS[2], PLAYER_BULLET_Y)]
                        for b in self.bullets:
                            b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
                            self.addItem(b)

                        self.selectList = []
                        for value in self.customizeDic.values():
                            select = Customize(value['image'], value['text'], self)
                            self.selectList.append(select)
                            select = None

                        length = 0
                        for select in self.selectList:
                            x, y = Customize.selectLocation[length][0], Customize.selectLocation[length][1]
                            select.setPos(x, y)
                            select.pos = length
                            self.addItem(select)
                            length += len(Customize.selectLocation) // len(self.selectList)


                        # BackButton
                        self.backButton = BackButton(self)
                        self.backButton.setPos(10, 20)
                        self.addItem(self.backButton)

                        self.isInitialized = True


                    else:
                        if self.customize.cancel:
                            self.screen = 'InitialScreen'
                            self.isInitialized = False
                            self.clear()


            else:
                self.player.game_update(self.keys_pressed)
                for b in self.bullets:
                    b.game_update(self.keys_pressed, self.player)

                if self.backButton.game_update(self.bullets):
                    return

                for i in range(len(self.selectList)):
                    if self.selectList[i].game_update(self.bullets):
                        print(self.selectList[i].select, self.selectList[i].imagePath)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())