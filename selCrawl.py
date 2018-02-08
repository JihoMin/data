from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo
import time

# chrome webdriver dir
driver = webdriver.Chrome('/Users/minjiho/crawler/chromedriver')

driver.implicitly_wait(5)

# url access
driver.get('http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1711333016')

# click paging buttons below clothes contents
buttons = driver.find_elements_by_css_selector('#page_idx > span > a')

for i in range(len(buttons)):
    
    b = driver.find_elements_by_css_selector('#page_idx > span > a')
    b[i].click()
    time.sleep(5)
    
    # passing page source to beautifulsoup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select('div.cont > span.prod_nm')
    #goodsList > ul:nth-child(1) > li:nth-child(1) > a > div.cont > span.prod_nm
    #goodsList > ul:nth-child(1) > li:nth-child(1) > a > div.cont > span.prod_nm
    print(names[0].string)

'''
find_element_by_name(‘HTML_name’)
find_element_by_id(‘HTML_id’)
find_element_by_xpath(‘/html/body/some/xpath

find_element_by_css_selector(‘#css > div.selector’)
find_element_by_class_name(‘some_class_name’)
find_element_by_tag_name(‘h1’)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
'''

