#!/usr/bin/env python
# coding: utf-8

# ### 13. 클래스(class)
# - 데이터와 기능을 하나로 묶는 구조
# - 개념적(기능적)으로 유사한 관계에 있는 것들을 묶어줌




# 클래스 기본 문법
# 클래스의 정의
class ClassName:
  # 생성자(Constructor) : 인스턴스가 생성될 때 호출
  # 인스턴스 변수를 초기화, 기본 상태 설정
  # 하나의 클래스에서 하나만 정의 가능
  def __init__(self, name): 
    # 인스턴스 변수
    # self : 인스턴스 자기 자신을 가리킴
    self.name = name
    self.age = 0

  # (인스턴스) 메서드
  def method_name(self):
    print(f"이 인스턴스의 이름은 {self.name}입니다.")

# 인스턴스의 생성
my_instance = ClassName("내 인스턴스")
my_instance.name
my_instance.method_name()

another_intance = ClassName("다른 인스턴스")
another_intance.method_name()





class Person:
  def __init__(self, name, age, address, hobby):
    self.name = name
    self.age = age
    self.address = address
    self.hobby = hobby

  def introduce(self):
    print(f"안녕하세요. 저는 {self.name}입니다. 나이는 {self.age}살입니다.")
    print(f"사는 곳은 {self.address}이구요. 취미는 {self.hobby}입니다.")

  def add_age(self):
    self.age += 1
    print(f"나이를 한 살 더 먹었습니다. 현재나이: {self.age}")

p1 = Person("ian", 15, "창동", "책읽기")
p1.introduce()
p1.add_age()
p1.introduce()
print()

p2 = Person("codingowl", 5, "염리동", "코딩")
p2.introduce()
p2.add_age()
p2.introduce()





# 실습1.
# 📌문제1. 책 클래스 만들기

class Book:
  def __init__(self, title, author, total_pages, current_page):
    self.title = title
    self.author = author
    self.total_pages = total_pages
    self.current_page = current_page

  def read_page(self, pages):
    self.current_page += pages

    if self.current_page > self.total_pages:
      self.current_page = self.total_pages
      print("책을 끝까지 다 읽었어요.")

  def progress(self):
    percent = (self.current_page / self.total_pages) * 100
    print(f"현재 읽은 분량: {self.current_page}/{self.total_pages} ({percent: .1f}% )")

nexus = Book("넥서스", "유발 하라리", 500, 1)
nexus.title
nexus.author
nexus.read_page(50)
nexus.progress()

nexus.read_page(500)
nexus.progress()





# 📌문제2. Rectangle 클래스 구현
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

w = int(input("넓이를 입력하세요."))
h = int(input("높이를 입력하세요."))

my_rect = Rectangle(w, h)

print(f"사각형의 넓이는 {my_rect.area()}입니다.")





# 클래스 변수
# 클래스가 가지고 있는 변수
# 모든 인스턴스가 공유할 수 있음
class Dog:
  # 클래스 변수
  kind = "강아지"

  def __init__(self, species, name, age):
    self.species = species
    self.name = name
    self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print("인1", dog1.kind)
print("인2", dog2.kind)
print("클래스", Dog.kind)





# 클래스 메서드
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스의 데이터를 조작하는데 사용
class Book:
  book_count = 0

  def __init__(self, title, author):
    Book.book_count += 1
    self.title = title
    self.author = author

  @classmethod # 데코레이터
  def get_count(cls):
    print(f"현재 {cls.book_count}권의 책을 가지고 계십니다.")

book1 = Book("넥서스", "유발 하라리")
book2 = Book("맹자", "맹자")
Book.get_count()





# 정적 메서드
# 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않는 함수를 정의

class OperationTool:
  @staticmethod # 데코레이터
  def add(a, b):
    return a + b

OperationTool.add(10,20)





# 실습2. User 클래스 구현
class User:
  total_users = 0

  def __init__(self, username, points):
    User.total_users += 1
    self.username = username
    self.points = points

  def add_points(self, amount):
    self.points += amount

  def get_level(self):
    if self.points >= 500:
      return "Gold"
    elif self.points >= 100:
      return "Silver"
    else:
      return "Bronze"

  @classmethod
  def get_total_users(cls):
    print(f"총 유저 수: {cls.total_users}")

u1 = User("ian", 100000)
u1.username = "이안"
print(u1.username)
u2 = User("codingowl", 100)
u3 = User("사자보이즈", 1000)
User.get_total_users()





# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상 시키기 위함
class Person:
  def __init__(self, name, age):
    # public
    self.name = name
    # private : 언더바(_) 두개를 변수 앞에 붙여서 정의
    self.__age = age

  # getter
  def get_age(self):
    return self.__age

  # setter
  def add_age(self, value):
    if value > 120 or value < 0:
      print("유효하지 않은 나이입니다.")
    else :
      self.__age = value

p1 = Person("ian", 15)
p1.name = "똥멍청이"
p1.name

