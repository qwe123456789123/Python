import random

import matplotlib.pyplot as plt

# [1]  선 차트
    # 데이터 수집
x=['kim','lee','park']
y1= [80,79,93]
y2= [100,110,120]

plt.title('member point')
plt.plot(x,y1,label = 'point1', color='blue')
plt.plot(x,y2,label = 'point2', color='black')
plt.legend() # 범례
plt.show()

# [2] 막대 차트
plt.title('bar chart')
plt.bar(x,y1, label= 'point1')
plt.bar(x,y2, label= 'point2')
plt.show()
import random # 랜덤 관련 함수를 제공하는 랜덤 모듈 가져오기
# [3] 산점도 : x축과 y축 값의 관계를 시각화
x= [random.random() for _ in range(50)]
y= [random.random() for _ in range(50)]
    # random.random() for _ in range(50) 0부터 49 까지 1씩 증가하면서 난수 생성
    # [random.random() for _ in range(50)] : [ 표현식 for 반복변수 in 리스트/range()]  : 리스트 검프리헨션
plt.scatter(x,y)
plt.show()
#[4] 원형 차트 : 백분율
size = [82,100]
labels = ['m','w'] # 남 여
plt.pie(size,labels=labels , autopct= '% .1f%%')
plt.show()

# 실습1 학생의 시험 성적 데이터를 시각화 하기
s1= [63,78,53]
s2= [83,77,100]
s3= [71,88,99]
x1= ['중간고사','기말고사','모의고사']
plt.title('test')
plt.plot(x1,s1,label = '1학년성적', color='blue')
plt.plot(x1,s2,label = '2학년성적', color='black')
plt.plot(x1,s3,label = '3학년성적', color='red')
plt.legend() # 범례
plt.show()