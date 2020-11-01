"""
날짜 : 2020/07/22
이름 : 이성진
내용 : 파이썬  hadoop 실습하기
"""

from webhdfspy.webhdfspy import

#Hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

#Local /home/bigdata/naver/naver-20-xx-xx를 하둡 /naver/복사


hdfs.make_dir('/naver')

hdfs.append_file('/home/bigdata/naver/naver-20-07-22', '/naver', naver-20-07-22.encode('utf-8'), overwrite=True)

#Local /home/bigdata/naver/naver-20-xx-xx를 삭제

hdfs.delete_file_dir('/home/bigdata/naver/naver-20-07-22')