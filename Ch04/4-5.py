"""
날짜 : 2020/08/11
이름 : 이성진
내용 : 머신러닝 - 다중선형회귀 분석 연습문제
문제 : 아래와 독립변수 '성별'이 추가 될 경우의 선형회귀분석을 수행한 후 키 180cm, 나이 27, 성별 1 데이터의 예측값을 추정하시오.
"""


from sklearn.linear_model import LinearRegression

#학습데이터
train_data = [[170, 30, 1], [155, 60, 2], [150, 50, 2], [175, 40, 1], [165, 20, 1]]
train_label = [65, 50, 45, 70, 55]

#학습하기
model = LinearRegression()
model.fit(train_data, train_label)

#모델검증
test_data = [[180, 27, 1], [180, 27, 2]]
result = model.predict(test_data)
print('result :', result)