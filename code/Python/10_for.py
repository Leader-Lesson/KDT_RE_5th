#!/usr/bin/env python
# coding: utf-8

# ### 10. for문
# - 이터러블의 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# In[ ]:


import time

# for문 기본 문법

for 반복변수 in ["가","나","다","라"]:
  # 반복할 코드
  print(반복변수)
  time.sleep(1)


# In[ ]:


# 리스트로 반복
fruits = ["사과", "배", "수박", "참외", "포도"]

for fruit in fruits:
  print(fruit)
  time.sleep(1)


# In[ ]:


# 문자열로 반복
my_str = "CodingOn"

for char in my_str:
  print(char)


# In[ ]:


# 튜플을 활용한 반복
좌표 = [(1,2), (10,15), (-6,8)]

# 언패킹 가능
for x,y in 좌표:
    print(f"x좌표: {x}, y좌표: {y}")
    time.sleep(1)


# In[ ]:


# 딕셔너리를 이용한 반복
person = {
  "name" : "ian",
  "age" : 15,
  "address" : "창동"
}

# 기본적인 활용
for key in person:
  print(f"key: {key}, value: {person[key]}")

# value만 가져오기
for value in person.values():
  print(f"value: {value}")

# item 가져오기
for key, value in person.items():
  print(f"key: {key}, value: {value}")


# In[ ]:


# 실습 1.
# 문제 1.
numbers = [3, 6, 1, 8, 4]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)


# In[ ]:


# 문제 2.
words = ["apple", "banana", "kiwi", "grape"]
lengths = []

for word in words:
  lengths.append(len(word))

print(lengths)


# In[ ]:


# 문제 3.
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_values = []
y_values = []

for x, y in coordinates:
  x_values.append(x)
  y_values.append(y)

print(f"x 좌표: {x_values}")
print(f"y 좌표: {y_values}")


# In[ ]:


# for문과 range()
# range 함수 : 지정된 범위의 정수 시퀀스
# range 자료형 (시퀀스 자료형)

# 기본문법
# range(start, end, step) 
list(range(1,5))

# for i in range(1,5):
#   print(i)

# for i in [1,2,3,4]:
#   print(i)

# start를 생략
range(5)

for i in range(10):
  print(i)

# for i in [0,1,2,3,4,5,6,7,8,9]:
#   print(i)

# 반복문의 반복변수는 꼭 써야할까?
for i in range(100):
  print("안녕하세요!")


# In[ ]:


# 간격(step) 지정
for i in range(0, 11, 2):
  print(i)


# In[ ]:


# 역순 반복
# 카운트다운
for i in range(10, 0, -1):
  print(i)
  time.sleep(1)


# In[ ]:


# range의 다양한 활용
print(list(range(1,10)))
print(list(range(10)))
print(list(range(1,10,2)))
print(list(range(3,100,3)))
print(list(range(10,0,-1)))


# In[ ]:


# 실습 2.
# 문제 1.
num = int(input("숫자를 입력하세요:"))
sum_num = 0

for i in range(num+1):
  sum_num += i

print(sum_num)


# In[ ]:


# 문제 2. 
dan = int(input("생성할 단을 입력해주세요:"))

for i in range(1,10):
  print(f"{dan} x {i} = {dan * i}")


# In[ ]:


# 문제 3.
result = 0

# for i in range(3,101,3):
#   # result = result + i
#   result += i

for i in range(1,101):
  if i % 3 == 0:
    result += i

print(result)


# In[ ]:


n = int(input())

# for i in range(1, n+1):
#   if i % 2 == 0 and i % 5 == 0:
#     print(i)

# for i in range(2, n+1, 2):
#   if i % 5 == 0:
#     print(i)

for i in range(1, n+1):
  if i % 2 == 0:
    if i % 5 == 0:
      print(i)


# In[ ]:


# 루프 제어문
# 특정 조건 하에서만 작동하도록 구현
# break : 반복을 즉시 중단

for i in range(10):
  if i == 5:
    break
  print(i)

print("반복 종료")


# In[ ]:


# continue : 현재 반복을 넘어감

for i in range(5):
  if i == 2:
    print("건너뜀")
    continue
  print(i)
  time.sleep(1)

print("반복 종료")


# In[ ]:


# pass
for i in range(10):
  pass


# In[ ]:


# for - else 구문
for i in range(5):
  if i == 2:
    break
  print(i)
else:
  print("반복종료")


# In[ ]:


# 중첩 for문
# 하나의 for문 안에 다른 for문이 들어있는 구조

# 이중 for문
for i in range(5):
  for j in range(5):
    print("🌟", end="")
    time.sleep(1)
  print()
  time.sleep(2)


# In[ ]:


# 이중 for문
for i in range(4):
  for j in range(4):
    print(f"{i},{j}", end=" ")
    time.sleep(1)
  print()
  time.sleep(1)


# In[ ]:


colors = ["red", "blue"]
fruits = ["apple", "banana"]

for color in colors:
  for fruit in fruits:
    print(f"{color}: {fruit}")


# In[ ]:


# 문제 1.
for i in range(2,10):
  print(f"[ {i}단 ]")
  for j in range(1,10):
    print(f"{i} x {j} = {i*j}")
  for j in range(1,10):
    print(f"{i} x {j} = {i*j}")
  print()


# In[ ]:


# 문제 2. 별찍기
# 왼쪽 정렬
n = int(input("몇 줄?:"))

for i in range(1, n+1):
  for j in range(i):
    print("🌟", end="")
  print()


# In[ ]:


# 오른쪽 정렬
n = int(input("몇 줄?:"))

for i in range(1, n+1):
  for j in range(n - i):
    print(" ", end="")
  for j in range(i):
    print("*", end="")
  print()


# In[ ]:


# 가운데 정렬
n = int(input("몇 줄?:"))

for i in range(1, n+1):
  # 공백 출력
  for j in range(n - i):
    print(" ", end="")
  # 별 출력
  for j in range(2 * i - 1):
    print("*", end="")
  print()


# In[ ]:


# 리스트 컴프리헨션(List Comprehension)
# for문을 리스트에 한줄로 축약하여 새리스트를 생성하는 문법
# [표현식(리스트의 원소) for 변수 in 반복대상 if 조건]
# 표현식 : 값을 유도하는 식(표현)

# for문 이용
squares = []
for x in range(1,6):
  squares.append(x ** 2)
print(squares)

# 리스트 컴프리헨션
squares_2 = [x ** 2 for x in range(1,6)]
print(squares_2)


# In[ ]:


# 조건문 추가하기
squares_3 = [x ** 2 for x in range(1,11) if x % 2 == 0]
squares_3


# In[ ]:


words = ["apple", "banana", "kiwi", "grape"]
lengths = [len(word) for word in words]
lengths


# In[ ]:


numbers = [3, 6, 1, 8, 4]
doubled = [x * 2 for x in numbers]
doubled


# In[ ]:


# 중첩 for문
colors = ["red", "blue"]
fruits = ["사과", "수박"]

pairs = [(color, fruit) for color in colors for fruit in fruits]
pairs


# In[21]:


# 실습 4.
# 문제 1.
squares = [x**2 for x in range(1,11)]
print(squares)


# In[ ]:


# 문제 2.
result = [x for x in range(3, 51) if x % 3 == 0]
print(result)


# In[25]:


# 문제 3.
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
words = [fruit for fruit in fruits if len(fruit) >=5]
print(words)

