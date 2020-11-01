"""
날짜 : 2020/08/18
이름 : 이성진
내용 : 텐서플로 1.x HelloWorld 실습
"""

"""
터미널 열어서
Bigdata>pip install tensorflow-cpu 엔터
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#텐서플로 버전 확인
print(tf.__version__)

#그래프 생성
hello = tf.Variable('Hello Tesorflow!')

#세션 생성
sess = tf.Session()

#그래프 실행
result = sess.run(hello)
print(result)

#세션 종료
sess.close()