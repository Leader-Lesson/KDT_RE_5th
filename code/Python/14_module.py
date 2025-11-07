#!/usr/bin/env python
# coding: utf-8

# ### 14. 모듈(module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것

# In[ ]:


# 모듈 불러오기(1)
import hello

hello.greeting("ian")


# In[ ]:


# 모듈 불러오기(2)
from hello import greeting

greeting("ian")
introduce("ian", 15)


# In[ ]:


# 모듈 불러오기(3)
from hello import *

greeting("ian")
introduce("ian", 15)


# In[ ]:


# 모듈 불러오기(4)
import hello as h

h.greeting("ian")
h.introduce("ian", 15)


# In[ ]:


# 실습1. 계산기 모듈 만들어보기
import Python.my_package.calc as c

c.add(3, 5)
c.subtract(10, 3)
c.mutiply(2, 10)
c.divide(3, 0)
c.divide(20, 3)


# In[ ]:


# 패키지
# 모듈의 묶음
# 모듈을 폴더단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
# 별칭은 상황에 따라 적절하게!
from my_package import calc as c

c.add(10,20)


# In[ ]:


# 패키지에서 모듈 불러오기(2)
from my_package.calc import add


# In[ ]:


# 파이썬 표준 라이브러리
# math 모듈 : 수학적 연산에 사용되는 모듈
import math

# 1. 올림/내림
# round : 반올림 - 파이썬 내장 함수
round(3.141592, 2) 

# ceil : 올림, 소수점 지정X
math.ceil(3.14)

# floor : 내림, 소수점 지정X
math.floor(3.14)

# 2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^y를 반환
math.pow(2,3)

# sqrt(x) : 제곱근 반환
math.sqrt(16)

# 3. 상수
# pi : 원주율
math.pi

# 4. 수학 계산 편의 기능
# factorial(x) : x! 팩토리얼 반환
math.factorial(5)

# gcd(x, y) : 최대 공약수
math.gcd(12, 20)

# lcm(x, y) : 최소 공배수
math.lcm(12, 20)


# In[ ]:


# 실습2.
# 📌 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

# 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
dist = round(math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)), 2)

print(f"두 점 사이의 거리는: {dist}")


# In[ ]:


# 📌 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
a = 18
b = 24

# 최대공약수 
gcd = math.gcd(a,b)

# 최소공배수
lcm = math.lcm(a,b)

print(f"최대 간식 개수: {gcd}")
print(f"최소 간식 개수: {lcm}")


# In[ ]:


# random 모듈 : 랜덤 값(난수) 생성시 사용
import random

# 1. 난수 생성
# seed(a) : 난수 발생 초기값(seed) 설정 - 최초 생성한 난수를 고정해야 할 때 사용
# random.seed(42)

# random() : 0이상 1미만의 float 난수 반환
random.random()

# uniform(a, b) : a이상 b이하의 실수 난수 반환
random.uniform(1, 10)

# ranint(a, b) : a이상 b이하의 정수 난수 반환
random.randint(1, 100)

# randrange(start, stop, step) : 범위 안의 정수 난수 반환, 간격 지정 가능
random.randrange(0, 100, 5)

# 2. 랜덤 선택
fruits = ["apple", "banana", "watermelon", "grape", "orange"]

# choice(seq) : 시퀀에서 임의의 요소 1개 반환
random.choice(fruits)

# choices(seq, k) : 시퀀스에서 "중복 허용" k개 요소 리스트를 반환
random.choices(fruits, k=2)

# sample(seq, k) : 시퀀스에서 "중복 없이" k개 요소 리스트를 반환
random.sample(fruits, k=2)

# shuffle(seq) : 시퀀스의 요소를 무작위로 섞음 → 원본 시퀀스를 변경
numbers = [1,2,3,4,5]
random.shuffle(numbers)
numbers


# In[ ]:


# 실습3. 로또 번호 뽑기
# 1 ~ 45사이의 정수중에서 랜덤으로 6개의 숫자를 뽑는다
# 6개의 숫자는 중복이 있어서는 x
# 오름차순으로 결과를 정렬한다!
# 방법1
import time

lotto = []

while len(lotto) < 6:
  number = random.randint(1,45)
  if number in lotto:
    continue
  print(number)
  lotto.append(number)
  time.sleep(1)

lotto.sort()
print(lotto)


# In[ ]:


# 방법2
result = sorted(random.sample(range(1,46), k=6))
result


# In[ ]:


# 실습4. 가위 바위 보 게임 만들기
import random

RPS = ["가위", "바위", "보"]
win_count = 0

