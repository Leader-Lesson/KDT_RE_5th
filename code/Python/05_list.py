# =========================================
# 05. 리스트 (List)
# - 여러 값들을 순서대로 저장할 수 있는 자료형
# - 인덱스(index): 각 값에 부여된 순서 번호 (0부터 시작)
# - 가변 자료형(mutable): 원소의 추가/수정/삭제 가능
# =========================================

# 리스트 만들기
내리스트1 = []  # 빈 리스트
내리스트2 = ["안녕하세요", "반갑습니다", "어서오세요"]
내리스트3 = [10, "아주좋아요", 3.14, [1, 2, 3, 4]]

# 리스트 생성 함수로 만들기
내리스트4 = list()
내리스트5 = list("CodingOn")
print(내리스트5)


# 인덱싱과 슬라이싱
my_list = [1, 2, 3, 4, 5]
my_list[0]
my_list[2]
my_list[1]
my_list[-1]
my_list[3] = 40
my_list[3]


# 문자열 인덱싱
my_str = "CodingOn"
my_str[2]
my_str[-2]

number = input("네 자릿수 정수를 입력하세요.: ")
천 = number[0]
백 = number[1]
십 = number[2]
일 = number[3]


# 슬라이싱(Slicing)
my_numbers = [10,20,30,40,50,60,70,80,90,100]
my_numbers[1:4]
my_numbers[3:]
sliced = my_numbers[:4]
my_numbers[1::2]
my_numbers[:]
my_numbers[::-1]
my_numbers[2:4] = [300,400]
my_numbers


# 실습1
nums = [10, 20, 30, 40, 50]
print("문제1", nums[0])
print("문제1", nums[-1])

nums = [100, 200, 300, 400, 500, 600, 700]
print("문제2", nums[2:5])

nums = [1, 2, 3, 4, 5]
nums[0] *= 2
nums[1] *= 2
nums[2] *= 2
nums[3] *= 2
nums[4] *= 2
print("문제3", nums)

items = ["a", "b", "c", "d", "e"]
print("문제4", items[::-1])

data = ["zero", "one", "two", "three", "four", "five"]
print("문제5", data[::2])

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print("문제6", movies)

subjects = ["국어","수학","영어","물리","화학","생물","역사","지구과학","윤리"]
print("문제7", subjects[3:8:2])

data = ["A","B","C","D","E","F","G","H","I"]
print("문제8")
print(data[0:3][::-1], end=" ")
print(data[3:6][::-1], end=" ")
print(data[6:9][::-1])


# 인덱스 범위 벗어남
my_list = [1,2,3,4]
# my_list[4]  # IndexError


# 슬라이싱 주의사항
my_list = [1,2,3,4,5]
print(my_list[4:1:2])
print(my_list[1:3:-1])


# 리스트 연산 - del
my_list = [10,20,30,40,50]
del my_list[2]
print(my_list)
del my_list[1:3]
print(my_list)
del my_list
# print(my_list)  # NameError


# 리스트 연결(+)
my_list1 = ["가","나","다"]
my_list2 = ["라","마","바"]
new_list = my_list1 + my_list2
print(my_list1, my_list2, new_list, sep=" / ")


# 리스트 반복(*)
my_list = ["금", "은", "동"]
new_list = my_list * 3
print(my_list, new_list, sep=" / ")


# 포함 여부 (in, not in)
fruits = ["토마토","사과","포도","수박","바나나"]
print("포도" in fruits)
print("참외" not in fruits)

if "참외" not in fruits:
  print("참외는 없어요")
else:
  print("참외 있어요")


# 실습2
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
result = fruits[:1] + fruits[1:]
print(result)

letters = ["A","B"]
new_letters = letters * 3
del new_letters[2]
print(new_letters)


# 리스트 주요 메서드
numbers = [1,2,3,4,5]
print("1. len()", len("CodingOn"), len(numbers))

numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers)

numbers.insert(2, 2.5)
numbers.insert(4, 3.5)
numbers.insert(0, 0)
numbers.insert(5, 2.5)
print("3. insert()", numbers)

numbers.remove(2.5)
numbers.remove(3.5)
print("4. remove()", numbers)

a = numbers.pop(4)
b = numbers.pop()
print("5. pop()", numbers)
print("삭제한 요소", a, b)

fruits = ["사과", "수박", "포도"]
fruits.extend(["배","참외"])
fruits.extend(("토마토","키위"))
fruits.extend("딸기")
print("6. extend()", fruits)


# 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()", numbers1)
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1)

numbers2 = [50, 52, 53, 51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True)
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc)


# 뒤집기
my_numbers = [100, 101, 102, 103, 104]
my_numbers.reverse()
print("8-1. reverse()", my_numbers)
my_numbers.reverse()
print("8-1. reverse()", my_numbers)

my_numbers2 = [11,12,13,14,15]
my_numbers2_rev = list(reversed(my_numbers2))
print("8-2. reversed()", my_numbers2, my_numbers2_rev)


# count, min, max, sum
numbers = [1,2,2,2,2,3,4,5,6,7]
print("9. count(2):", numbers.count(2))
numbers2 = [100,200,50,70,1000,40,20,250]
print("10. min/max:", min(numbers2), max(numbers2))
print("11. sum:", sum(numbers2))


# 실습3 - 기차 탑승 시뮬레이션
train = []
train.append("철수")
train.append("영희")
print("1.", train)

train.extend(["민수","지훈"])
print("2.", train)

train.remove("영희")
print("3.", train)

train.insert(1,"수진")
print("4.", train)

train.remove("민수")
train.reverse()
print("5.", train)


# 문제2 - 숫자 처리 게임
cards = [5,3,7]
cards.extend([4,9])
print("1.", cards)

print("2. 가장 큰 수:", max(cards))
print("2. 가장 작은 수:", min(cards))

print("3. 총합:", sum(cards))

cards.sort()
print("4. 제거한 숫자:", cards.pop())
print("5.", cards)
