#!/usr/bin/env python
# coding: utf-8

# ### 12. 함수(function)
# - 특정 작업을 수행하는 코드들의 모음
# - 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
# - 특정한 코드들을 재사용 할 수 있게 함




# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def 사용
def 함수이름(매개변수):
  # 실행할 코드
  print(매개변수)
  return "반환값"

# 함수의 실행(호출 call)
함수이름("인자")

# 매개변수(Parameter) : 매개 + 변수
# 매개 :둘 사이를 연결해줌
# 함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할

# 인자(Argument)
# 함수의 실행시 매개변수로 전달하는 실제 값





# 함수의 필요성 예제
a = 10
b = 20

if a > b:
  print(a-b)
else :
  print(a+b)

c = 30
d = 40

if c > d:
  print(c-d)
else :
  print(c+d)

e = 100
f = 120

if e > f:
  print(e-f)
else :
  print(e+f)

# ...





def my_func(a,b):
  if a > b:
    return a - b
  else:
    return a + b

print(my_func(10,20))
print(my_func(20,10))
print(my_func(30,50))
print(my_func(50,30))





# 예제1.
def introduce(name):
  print(f"안녕하세요. 처음 뵙겠습니다. {name}입니다.")

introduce("ian")

# 예제2.
def add(x, y):
  return x + y

print(add(10,20))
print(add(100,50))





# 실습 1.
# 함수 이름은 calculate로 합니다.
# 매개변수는 a, b, operator 세 개입니다.
# operator는 문자열이며, 다음 중 하나입니다: "+", "-", "*", "/"
# 나눗셈은 결과를 실수(float) 로 반환합니다.
# 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다"라는 문자열을 반환하세요.

def calculate(a, b, operator):
  if operator == "+":
    return a + b
  elif operator == "-":
    return a - b
  elif operator == "*":
    return a * b
  elif operator == "/":
    return float(a / b)
  else:
    return "지원하지 않는 연산입니다"

print(calculate(20,30,"+"))
print(calculate(50,40,"-"))
print(calculate(5,4,"*"))
print(calculate(100,3,"/"))
print(calculate(1000,10000,"&"))

print(calculate(30,50,"+") + calculate(10,20,"+"))





# 키워드 인자
# 예시 1.
print("안녕하세요", "반갑습니다", sep="-", end=" / ")
print("처음뵙겠습니다", "화이팅!!", sep="-", end=" / ")

# 예시 2.
def my_func(a, b, c=None, operator=None):
  if operator == "+":
    return a + b
  else:
    return c

my_func(10,20,operator="+")





# 기본값 인자
# 단, 기본값 매개변수는 뒤쪽에 위치해야함
def greet(name, message="안녕하세요!"):
  print(f"{name}님, {message}")

# 호출시 인자 생략 → 기본값 사용
greet("ian")
greet("ian", "반갑습니다!")





# 위치 가변 인자
# 여러개의 값을 유동적으로 받을 수 있음
# 값이 튜플 형태로 받아짐

def add_all(*args):
  return sum(args)

add_all(1,2,3,4,5)





# 키워드 가변 인자
# 여러 키워드 인자를 유동적으로 받을 수 있음
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwagrs):
  for key, value in kwagrs.items():
    print(f"{key}: {value}")

print_info(name="ian", age=15, city="서울", job="developer")





# 여러가지 가변 인자를 섞어서 사용할 수 있음
# 단, 가변 인자의 순서가 맞아야 함!!!
# 위치인자 → 키워드인자 → 위치가변인자 → 키워드가변인자
def my_func(a, b=None, *args, **kwagrs):
  print(a)
  print(b)
  print(args)
  print(kwagrs)

my_func(10, 20, 30, 40, 50, name="ian", age=15)





def add_to_list(my_list):
  my_list.append(100)

test_list = [1,2,3]
add_to_list(test_list)

print(test_list)





