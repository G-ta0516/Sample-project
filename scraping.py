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
   
    [
    # RSK山陽放送
    ['https://www.sumo.or.jp/Fortune','uranai_rank ribbon-number1','uranai_desc']
    # RSK山陽放送
    ,['https://www.rsk.co.jp/horoscope/','uranai_rank ribbon-number1','uranai_desc']
    # RSK山陽放送
    ,['https://www.rsk.co.jp/horoscope/','uranai_rank ribbon-number1','uranai_desc']
    # リンネル
    ,['https://liniere.jp/column/lifestyle/36333/','p-article-post-col-data__title','p-article-post-col-data__text']
    # テレ朝
    ,['https://www.tv-asahi.co.jp/goodmorning/uranai/','seiza-ttl','read-area']
    # Ameba
    ,['https://amb-uranai.ameba.jp/fortune/zodiac/','nonmemberZodiacList__name','nonmemberZodiacList__message']
    # LINE
    ,['https://fortune.line.me/contents/horoscope/','zodiac-item_name__c4Ypu','zodiac-item_summary__E_Vh7']
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
# GetURANAi(*URLList[0])

# for num in URLList(5):
#     GetURANAi(*URLList[num])

for num in range(len(URLList)):
    GetURANAi(*URLList[num])


# # 朝日新聞占い
# res朝日新聞 = requests.Session().get('https://www.asahi.com/uranai/12seiza/')
# res朝日新聞.encoding = res朝日新聞.apparent_encoding

# soup朝日新聞 = BeautifulSoup(res朝日新聞.text, 'html.parser')
