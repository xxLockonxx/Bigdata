"""
날짜 : 2020/07/13
이름 : 이성진
내용 : 파이썬 HTML 파싱하기
"""
from bs4 import BeautifulSoup as bs
import urllib.request as req

html = req.urlopen('http://chhak.kr/py/test1.html').read().decode('UTF-8')
#print(html)

#HTML 파싱
dom = bs(html, 'html.parser')
items = dom.select('ul > li')
result = dom.select_one('#list > .apple').string

#출력
print('items :', items)
print('result : ', result)