# 실습 2. 가변인자 연습하기
# 문제 1. 숫자 여러 개의 평균 구하기
def average(*agrs):
  # 예외처리
  if len(agrs) == 0:
    return "입력값이 없습니다"
  return sum(agrs) / len(agrs)

average()





# 문제 2. 가장 긴 문자열 찾기
# 방법 1.
def longgest(*args):
  answer = ""
  for s in args:
    if len(s) > len(answer):
      answer = s
  return answer

# longgest("apple","watermelon","grape","kiwi")

# 방법 2.
def longgest2(*agrs):
    # 예외처리
  if len(agrs) == 0:
    return "입력값이 없습니다"
  return max(agrs, key=len)

longgest2()





# 문제 3. 사용자 정보 출력 함수
# dict.items() 활용
def print_info(**kwagrs):
  for key, value in kwagrs.items():
    print(f"{key}: {value}")

print_info(name="ian", age=15, city="서울", job="developer")





# 문제 4. 할인 계산기
# dict.items() 활용
def discount_price(**kwargs):
  for key, value in kwargs.items():
    discounted = value * 0.9
    print(f"{key}: 할인가 {discounted} (원가 {value})")

discount_price(apple=2000, watermelon=20000, chocolate=2500)





# 전역변수 : 함수 밖에 선언된 변수
# 지역변수 : 함수 안에 선언된 변수 

# 전역변수
x = 100

# 예제
def my_func():
  # 지역변수
  x = 10
  print(x)

  def inner_func():
    x = 50
    print(x)

print("함수밖")

def any_func():
  # 지역변수
  x = 20
  print(x)





# 전역변수와 지역변수 예제1
x = 10

def my_func():
  x = 20
  x += 5
  print("지역변수", x)

my_func()

print("전역변수", x)





# 전역변수와 지역변수 예제1
x = 10

def my_func():
  global x # 전역변수 사용을 선언
  x += 5
  print("지역", x)

my_func()

print("전역", x)





# 예제2
# 보통의 경우, 변수의 변경을 시도하는 것은 하나의 경로를 따라서 변경하게 한다.
x = 10

def func1():
  global x
  x += 10

def func2():
  global x
  x *= 2

func1()
func2()

print(x)





# 권장되는 패턴
# 함수형 프로그래밍
# 부수효과(Side effect)를 발생시키지 않는 함수(순수함수)를 위주로 프로그래밍을 하는 것
x = 10

def my_func(x): # 매개변수는 지역에 존재
  x += 5
  return x

x = my_func(x)

print("전역", x)





# 스택 구조에 대한 예시
def deep_func():
  print("더 안쪽 함수")

def inner_func():
  deep_func()
  print("안쪽 함수")

def outter_func():
  inner_func()
  print("바깥쪽 함수")

outter_func()





# 실습 3. 전역 변수 연습하기
# ✅ 요구사항
# 전역 변수 current_user는 로그인한 사용자의 이름을 저장합니다.
# login(name) 함수는 사용자를 로그인시키고, logout() 함수는 로그아웃 상태로 만듭니다.
# 이미 로그인된 상태에서 다시 로그인하면 "이미 로그인되어 있습니다"를 출력합니다.
# 로그아웃하지 않고 로그인을 여러 번 시도할 수 없도록 합니다.

current_user = None
login_count = 0

def login(name):
  global current_user
  global login_count

  if current_user == None:
    if len(name) > 4:
      current_user = name
      print(f"🤗{name}님 로그인 성공!")
    # 예외처리
    else:
      print("⚠️아이디는 네글자 이상이어야 해요.")

      login_count += 1
      if login_count > 4:
        print("더이상 로그인 시도를 할 수 없습니다.")
  else:
    print("🚨이미 로그인되어 있습니다.")

    login_count += 1
    if login_count > 4:
      print("더이상 로그인 시도를 할 수 없습니다.")


def logout():
  global current_user
  global login_count 
  if current_user == None:
    print("⚠️로그인 상태가 아닙니다.")
  else:
    print("✅로그아웃 되었습니다!")
    current_user = None
    login_count = 0

