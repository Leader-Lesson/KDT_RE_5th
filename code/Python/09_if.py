#!/usr/bin/env python
# coding: utf-8

# ### 9. 조건문
# - 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
# - 조건 : 참/거짓을 구분할 수 있는 문장

# In[ ]:


# 조건문의 기초 문법
# if + 조건 → 조건이 참이면 실행
a = int(input())
if a > 10:
  print("a는 10보다 커요")
print("조건문 종료")


# In[ ]:


# 들여쓰기 에러 예시
if a > 10:
# print("a는 10보다 커요") # indent 에러
  print("조건문 종료")

# In[ ]:


# 조건문에 실행할 코드를 작성하지 않았을 때 
# pass로 해당 조건문을 넘어갈 수 있음
if a > 100:
  pass


# In[ ]:


# 조건식의 평가(Truthy, Falsy한 값)
name = ""
if name:
  print("참이면 실행")


# In[ ]:


# 실습1. ​날씨에 따른 준비물 안내
# 오늘의 날씨에 따라 필요한 준비물이 달라집니다.
# 사용자에게 오늘의 날씨를 입력받고, 그에 따라 적절한 메시지를 출력하는 프로그램을 만들어 보세요.
weather = input("비 또는 맑음을 입력해주세요: ")

# 비가 오는 경우 
# 날씨가 비 라면? → 날씨가 비와 같다
if weather == "비":
  print("우산을 챙기세요!")

# 날씨가 맑은 경우
# 날씨가 맑음 라면? → 날씨가 맑음과 같다
if weather == "맑음":
  print("선크림을 바르세요!")


# In[15]:


# if - else 문
# 조건이 참일 때는 if문을 조건이 거짓일 때는 else문을 실행
# else : '아니라면'의 의미 → 조건이 필요X, if문과 반드시 같이 나와야 함.
a = int(input())
if a > 10:
  print("a는 10보다 커요")
else:
  print("a는 10보다 작아요")


# In[18]:


# 실습2. ​짝수 홀수 판별하기
number = int(input("정수를 입력해주세요."))

#짝수판단
if number % 2 == 0:
  print("짝수입니다.")
else:
  print("홀수입니다.")


# In[23]:


# if - elif - else 구문
# elif : else if 의 약자, 그게 아니라 만약 ~ 라면
# 조건을 반드시 기록
# if가 있어야만 사용할 수 있음
score = int(input())
# 90점 이상이면 a
if score >= 90:
  print("a")
# (90점 미만이고) 80점 이상이면 b
elif score >= 80:
  print("b")
# 70점 이상이면 c
elif score >= 70:
  print("c")
# 60점 이상이면 d
elif score >= 60:
  print("d")
# 그외에는 f
else:
  print("f")


# In[24]:


score = int(input())
# 90점 이상이면 a
if score >= 90:
  print("a")
# (90점 미만이고) 80점 이상이면 b
if score >= 80:
  print("b")
# 70점 이상이면 c
if score >= 70:
  print("c")
# 60점 이상이면 d
if score >= 60:
  print("d")
# 그외에는 f



# In[ ]:


# 실습3. 나이에 따른 영화 관람 가능 여부
# 영화관에서는 연령에 따라 관람할 수 있는 영화가 정해져 있습니다.
# 아래의 기준에 따라 사용자의 나이를 입력 받아 관람 가능한 등급을 출력하는 프로그램을 만들어보세요.
age = int(input("나이를 입력해주세요:"))

if age >= 19:
  print("청소년 관람 불가 가능")
elif age >= 16:
  print("15세이상 관람가 가능")
elif age >= 13:
  print("12세 이상 관람가 가능")
else:
  print("전체 관람가 시청 가능")


# In[3]:


# 실습4
# 조건문을 이용해서 ​초를 입력하면 시, 분, 초로 나누어 알려주는 프로그램을 만들어 봅시다.
# 변수를 만들고 정수를 입력 받아 주세요. 
# 입력 받은 변수의 값을 사용해서 변수 hour와 minute, second에 알맞은 값을 저장해 주세요.
# 조건에 따라 시, 분, 초를 적절히 출력해 주세요.

hour, minute, second = 0, 0, 0

input_second = int(input())

minute = input_second // 60
second = input_second % 60
hour = minute // 60
minute %= 60

if hour > 0:
  print(f"{hour}시간 {minute}분 {second}초")
elif minute > 0:
  print(f"{minute}분 {second}초")
else:
  print(f"{second}초")


# In[ ]:


# 중첩 조건문
# 하나의 if문 안에 또 다른 if문을 사용하는 것

# 로그인 프로세스
username  = input("관리자 아이디를 입력하세요:")
password = input("비밀번호를 입력하세요:.")
if username == "admin" and password == "abcd":
    print("로그인 성공!")
else:
  print("잘못된 입력입니다.")


# In[8]:


# 실습5
money = int(input("금액을 넣어주세요:"))
item = input("김밥 / 삼각김밥 / 도시락 중 골라주세요")
김밥, 삼각김밥, 도시락 = 2500, 1500, 4000

if item == "김밥":
  if money >= 김밥:
    print("김밥을 구입했습니다.")
  else:
    print("금액이 부족해요.")
elif item == "삼각김밥":
  if money >= 삼각김밥:
    print("삼각김밥을 구입했습니다.")
  else:
    print("금액이 부족해요.")
elif item == "도시락":
  if money >= 도시락:
    print("도시락을 구입했습니다.")
  else:
    print("금액이 부족해요.")
else:
  print("입력이 잘못되었습니다.")

