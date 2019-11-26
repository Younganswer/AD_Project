import random
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsPixmapItem


path = 'C:/Users/dudtj/iCloudDrive/vscode_workspace/Python_workspace/Github/AD_Project/YoungSeo/'

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
ENEMY_SPONE_X           = 800
ENEMY_SPONE_Y           = 600
ENEMY_FRAMES            = 500


# 음식 설정 클래스
class FoodInfo(QGraphicsPixmapItem):

    wholeFoodDic    = {}
    koreanFoodDic   = {}
    chineseFoodDic  = {}
    japaneseFoodDic = {}
    westernFoodDic  = {}

    # Korean   Food
    bibimbab = {"image": "bibimbab image", "foodInfo": "bibimbab infomation", "URL": "bibimbab URL"}
    # Chinese  Food
    mara =  {"image": "mara image", "foodInfo": "mara infomation", "URL": "mara URL"}
    # Japanese Food
    sushi = {"image": "sushi image", "foodInfo": "sushi infomation", "URL": "sushi URL"}
    # Western  Food
    pizza = {"image": "pizza image", "foodInfo": "pizza infomation", "URL": "pizza URL"}

    koreanFoodDic["bibimbab"] = bibimbab
    chineseFoodDic["mara"]    = mara
    japaneseFoodDic["sushi"]  = sushi
    westernFoodDic["pizza"]   = pizza

    wholeFoodDic["koreanFood"]   = koreanFoodDic
    wholeFoodDic["chineseFood"]  = chineseFoodDic
    wholeFoodDic["japaneseFood"] = japaneseFoodDic
    wholeFoodDic["westernFood"]  = westernFoodDic

    sound = QSound(path+'Bonus/sfx_retro_spaceship_explosion.wav')
                          
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def game_update(self, enemies, idx, bullets):
        return