while win_count < 3:
  com_choice = random.choice(RPS)
  user_choice = input("가위, 바위, 보 중에 골라주세요!✌️✊🤚: ")

  print(f"유저의 선택: {user_choice}")
  print(f"컴퓨터의 선택: {com_choice}")
  if user_choice == com_choice:
    print("😑비겼습니다!")
  elif (
    (user_choice == "가위" and com_choice == "보") or
    (user_choice == "바위" and com_choice == "가위") or
    (user_choice == "보" and com_choice == "바위")
  ):
    print("🤗이겼습니다!")
    win_count += 1
  elif user_choice in RPS:
    print("😣졌습니다ㅠㅠ")
  else:
    print("🚨잘못된 입력에요!")

  print(f"현재 승리 횟수: {win_count}")


# In[ ]:


# datetime 모듈 
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공
import datetime

# 1. 날짜/시간 구하기
# 현재 날짜와 시간 구하기
now = datetime.datetime.now()

# 오늘 날짜만 구하기
today = datetime.date.today()

# 2. 날짜/시간 형식 변환
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
formatted

parsed = datetime.datetime.strptime(formatted,"%Y/%m/%d %H:%M:%S")
parsed

# 3. 날짜/시간 연산
dt = datetime.date(2025, 7, 7)
passed_time = today - dt
print(f"개강 이후 {passed_time.days}일이 지났습니다.")

# 4. 요일반환 : weekday
# 0: 월요일 ~ 7: 일요일
days = ["월","화","수","목","금","토","일"]
day_num = today.weekday()
days[day_num]

추석 = datetime.date(2025, 10, 6).weekday()
days[추석]

# datetime 또는 date 객체에는 년/월/일 시간 등이 속성으로 들어있음
datetime.datetime.now().year
datetime.date.today().day


# In[ ]:


# calendar 모듈
# 날짜와 달력 관련 기능을 제공
import calendar

# 1. 달력 조회
calendar.prmonth(2025, 9)
calendar.prcal(2025)

# 텍스트로 값을 반환
calendar.month(2025, 9)
calendar.calendar(2025)

# 요일 반환
calendar.weekday(2025, 7, 7)


# In[ ]:


import datetime

# 사용자로부터 생일을 입력받음
birth_month, birth_day = map(int, input("생일을 입력하세요.(예 03/14):").split("/"))

# 오늘 날짜 구하기
today = datetime.date.today()

# 올해 생일을 date 객체로 변환(why? 날짜 계산해야 하니까)
birthday_this_year = datetime.date(today.year, birth_month, birth_day)

# 오늘 날짜와 올해 생일을 비교
if today > birthday_this_year:
  # 올해 생일이 지났으면 내년으로 설정
  birthday_next = datetime.date(today.year + 1, birth_month, birth_day)
else:
  # 아니면 올해로 설정
  birthday_next = birthday_this_year

# 남은 일수를 계산
days_left = (birthday_next - today).days

print(f"다음 생일까지 {days_left}일이 남았어요!🎉")


# In[ ]:


# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능 제공
import time

# 1. 시간 반환
# time()
# Unix 타임스탬프로 반환(1970.1.1부터 경과 초)
time.time()

# ctime() : 현재 시간을 문자열로 반환
time.ctime()
time.ctime(0) # 기준시로 반환

# strftime() : 원하는 포맷의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted)

# stfptime() : 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)

# 2. 시간 지연
# sleep(seconds) : 지정한 초만큼 프로그램이 일시 중지
time.sleep(1) 


# In[ ]:


# 시간 측정하기
start = time.time()

for i in range(5):
  print(i)
  time.sleep(1)

end = time.time()
print(f"수행시간 : {end-start: .2f}초")


# In[ ]:


# 실습6. 타자연습게임
import random
import time

words = [
    "apple", "banana", "orange", "grape", "lemon",
    "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden",
    "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market",
    "doctor", "planet", "energy", "nature", "memory"
]

n = 1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    question = random.choice(words)
    print(question)
    user_answer = input()

    if user_answer == "종료":
        break

    if question == user_answer:
        print("통과!")
        n += 1
    else:
        print("오타! 다시 도전!")

end = time.time()
et = end - start
print(f"총 소요시간 : {et: 2f}초")


# In[ ]:


# sys 모듈 
# 파이썬 인터프리터와 관련된 다양한 기능 제공

import sys

# 파이썬 버전 정보
sys.version

# 운영체제 정보
sys.platform


# In[ ]:


import sys

print("프로그램 시작")
sys.exit() # 프로그램 강제 종료
print("이 코드는 실행되지 않습니다.")


# In[ ]:


# os 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공
import os

# getcwd(): 현재 작업 디렉토리 반환
os.getcwd()

# listdir(): 현재 폴더내 파일, 디렉터리 목록 반환
os.listdir()


# In[7]:


import os

folder_name = "sample_folder"
if not os.path.exists(folder_name):
  os.mkdir(folder_name)
else:
  print(f"{folder_name} 폴더가 이미 존재합니다.")

print(os.listdir())

