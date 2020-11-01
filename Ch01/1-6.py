"""
날짜 : 2020/07/13
이름 : 이성진
내용 : 네이버 실시간 검색어 출력하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

#크롬 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#네이버 데이터랩 메인 이동
browser.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

#네이버 실검 1~10위 파싱
item_boxs = browser.find_elements_by_css_selector('#content > div > .selection_area > .selection_content > .field_list > div > div > ul:nth-child(1) > li > .item_box')



#파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(fname, mode='w', encoding='utf8')

now = "{:%y%m%d%H%M%S}".format(datetime.now())

file.write('순위,제목,날짜 \n')
for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('[%s],' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % now)

#파일닫기
file.close()



"""
html = req.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
dom = bs(html.text, 'html.parser')

print(dom)

keywords = dom.select('#content > div > .selection_area > .selection_content > .field_list > div > div > ul:nth-of-type(1) > li > .item_box')

#출력
print(keywords)
"""