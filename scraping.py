# import requests
# from bs4 import BeautifulSoup

# url = "https://www.sejuku.net/blog/"

# response = requests.get(url)
# response.encoding = response.apparent_encoding

# bs = BeautifulSoup(response.text, 'html.parser')

# for i in bs.select("h3"):
#     print(i.getText())

# coding: UTF-8

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.fujitv.co.jp/meza/uranai/index.html"

# # WEBサイトからHTMLデータを取得
# response = requests.get(url)

# if response.status_code == 200:
#     # BeautifulSoupオブジェクトを作成
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # タイトルを取得して表示
#     title = soup.title.text.strip()
#     print("タイトル:", title)
    
#     # 本文の一部を表示
#     content = soup.find('div', class_='section-inner').text.strip()
#     print("本文:", content)
# else:
#     print("WEBサイトにアクセスできませんでした。")
import requests
from bs4 import BeautifulSoup

url = "https://www.fujitv.co.jp/meza/uranai/index.html"

# WEBサイトからHTMLデータを取得
response = requests.get(url)

if response.status_code == 200:
    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # タイトルを取得して表示
    title = soup.title.text.strip()
    print("タイトル:", title)
    
    # class="result1"の中身を取得して表示
    result1_element = soup.find('div', class_='result1')
    if result1_element:
        result1_content = result1_element.text.strip()
        print("class=\"result1\"の中身:", result1_content)
    else:
        print("class=\"result1\"の要素が見つかりませんでした。")
else:
    print("WEBサイトにアクセスできませんでした。")