"""
날짜 : 2020/07/15
이름 : 이성진
내용 : 기상청 날씨 크롤링하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

#세션시작
sess = req.session()

#날씨 데이터 요청
html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

#파싱 후 포인트 출력
dom = bs(html.text, 'html.parser')

locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temperatures = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
dewpointtemps = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
sensibletemps = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
percipitations = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
humidities = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
winddirections = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')
sealevelpressures = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

# 저장 디렉터리 생성
dir ='/home/bigdata/weather/weather-{:%y-%m-%d}'.format(datetime.now())
if not os.path.exists(dir):
    os.mkdir(dir)

# 파일로 저장 20-07-15-16.csv
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')

#csv파일 헤더
file.write('지역,시정,현재기온,이슬점온도,체감온도,일강수,습도,풍향,해면기압\n')
for i in range(0, len(locals)):
    file.write(locals[i].text+','+
          visibilities[i].text+','+
          temperatures[i].text+','+
          dewpointtemps[i].text+','+
          sensibletemps[i].text+','+
          percipitations[i].text+','+
          humidities[i].text+','+
          winddirections[i].text+','+
          sealevelpressures[i].text+'\n'
          )

#파일닫기
file.close()

#브라우저 닫기
browser.close()



#print('지역: ', local.text)
#print('현지기온: ', temp.text)

#cron작업 등록
#crontab -e
# * * * * * python3 /root/naver.py
#(분, 시, 일, 월, 요일)
#매분마다 python3 /root/naver.py 을 실행

#cron데몬 서비스 시작/종료
#systemctl start crond
#systemctl stop crond

#cron작업 조회
#crentab -l

#cron작업 삭제
#crentab -r