# 외부에서 private 요소에 접근시도 → 접근할 수 없음
# p1.__age
p1._Person__age # 권장되지X

p1.add_age(130)

# p1.get_age()
# p1.add_age()
# p1.get_age()





# @property 데코레이터
# 메서드를 속성처럼 보이게 만들어주는 데코레이터

# 기본문법
class ClassName:
  def __init__(self):
    self.__value = 0

  # getter
  @property
  def value(self):
    return self.__value

  # setter
  @value.setter
  def value(self, val):
    if val < 0:
      print("유효하지 않은 값입니다.")
    else:
      self.__value = val

c1 = ClassName()
c1.value
c1.value = 100
c1.value
c1.value = -100
c1.value





# 실습3.
# 문제1. UserAccount 클래스 : 비밀번호 보호
class UserAccount:
  def __init__(self, username, password):
    self.username = username
    self.__password = password

  def change_password(self, old_pw, new_pw):
    if self.__password == old_pw:
      self.__password = new_pw
      print("🤗비밀번호가 변경되었어요.")
    else:
      print("😣비밀번호가 일치하지 않아요.")

  def check_password(self, password):
    return self.__password == password

user1 = UserAccount("ian_genius", "abc123")
user1.username
# user1.__password

user1.change_password("abcd1234", "qwer1234")
user1.change_password("abc123", "qwer1234")
user1.check_password("qwer1234")





# 문제 2. Student 클래스: 성적 검증
class Student:
  def __init__(self, name, score):
    self.name = name
    self.__score = score

  @property # getter
  def score(self):
    return self.__score

  @score.setter
  def score(self, value):
    if 0 <= value <= 100:
      self.__score = value
    else:
      raise ValueError("범위를 벗어난 값입니다.")

s1 = Student("ian", 0)
s1.score
s1.score = 50
s1.score
s1.score = 200





# 상속
# 부모 클래스의 속성과 메서드를 물려받아 새로운 자녀 클래스를 만드는 것

# 상속 기본 문법
# 부모 클래스
class Animal:
  def __init__(self, name):
    self.name = name

  def bark(self):
    print("동물이 울음 소리를 냅니다.")

# 자녀 클래스
class Dog(Animal):
  pass

d = Dog("구름이")
d.bark()
d.name





class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("동물이 울음 소리를 냅니다.")

# 자녀 클래스
class Dog(Animal):
  # 오버라이딩
  def __init__(self, name, age, species):
    # super는 부모를 가리킴
    # 부모의 함수를 그대로 복제함
    super().__init__(name, age)
    self.species = species

  # 오버라이딩
  def bark(self):
    super().bark()
    print("멍멍")

d = Dog("리치", 12, "포메라니안")
d.bark()
print(d.name)
print(d.age)
print(d.species)





# 다단계 상속
class LivingBeing:
  def __init__(self):
    self.alive = True

class Animal(LivingBeing):
  def __init__(self, name, age):
    super().__init__()
    self.name = name
    self.age = age

  def eat(self):
    print(f"{self.name}이(가) 음식을 먹습니다.")

class Dog(Animal):
  def __init__(self, name, age, species):
    super().__init__(name, age)
    self.species = species

  def bark(self):
    print(f"{self.name}은(는) {self.species}이며 멍멍 짖어요.")

d = Dog("구름이", 10, "비숑")
d.alive
d.eat()
d.bark()





# 실습4.
# 문제 1. Shape 클래스 오버라이딩
class Shape:
  def __init__(self, sides, base):
    self.sides = sides
    self.base = base

  def pritInfo(self):
    print(f"변의 개수: {self.sides}")
    print(f"밑변의 길이: {self.base}")

  def area(self):
    print("⚠️넓이 계산이 정의되지 않았어요.")

class Rectangle(Shape):
  def __init__(self, sides, base, height):
    super().__init__(sides, base)
    self.height = height

  def area(self):
    area = self.base * self.height
    print(f"{self.sides}각형의 넓이: {area}")

class Triangle(Shape):
  def __init__(self, sides, base, height):
    super().__init__(sides, base)
    self.height = height

  def area(self):
    area = int((self.base * self.height) / 2)
    print(f"{self.sides}각형의 넓이: {area}")

r = Rectangle(4, 10, 5)
r.pritInfo()
r.area()
print()
t = Triangle(3, 8, 6)
t.pritInfo()
t.area()



# 추상 클래스(Abstract Class)
# 클래스의 구조를 정의하는 클래스

from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def bark(self):
    pass

class Dog(Animal):
  def bark(self):
    print("멍멍")

# a = Animal()
d = Dog()
d.bark()





# 실습5. 추상 클래스 Payment 구현
from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

class CardPayment(Payment):
  def __init__(self):
    super().__init__()

  def pay(self, amount):
    print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
  def pay(self, amount):
    print(f"현금으로 {amount}원을 결제합니다.")

card = CardPayment()
card.pay(10000)

