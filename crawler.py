import urllib
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
# 검색할 이미지의 키워드 입력
keyword = input("검색할 이미지를 입력하세요 : ")
url = 'https://www.google.co.kr/search?q=sweatshirt&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjl_YeYifLYAhULmZQKHe3LCSwQ_AUICigB&biw=783&bih=699'
# html 소스 가져오기
text = requests.get(url, headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}).text


# html 문서로 파싱
text_source = StringIO(text)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음(20개만 크롤링 됨.. 이유 찾아봐야 됨)
imgs = doc.findall('.//img')

img_list = []   # 이미지 경로가 담길 list
i = 0
#print(imgs[1].get('src'))
#urllib.request.urlretrieve(imgs[1].get('src'), "1.jpg")

for a in imgs:
    if i <= 20:
        i = i + 1
        continue
    else:
        img_list.append(a.get('data-src'))   
        print(a.get('data-src'))
        full_name = keyword + str(i) + ".jpg"
        i = i + 1
        urllib.request.urlretrieve(str(a.get('data-src')), full_name)
