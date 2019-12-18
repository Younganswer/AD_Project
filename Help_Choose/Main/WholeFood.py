wholeFoodDic    = {}
koreanFoodDic   = {}
chineseFoodDic  = {}
japaneseFoodDic = {}
westernFoodDic  = {}

# KoreanFood
bibimbab = {"image": "PNG/Korean_Food/bibimbab.png", "foodInfo": "밥에 고기나 나물 등을 넣고\n양념과 함께 비벼먹는 음식\n구수한 된장찌개와 함께 비벼먹는다면\n그 맛은 이루 말할 필요가 없다",      "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=12672126&memberNo=32920277"}
soju     = {"image": "PNG/Korean_Food/soju.png",     "foodInfo": "한국의 대표적인 쌀 증류주\n하지만 요즘은 희석식 소주가 더 많다\n홍합탕과의 조합은 일품\n아래의 URL은 링겔주를 다루고있다",       "URL": "https://www.beer2day.com/2416"}
tukkochi = {"image": "PNG/Korean_Food/tukkochi.png", "foodInfo": "남녀노소 한국인 대표 인기간식\n입이 심심할 때 먹기 최고이다\n우리의 추억을 불러일으키는 이 맛은\n우리의 지갑을 열기에 충분하다", "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=10627954&memberNo=32920277"}
ramen    = {"image": "PNG/Korean_Food/ramen.png",    "foodInfo": "한국의 전통음식\n피시방에서 게임하는 아이들부터\n어른들의 술자리 안주까지\n한국인의 젓가락을 움직이는 음식 1위",                    "URL": "https://www.google.com/search?q=%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD&oq=%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD&aqs=chrome..69i57j0l7.1454j0j7&sourceid=chrome&ie=UTF-8&sxsrf=ACYBGNQOC8vQLo3xKI6qDt-ESxLep2UwSw:1576473953784&npsic=0&rflfq=1&rlha=0&rllag=37619063,127017538,1029&tbm=lcl&rldimm=16823392031548916546&lqi=CgzquYDrsKXsspzqta1aHgoN6rmA67ClIOyynOq1rSIN6rmA67ClIOyynOq1rQ&ved=2ahUKEwiC74yQt7nmAhUUzmEKHTwCA20QvS4wAHoECAsQIA&rldoc=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9&rlst=f#rlfi=hd:;si:16823392031548916546,l,CgzquYDrsKXsspzqta1aHgoN6rmA67ClIOyynOq1rSIN6rmA67ClIOyynOq1rQ;mv:[[37.660768,127.06367829999999],[37.560155,126.9681583]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9"}

koreanFoodDic["bibimbab"] = bibimbab
koreanFoodDic["soju"]     = soju
koreanFoodDic["tukkochi"] = tukkochi
koreanFoodDic["ramen"]    = ramen

# ChineseFood
tanghulu = {"image": "PNG/Chinese_Food/tanghulu", "foodInfo": "단걸 먹고 싶을 때 이것 만한게 없다\n입안에서 부숴지는 담백한 설탕코팅과\n그 속에 숨어있는 달콤한 과육\n이 맛을 한번만 먹고서는 못배긴다",                        "URL": "http://blog.naver.com/PostView.nhn?blogId=jsh4682239&logNo=221443386744&categoryNo=1&parentCategoryNo=0"}
baozi =    {"image": "PNG/Chinese_Food/baozi",    "foodInfo": "속이 꽉 차있는 중국식 만두\n바오쯔의 한 종류로 샤오룽바오가 있다\n최근 마라탕과 함께 급 부상한 바오쯔\n이 깊은 육즙을 맛보길 추천한다",                          "URL": "https://m.blog.naver.com/leejipot/221286391162"}
noodles =  {"image": "PNG/Chinese_Food/noodles",  "foodInfo": "땅콩 기름에 고춧가루, 마늘 등을 볶고\n국수에 얹은 다음 돼지고기와 파 등\n고명을 얹어 비벼 먹는 음식\n무거운 육수의 목넘김을 느껴보아라",                         "URL": "https://redcolorworld.tistory.com/152"}
tea =      {"image": "PNG/Chinese_Food/tea",      "foodInfo": "중국의 역사에 함게 살아숨쉰\n중국의 차는 깊은 역사만큼\n그 속에 깊은 맛을 가졌다\n몸뿐아니라 마음까지 따듯하게 해주는 차\n당신도 그 온기를 느껴보길 바란다",      "URL": "https://www.diningcode.com/list.php?query=%EC%8B%A0%EC%B4%8C%20%20%EC%A4%91%EA%B5%AD%EC%B0%A8"}

