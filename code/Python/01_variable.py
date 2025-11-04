# 변수(Variable)
"""
- 변수 : 자료를 저장하는 공간
- 선언 : 변수를 만드는 것
- 할당 : 변수에 값을 저장하는 것
- 초기화 : 처음으로 변수에 값을 할당하는 것 
- = : 대입 연산자, **등호가 아님!!!** ( 같다 → == )
  - 변수에 값을 저장한다(할당한다)는 의미
"""

# 변수의 선언과 할당
변수이름 = "저장할자료"
print(변수이름)
print(변수이름)
print(변수이름)

# 변수 이름 규칙
# 1st_place = "Gold"
fisrt_place = "Gold"

# user name = "Alice"
user_name = "Alice"

# class = "Math"
class_name = "Math"

# 변수의 특징
# 저장한 값을 바꿀 수 있다.
# 단, 한번에 하나씩만 저장된다.
인사 = "안녕하세요"
인사 = "반갑습니다"
print(인사)

# 파이썬에서 변수는 선언과 함께 초기화를 해줘야함
# 새로운변수 (X)
새로운변수 = "선언과 함께 초기화"

# 한 줄에 여러 변수 만들기
a = 1
b = 2
c = 3

a, b, c = 1, 2, 3

print(a, b, c)

x = 10
y = 20

x, y = y, x
print(x, y)

# 출력 : print 함수
# 내가 작성한 코드가 잘 작성됐는지 확인할 때 사용
print("Hello world!")

# print의 구분자 옵션
# sep
print("가", "나", "다", sep="-")

# print의 줄바꿈 옵션
# end
print("안녕하세요.", end=" ")
print("반갑습니다.", end=" ")
print("처음뵙겠습니다.")