login("")
login("a")
login("b")
login("c")
login("de")





import time
# 재귀함수
# 1. 자기가 자기 자신을 호출하는 함수
# 2. 반드시 기본 조건(종료 조건)이 있어야 함
# - 큰 문제를 작은 문제로 나누었을 때 일정한 패턴이 있어야 함

def recursive_func(n):
  # 기본 조건
  if n == 0:
    return
  recursive_func(n-1)
  print("재귀 호출", n)
  time.sleep(1)

recursive_func(5)





# 실습 4. 거듭 제곱
# 반복문으로 구현
def power_for(a, n):
  result = 1
  for _ in range(n):
    result *= a
  return result

print(power_for(4,3))

# 재귀함수 구현
def power_rec(a, n):
  if n == 0:
    return 1
  return a * power_rec(a, n - 1)

print("재귀함수", power_rec(4,3))





# 실습 5. 팩토리얼
# 반복문으로 구현
def factorial_for(n):
  # 예외처리
  if n < 0:
    return "음수의 팩토리얼은 정의되지 않습니다."

  result = 1

  for i in range(1, n+1):
    result *= i

  return result

factorial_for(5)

# 재귀함수
def factorial_rec(n):
  # 예외처리
  if n < 0:
    return "음수의 팩토리얼은 정의되지 않습니다."

  # 기본조건
  if n == 0 or n == 1:
    return 1

  return n * factorial_rec(n - 1)

factorial_rec(-10)
factorial_rec(0)
factorial_rec(5)





# 실습 6. 피보나치 수열
# 반복문
def fibonacci_for(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1

  a,b = 0,1
  for _ in range(n-1):
    a,b = b,a+b

  return b

fibonacci_for(6)

# 재귀함수
def fibonacci_rec(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1

  return fibonacci_rec(n-1) + fibonacci_rec(n-2)

fibonacci_rec(20)





# 람다(lambda) 함수
# 익명 함수
# 간단한 함수를 한줄로 표현할 때 사용

# 람다 함수의 기본 문법
# lambda 매개변수: 표현식
# 표현식 : 값이 반환되는 식
3 + 5
3 == 5

# 일반함수와 비교
def add(x, y):
  return x + y

# 람다를 재활용 하려면 → 변수에 담아서 활용
add_func = lambda x, y: x + y

# 저장한 람다 함수의 활용
add_func(3,5)

# 람다로 값을 반환하고 사용을 끝내는 경우
(lambda x: x ** 2)(10)





# 람다함수의 활용
# 1. map에서 활용
my_list = [1,2,3,4]

# 일반 함수를 사용
def square_func(x):
  return x ** 2

# 함수를 인자로 받는 함수 → 고차 함수(Higher-order Function)
list(map(square_func, my_list))

# 람다 함수를 사용
list(map(lambda x: x ** 2, my_list))

# 2. filter에서 활용
my_list2 = [1,2,3,4,5,6,7,8,9,10]

# 일반 함수를 사용
def is_even(x):
  return x % 2 == 0

list(filter(is_even, my_list2))

# 람다 함수를 이용
list(filter(lambda x: x % 2 ==0, my_list2))

# 3. sorted에서 활용
my_list3 = ["apple", "banana", "watermelon", "grape"]
sorted(my_list3, key=lambda word: len(word), reverse=True)





# 실습 7.
# 📌 문제1. 특정 조건 만족하는 튜플만 추출
students = [
    ("Alice", [80, 90]),
    ("Bob", [60, 65]),
    ("Charlie", [70, 70]),
]

list(filter(lambda s: sum(s[1]) / len(s[1]) >= 70, students))





# 📌 문제2. 키워드 추출 리스트 만들기
sentences = [
    "Python is fun",
    "Lambda functions are powerful",
    "Coding is creative"
]

list(map(lambda s: s.split()[0], sentences))





# 📌 문제3. 튜플 리스트를 정렬하기
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

sorted(people, key=lambda person: person[1])

