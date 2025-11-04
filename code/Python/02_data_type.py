2. 자료형(Data type)
자료의 종류와 구조를 정의하는 것
파이썬 : 동적 타입 언어(↔ 정적 타입 언어)
변수를 만들때 별도의 타입을 지정하지 않아도 됨
# 1. 문자열(string, str)
my_str1 = '' # 빈문자열(O)
my_str2 = " " # 공백문자열(O)
my_str3 = "안녕하세요" # "요하녕안세" → 문자열은 '순서가 있는 자료형'

# 문자열 여러줄로 만들기
multi_str = """코: 코딩을 한다
딩: 딩딩딩 머리가 울린다
온: 온제 끝나나
"""
print(multi_str)

print("코: 코딩을 한다")
print("딩: 딩딩딩 머리가 울린다")
print("온: 온제 끝나나")

print(type(multi_str))
# 따옴표 속에 따옴표 쓰기
print("'지식'은 우정을 대신하지 않아")
print('"지식"은 우정을 대신하지 않아')

multi_str = """코: '코딩'을 한다
딩: '딩딩딩' 머리가 울린다
온: '온제' 끝나나
"""
print(multi_str)
# 2. 정수형(integer, int)
# 크기 제한이 없음
my_int1 = 100
my_int2 = 2103801283091823908120938109283012839018293182038
print(type(my_int1))
# 3. 실수형(float)
# 부동소수점 방식
my_float1 = 100.0
my_float2 = 3.14
print(type(my_float1))
# 4. 논리형(boolean, bool)
# 참(1)과 거짓(0)을 표현하는 자료형
print(True)
print(False)
print(type(True))
print(type(False))
# f-string : 문자열 포매팅(formatting)
# 문자열 안에 변수를 쓸 수 있도록 해주는 기능
my_name = "Ian"
my_age = 15

# 일반적으로 print를 사용했을 때
# 내 이름은 Ian이고, 나이는 15살입니다.
print("내 이름은", my_name, "이고, 나이는", my_age, "입니다.")

# 공격력 : 100, 방어력 : 80, 민첩성 : 95, 지력 : 105
power, defence, agility, intelligence = 100, 80, 95, 105
print("공격력 :", power, ", 방어력 :", defence, ", 민첩성 :", agility, ", 지력 :", intelligence)

# f-string 사용
print(f"공격력 : {power}, 방어력 : {defence}, 민첩성 : {agility}, 지력 : {intelligence}")
# 이전방식1
print("내 이름은 %s입니다" % "ian")
print("내 나이는 %d살입니다" % 15)

# 이전방식2
print("내 이름은 {}입니다.".format("ian"))
# 형 변환(Type casting)
# 명시적 형변환(explicit) vs 암시적 형변환(implicit)
# 강타입 vs 약타입

# * 1. 정수로 변환 : int()
# 1) 실수 → 정수
# 2) 문자열로 표현된 정수 → 정수
# 3) 논리형 → 정수
# ✅ 가능한 경우
print(f"3.14 → {int(3.14)}")
print(f"'100' → {int('100')}")
print(f"True → {int(True)}")
print(f"False → {int(False)}")

# ❌ 불가능한 경우
print(int("3.14")) # 문자열로 표현된 실수
print(int("abc"))
# 2. 실수로 변환 : float()
# 1) 정수 → 실수
# 2) 문자열로 표현된 실수 → 실수
# 3) 문자열로 표현된 정수 → 실수
# 4) 논리형 → 실수

# ✅ 가능한 경우
print(f"7 → {float(7)}")
print(f"'3.14' → {float('3.14')}")
print(f"'100' → {float('100')}")
print(f"True, False → {float(True)}, {float(False)}")

# ❌ 불가능한 경우
print(float("def"))
# 암시적 형변환
# 정수와 실수의 연산에서 자동으로 실수로 연산해줌
print(10 + 5.0)
# print("100" + 200)
# 3. 문자열로 변환 : str()
# 모든 타입을 문자열로 변환 가능
print(str(100), type(str(100)))
print(str(3.14), type(str(3.14)))
print(str(True), type(str(True)))
100 <class 'str'>
3.14 <class 'str'>
True <class 'str'>
# 4. 논리형으로 변환 : bool()
print(bool(1))
print(bool(0))
True
False
# 실습1. 영화 정보 출력하기
title, director, year, genre = "아이언맨", "놀란", 2008, "슈퍼히어로"

print(f"Title: {title}, Director: {director}, Year: {year}, Genre: {genre}")
print(f"제가 제일 좋아하는 영화는 {title}입니다")
Title: 아이언맨, Director: 놀란, Year: 2008, Genre: 슈퍼히어로
제가 제일 좋아하는 영화는 아이언맨입니다
# 실습2 자기소개 하기
이름, 나이, MBTI, 취미 = "ian", 15, "ENFJ", "책읽기"

print(f"""안녕하세요.
제 이름은 {이름}이고,
{나이}입니다.
제 MBTI는 {MBTI}에요.
취미는 {취미}랍니다. 
하하하""")
안녕하세요.
제 이름은 ian이고,
15입니다.
제 MBTI는 ENFJ에요.
취미는 책읽기랍니다. 
하하하