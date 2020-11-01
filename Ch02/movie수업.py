"""
날짜 : 2020/07/16
이름 : 이성진
내용 : 파이썬 네이버 영화 리뷰평점 데이터 수집하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime
from pymongo import MongoClient as mongo
import time, logging

#로거 생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

#로그 포맷 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#핸들러 생성
fileHandler = logging.FileHandler('./movie.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

#로거 + 핸들러 연결
logger.addHandler(fileHandler)

#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#browser = webdriver.Chrome('../Ch01/chromedriver.exe', chrome_options=chrome_options)
browser = webdriver.Chrome('../Ch01/chromedriver.exe')
browser.implicitly_wait(3)
logger.info('클롬 가상브라우저 실행 완료')

# 랭크 페이지 번호 변수 선언
page = 1

while True:
    
    logger.info('첫번째 while 시작')
    # 랭크 변수 선언(0~49)
    i = 0
    time.sleep(1)


    while True:
        
        logger.info('두번째 while 시작')
        #네이버 영화 랭킹 평점순 이동
        browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200720&page='+str(page))
        browser.implicitly_wait(3)
        logger.info('네이버 영화 랭킹 평점순 이동 page=%d' % page)
        
        try:
            #영화 랭킹 클릭
            ranks = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
            ranks[i].click()
            browser.implicitly_wait(3)
            logger.info('영화 랭킹 클릭')

        except:
            logger.warning('두번째 while try 예외발생')
            break

        #영화 평점 탭 클릭
        review_tab = browser.find_element_by_css_selector('#movieEndTabMenu > li > a.tab05')
        review_tab.click()
        browser.implicitly_wait(3)
        logger.info('영화 평점 탭 클릭')

        #영화제목 수집
        tit_tag = browser.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
        href = tit_tag.get_attribute('href')
        i = href.rfind('=')+1

        code = href[i:]
        title = tit_tag.text
        logger.info('영화 제목 : %s' % title)

        # 평점, 리뷰, 날짜 수집을 위해 현재 브라우저를 iframe 페이지로 전환
        browser.switch_to.frame('pointAfterListIframe')
        browser.implicitly_wait(3)
        logger.info('iframe 전환')

        # 최신순 클릭
        tag_latest_a = browser.find_element_by_css_selector('#orderCheckbox > ul.sorting_list > li:nth-child(2) > a')
        tag_latest_a.click()
        browser.implicitly_wait(3)
        logger.info('최신순 클릭')

        # MongoDB 접속, DB선택, Collection 선택
        conn = mongo('mongodb://lsj:1234@192.168.50.82:27017/lsj')
        db = conn.get_database('lsj')
        collection = db.get_collection('movies')

        # 현재 페이지 설정
        page_num = 1


        while True:

            try:
                # page 클릭
                page_id = 'pagerTagAnchor'+str(page_num)
                page_btn = browser.find_element_by_id(page_id)
                page_btn.click()
                browser.implicitly_wait(3)
                logger.info('현재 페이지 : %d ' % page_num)

            except:
                logger.info('클릭할 페이지 없음')
                break

            # 평점, 리뷰, 날짜 수집
            li_tags = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')
            list_data = []

            for li in li_tags:
                score = li.find_element_by_css_selector('.star_score > em')
                reple = li.find_element_by_css_selector('.score_reple > p > span:last-child')
                rdate = li.find_element_by_css_selector('.score_reple > dl > dt > em:nth-child(2)')

                list_data.append({'title': title,
                                  'code': code,
                                  'score': score.text,
                                  'reple': reple.text,
                                  'rdate': rdate.text})

            #Insert 실행
            collection.insert_many(list_data)


            print(page_num, '페이지 insert 완료.')
            page_num += 1

        # 그 다음 영화 리뷰 수집을 위한 랭크 변수 증가
        i += 1

    page += 1

print('종료...')

#브라우저 종료
browser.close()
browser.quit()


"""
#디렉터리 생성
dir = "/home/bigdata/naver/naver-{:%y-%m-%d}".format(datetime.now())
if not os.path.exists(dir):
	os.makedirs(dir)
#파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')
file.write('순위,제목,날짜\n')
for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('[%s],' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % "{:%y%m%d%H%M%S}".format(datetime.now()))
#파일닫기
file.close()
"""