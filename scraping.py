import requests
from bs4 import BeautifulSoup


def GetURANAi(URL,Constellation,Detail):
    # 占いサイトのURL
    resURL = requests.get(URL)
    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soupURL = BeautifulSoup(resURL.text, 'html.parser')
    #タグの文字列を取得する
    txtConstellation = soupURL.find(class_=Constellation)
    txtDetail = soupURL.find(class_=Detail)

    # print SQLに入れたい
    print(txtConstellation)
    print(txtDetail)

# GetURANAi('https://fortune.line.me/contents/horoscope/','zodiac-item_name__c4Ypu','zodiac-item_summary__E_Vh7')

URLList = [
    # LINE
    ['https://fortune.line.me/contents/horoscope/','zodiac-item_name__c4Ypu','zodiac-item_summary__E_Vh7']
    # 占いの泉
    ,['https://izumi.uranai.jp/unsei','topSeizaName','seizaRstTxt']
    # 家庭画報
    ,['https://www.kateigaho.com/horoscope/','horoscope_name font_min','horoscope_txt font_hk']
    # Rsk
    ,['https://www.rsk.co.jp/horoscope/','uranai_seiza','uranai_desc']
    # ハルメク365
    ,['https://halmek.co.jp/culture/c/psychology/daily','text','/uranai/12seiza/sagittarius.html']
    ]

# print(URLList[0])

# GetURANAi('https://fortune.line.me/contents/horoscope/','zodiac-item_name__c4Ypu','zodiac-item_summary__E_Vh7')
GetURANAi(*URLList[0])

# for num in URLList(5):
#     GetURANAi(*URLList[num])

for num in range(len(URLList)):
    GetURANAi(*URLList[num])


# # 朝日新聞占い
# res朝日新聞 = requests.Session().get('https://www.asahi.com/uranai/12seiza/')
# res朝日新聞.encoding = res朝日新聞.apparent_encoding

# soup朝日新聞 = BeautifulSoup(res朝日新聞.text, 'html.parser')
