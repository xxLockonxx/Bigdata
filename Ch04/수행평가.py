import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

#데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')

#학습데이터 준비
iris_data  = df_iris[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
iris_label = df_iris['variety']

#훈련데이터와 테스트데이터 분류
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

#학습하기
model = svm.SVC()
model.fit(train_data, train_label)

#검증하기
result = model.predict(test_data)
print(result)

#학습률 확인
score = metrics.accuracy_score(test_label, result)
print('학습률 : ', score)

