# -*- coding: utf-8 -*- 

#import pymongo
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as pr
import os, sys
from bs4 import BeautifulSoup
import re

#connection = pymongo.MongoClient("localhost")
#db = connection.STOREDB
#collection = db.uniqlo

#men category crawling

#starting url
baseurl = "http://www.uniqlo.kr/display/displayShop.lecs?storeNo=22&siteNo=9&displayMallNo=UQ1&displayNo=UQ1A02A01A15#UQ1A02A01A15A02"
res = req.urlopen(baseurl)
print(res)
#navHeader > li.active > div > div.gnb_2016_col.col3
#root dir
rootDir = os.path.join(os.getcwd(), 'uniqlo')

soup = BeautifulSoup(res, "html.parser")

#첫 페이지에서 -> men category
a_list = soup.select("div.gnb_2016_col.col3 > div.col_block > ul a")

#print(a_list)
for a in a_list:
    print("ㅇㅇ: " + a.string + a.get('href')+ '\n')
    #찾은 카테고리명으로 디렉토리 생성
    dirname = os.path.join(rootDir, a.string)
    if not(os.path.isdir(dirname)):
        os.mkdir(dirname)
    #해당 카테고리 페이지로 이동
    url = pr.urljoin(baseurl, a.get('href'))

    res2 = req.urlopen(url)
    soup2 = BeautifulSoup(res2, "html.parser")
    #img, price
    item_list = soup2.select("ul.uniqlo_info > li.item")
    img_list = soup2.select("ul.uniqlo_info > li.item div.thumb > p > a > img")
    price_list = soup2.select("ul.uniqlo_info > li.item strong")
    #content1 > div:nth-child(3) > div > ul > li:nth-child(1) > p > span > a
    #size_list = soup2.select("ul.uniqlo_info > li.item > div.color_chip > span")
    #print("\nimg: " + str(len(img_list)) + "\nprice: " + str(len(price_list)))
    
    price = re.split(',|원',item_list[1].select_one("strong.price").string)
    price = int(price[0] + price[1])
    #price = price[0]
    coloritem = item_list[1].select("ul.info_color")
    for ic in coloritem:
        url = ic.select_one("li > a").get('data-image-path')
        color = ic.select_one("li > a > img").get('alt').split(' ')
        color = color[len(color)-1]
        print("hihi:", url,color)
    #navHeader > li.active > div > div.gnb_2016_col.col3 > div:nth-child(1)

    print("\nstrong: ", price)

    for i in range( len(img_list)):
        img_name = img_list[i].get('alt')
        img_price = price_list[i].string
        img_url = img_list[i].get('src')
        img_size = "XS-XL"
        
        #print(img_name, img_price, img_url, img_size)
        #req.urlretrieve(img_list[i].get('src'), dirname +'/'+img_name +'.jpg')
        #print("     " + img_list[i].get('alt') + img_list[i].get('src'))
        '''
        collection.insert({"name": img_name,
                           "price": img_price,
                           "url": img_url,
                           "size": img_size,
                           "color": img_color,
                           "shape": img_shape
                           })
        print("insert in DB\n")
        '''
        
