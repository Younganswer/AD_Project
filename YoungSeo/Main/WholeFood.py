wholeFoodDic    = {}
koreanFoodDic   = {}
chineseFoodDic  = {}
japaneseFoodDic = {}
westernFoodDic  = {}

# KoreanFood
bibimbab = {"image": "PNG/Korean_Food/bibimbab.png", "foodInfo": "bibimbab infomation", "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=12672126&memberNo=32920277"}
soju     = {"image": "PNG/Korean_Food/soju.png",     "foodInfo": "soju infomation",     "URL": "https://www.beer2day.com/2416"}
tukkochi = {"image": "PNG/Korean_Food/tukkochi.png", "foodInfo": "tukkochi infomation", "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=10627954&memberNo=32920277"}
ramen    = {"image": "PNG/Korean_Food/ramen.png",    "foodInfo": "ramen infomation",    "URL": "https://www.google.com/search?q=%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD&oq=%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD&aqs=chrome..69i57j0l7.1454j0j7&sourceid=chrome&ie=UTF-8&sxsrf=ACYBGNQOC8vQLo3xKI6qDt-ESxLep2UwSw:1576473953784&npsic=0&rflfq=1&rlha=0&rllag=37619063,127017538,1029&tbm=lcl&rldimm=16823392031548916546&lqi=CgzquYDrsKXsspzqta1aHgoN6rmA67ClIOyynOq1rSIN6rmA67ClIOyynOq1rQ&ved=2ahUKEwiC74yQt7nmAhUUzmEKHTwCA20QvS4wAHoECAsQIA&rldoc=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9&rlst=f#rlfi=hd:;si:16823392031548916546,l,CgzquYDrsKXsspzqta1aHgoN6rmA67ClIOyynOq1rSIN6rmA67ClIOyynOq1rQ;mv:[[37.660768,127.06367829999999],[37.560155,126.9681583]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9"}

koreanFoodDic["bibimbab"] = bibimbab
koreanFoodDic["soju"]     = soju
koreanFoodDic["tukkochi"] = tukkochi
koreanFoodDic["ramen"]    = ramen

# ChineseFood
tanghulu = {"image": "PNG/Chinese_Food/tanghulu", "foodInfo": "tanghulu infomation", "URL": "http://blog.naver.com/PostView.nhn?blogId=jsh4682239&logNo=221443386744&categoryNo=1&parentCategoryNo=0"}
baozi =    {"image": "PNG/Chinese_Food/baozi",    "foodInfo": "baozi infomation",    "URL": "https://m.blog.naver.com/leejipot/221286391162"}
noodles =  {"image": "PNG/Chinese_Food/noodles",  "foodInfo": "noodles infomation",  "URL": "https://redcolorworld.tistory.com/152"}
tea =      {"image": "PNG/Chinese_Food/tea",      "foodInfo": "tea infomation",      "URL": "https://www.diningcode.com/list.php?query=%EC%8B%A0%EC%B4%8C%20%20%EC%A4%91%EA%B5%AD%EC%B0%A8"}

chineseFoodDic["tanghulu"] = tanghulu
chineseFoodDic["baozi"]    = baozi
chineseFoodDic["noodles"]  = noodles
chineseFoodDic["tea"]      = tea

# JapaneseFood
sushi    = {"image": "PNG/Japanese_Food/sushi",    "foodInfo": "sushi infomation",    "URL": "https://m.blog.naver.com/PostView.nhn?blogId=rah210&logNo=221331340647&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
tempura  = {"image": "PNG/Japanese_Food/tempura",  "foodInfo": "tempura infomation",  "URL": "https://m.blog.naver.com/PostView.nhn?blogId=ceron2&logNo=221480036008&categoryNo=44&proxyReferer=&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
takoyaki = {"image": "PNG/Japanese_Food/takoyaki", "foodInfo": "takoyaki infomation", "URL": "https://www.mangoplate.com/search/%ED%83%80%EC%BD%94%EC%95%BC%EB%81%BC"}
yakitori = {"image": "PNG/Japanese_Food/yakitori", "foodInfo": "yakitori infomation", "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=7592072&memberNo=32920277"}

japaneseFoodDic["sushi"]    = sushi
japaneseFoodDic["tempura"]  = tempura
japaneseFoodDic["takoyaki"] = takoyaki
japaneseFoodDic["yakitori"] = yakitori

# WesternFood
pizza     = {"image": "PNG/Western_Food/pizza.png",     "foodInfo": "pizza infomation",     "URL": "https://www.pji.co.kr/?gclid=Cj0KCQiA0NfvBRCVARIsAO4930mCwpKj11WpdTyOELJP1_bd2rs_MH-_QKVsVAwW7vdhsFLCidoI2uMaAr3ZEALw_wcB"}
spaghetti = {"image": "PNG/Western_Food/spaghetti.png", "foodInfo": "spaghetti infomation", "URL": "https://m.blog.naver.com/PostView.nhn?blogId=yeun12134&logNo=220596803333&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
steak     = {"image": "PNG/Western_Food/steak.png",     "foodInfo": "steak infomation",     "URL": "https://www.outback.co.kr/"}
burger    = {"image": "PNG/Western_Food/burger.png",    "foodInfo": "burger infomation",    "URL": "https://minimom08tech.tistory.com/342"}

westernFoodDic["pizza"]     = pizza
westernFoodDic["spaghetti"] = spaghetti
westernFoodDic["steak"]     = steak
westernFoodDic["burger"]    = burger

wholeFoodDic["KoreanFood"]   = koreanFoodDic
wholeFoodDic["ChineseFood"]  = chineseFoodDic
wholeFoodDic["JapaneseFood"] = japaneseFoodDic
wholeFoodDic["WesternFood"]  = westernFoodDic

wholeFoodList = []
for value in wholeFoodDic.values():
    for key in value.keys():
        wholeFoodList.append(key)

if __name__ == '__main__':
    print(wholeFoodList)