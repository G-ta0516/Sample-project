import requests
from bs4 import BeautifulSoup

# スクレイピング対象の URL にリクエストを送り HTML を取得する
# LINE占い
resLINE = requests.get('https://fortune.line.me/contents/horoscope/')
# Dmenu占い
# resDmenu = requests.get('https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_ranking.html')
# 占いの泉
resIzumi = requests.get('https://izumi.uranai.jp/unsei')
# 家庭画報
res家庭画報 = requests.get('https://www.kateigaho.com/horoscope/')
# Rsk
resRsk = requests.get('https://www.rsk.co.jp/horoscope/')
# ハルメク365
resハルメク365 = requests.get('https://halmek.co.jp/culture/c/psychology/daily')
# 朝日新聞占い
res朝日新聞 = requests.Session().get('https://www.asahi.com/uranai/12seiza/')
res朝日新聞.encoding = res朝日新聞.apparent_encoding


# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soupLINE = BeautifulSoup(resLINE.text, 'html.parser')
# soupDmenu = BeautifulSoup(resDmenu.text, 'html.parser')
soupIzumi = BeautifulSoup(resIzumi.text, 'html.parser')
soup家庭画報 = BeautifulSoup(res家庭画報.text, 'html.parser')
soupRsk = BeautifulSoup(resRsk.text, 'html.parser')
soupハルメク365 = BeautifulSoup(resハルメク365.text, 'html.parser')
soup朝日新聞 = BeautifulSoup(res朝日新聞.text, 'html.parser')

#タグの文字列を取得する
txtConstellationLINE = soupLINE.find(class_='zodiac-item_name__c4Ypu')
txtDetailLINE = soupLINE.find(class_='zodiac-item_summary__E_Vh7')
# txtConstellationDmenu = soupDmenu.find(class_='postRank__infoHead')
# txtDetailDmenu = soupDmenu.find(class_='postRank__infoFoot')
txtConstellationIzumi = soupIzumi.find(class_='topSeizaName')
txtDetailIzumi = soupIzumi.find(class_='seizaRstTxt')
txtConstellation家庭画報 = soup家庭画報.find(class_='horoscope_name font_min')
txtDetail家庭画報 = soup家庭画報.find(class_='horoscope_txt font_hk')
txtConstellationRsk = soupRsk.find(class_='uranai_seiza')
txtDetailRsk = soupRsk.find(class_='uranai_desc')
txtConstellationハルメク365 = soupハルメク365.find(class_='sign-name')
txtDetailハルメク365 = soupハルメク365.find(class_='text')
txtConstellation朝日新聞 = soup朝日新聞.find(href='/uranai/12seiza/sagittarius.html')

# print
print(txtConstellationLINE)
print(txtDetailLINE)
# print(txtConstellationDmenu)
# print(txtDetailDmenu)
print(txtConstellationIzumi)
print(txtDetailIzumi)
print(txtConstellation家庭画報)
print(txtDetail家庭画報)
print(txtConstellationRsk)
print(txtDetailRsk)
print(txtConstellationハルメク365)
print(txtDetailハルメク365)
print(txtConstellation朝日新聞)