chineseFoodDic["tanghulu"] = tanghulu
chineseFoodDic["baozi"]    = baozi
chineseFoodDic["noodles"]  = noodles
chineseFoodDic["tea"]      = tea

# JapaneseFood
sushi    = {"image": "PNG/Japanese_Food/sushi",    "foodInfo": "단촛물으로 감칠맛을 높인 밥\n밥위에 얹어진 기름이 그득한 회 한점\n입안을 가득 채우는 부드러움\n이번 겨울 스시를 먹어보는건 어떤가", "URL": "https://m.blog.naver.com/PostView.nhn?blogId=rah210&logNo=221331340647&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
tempura  = {"image": "PNG/Japanese_Food/tempura",  "foodInfo": "일반적인 튀김옷 보다 가볍다\n그 가벼움이 입안 가득 바삭거린다\n남녀노소 즐길 수 있는 일본식 튀김\n그 바삭함의 늪에 빠져보자",       "URL": "https://m.blog.naver.com/PostView.nhn?blogId=ceron2&logNo=221480036008&categoryNo=44&proxyReferer=&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
takoyaki = {"image": "PNG/Japanese_Food/takoyaki", "foodInfo": "밀가루 반죽에 잘게 썬 문어와\n파, 양배추 등을 넣어 동그랗게 구워내\n가쓰오부시와 소스를 뿌려먹는\n일본의 대표 먹거리 그 맛은 일품", "URL": "https://www.mangoplate.com/search/%ED%83%80%EC%BD%94%EC%95%BC%EB%81%BC"}
yakitori = {"image": "PNG/Japanese_Food/yakitori", "foodInfo": "길거리에서 사먹는 그 맛부터\n술 안주로 먹는 그 맛까지\n닭꼬치의 다양한 그 맛을\n이번 겨울 느껴보는 것은 어떤가",                   "URL": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=7592072&memberNo=32920277"}

japaneseFoodDic["sushi"]    = sushi
japaneseFoodDic["tempura"]  = tempura
japaneseFoodDic["takoyaki"] = takoyaki
japaneseFoodDic["yakitori"] = yakitori

# WesternFood
pizza     = {"image": "PNG/Western_Food/pizza.png",     "foodInfo": "PPL은 아니지만 필자는 개인적으로\n파파존스 피자를 좋아한다\n입안가득 퍼지는 고기의 깊은 육즙\n파파존스 올미트 피자, 어떠한가",     "URL": "https://www.pji.co.kr/?gclid=Cj0KCQiA0NfvBRCVARIsAO4930mCwpKj11WpdTyOELJP1_bd2rs_MH-_QKVsVAwW7vdhsFLCidoI2uMaAr3ZEALw_wcB"}
spaghetti = {"image": "PNG/Western_Food/spaghetti.png", "foodInfo": "국민대 최고의 아웃풋 델리버스\n한끼 든든한 빠네크림파스타\n그릴드치킨파스타, 크림리조또\n복지관 1층 델리버스를 추천한다", "URL": "https://m.blog.naver.com/PostView.nhn?blogId=yeun12134&logNo=220596803333&proxyReferer=https%3A%2F%2Fwww.google.com%2F"}
steak     = {"image": "PNG/Western_Food/steak.png",     "foodInfo": "고급 음식으로서 우리 인식에\n자리매김 하고있는 스테이크\n등심, 안심등의 다양한 부위를\n즐길 수 있는 그 매력에 빠져보자",     "URL": "https://www.outback.co.kr/"}
burger    = {"image": "PNG/Western_Food/burger.png",    "foodInfo": "참깨빵 위에 순쇠고기 패티 두 장\n특별한 소스 양상추\n치즈, 피클, 양파까아지\n뜨근하고 든든한 햄버거!",    "URL": "https://minimom08tech.tistory.com/342"}

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