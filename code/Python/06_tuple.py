# =========================================
# 06. 튜플(Tuple)
# - 순서가 존재하는 여러 데이터의 모음
# - 불변(immutable) 자료형
# =========================================


# -------------------------------
# 튜플 생성
# -------------------------------
my_tuple = (1, 2, 3, 4)
print(my_tuple)

# 소괄호 없이 튜플 생성
no_paren_tuple = 5, 6, 7, 8
print(no_paren_tuple, type(no_paren_tuple))

# 원소가 하나인 튜플 생성
single_el_tuple = (100,)  # 콤마를 반드시 붙여야 함
print(single_el_tuple, type(single_el_tuple))

# 튜플 생성 함수로 생성
my_tuple2 = tuple()
print(my_tuple2)

my_tuple3 = tuple("CodingOn")  # 문자열을 튜플로 변환
print(my_tuple3)


# -------------------------------
# 언패킹(Unpacking)
# 시퀀스에 저장된 여러 값을 여러 변수에 나누어 저장하는 것
# 구조 분해 할당(Destructuring)
# -------------------------------
과일1, 과일2, 과일3 = "사과", "수박", "참외"
운동1, 운동2, 운동3 = ["축구", "농구", "야구"]
문, 자, 열 = "코딩온"

print(문)
print(자)
print(열)


# -------------------------------
# 튜플의 불변성 
# 불변성 : 객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
# -------------------------------
my_tuple = (1, 2, 3)
# 아래 코드는 오류 발생 (TypeError)
# my_tuple[0] = 100


# -------------------------------
# 튜플 삭제 시도
# -------------------------------
# del my_tuple[1]  # TypeError 발생


# -------------------------------
# 튜플의 수정 (새 튜플로 대체)
# -------------------------------
my_tuple2 = (10, 20, 30)
new_tuple = (100,) + my_tuple2[1:]
print("원본 튜플", my_tuple2)
print("새로운 튜플", new_tuple)


# -------------------------------
# 튜플의 삭제
# 튜플의 원소는 삭제할 수 X, 튜플 자체는 삭제 가능
# -------------------------------
# del my_tuple 
# print(my_tuple)  # NameError 발생


# =========================================
# 실습 1.
# =========================================
# Step 1. 해킹된 고객 이름 복구하기
# 기존 튜플은 ("minji", 25, "Seoul")
# 이름을 "eunji"로 변경한 새 튜플을 만들어 변수 restored_user에 저장하세요.

user = ("minji", 25, "Seoul")

# 튜플은 수정 불가이므로, 슬라이싱과 결합을 사용해 새 튜플 생성
restored_user = ("eunji",) + user[1:]

# Step 2. 언패킹
# 복원된 튜플을 name, age, city로 언패킹하고 각각 출력해보세요.
name, age, city = restored_user

# Step 3. 지역에 따라 보안 메시지 다르게 출력
# city가 "Seoul"이면 "※ 서울 지역 보안 정책 적용 대상입니다."
# 아니라면 "※ 일반 지역 보안 정책 적용 대상입니다."
if city == "Seoul":
    print("※ 서울 지역 보안 정책 적용 대상입니다.")
else:
    print("※ 일반 지역 보안 정책 적용 대상입니다.")

# Step 4. 고객 데이터 분석
# 아래 튜플에서 "minji"가 몇 번 등장하는지 count()로 구하고
# "soojin"이 처음 등장하는 인덱스를 index()로 구하세요.
users = ("minji", "eunji", "soojin", "minji", "minji")

count_minji = users.count("minji")
index_soojin = users.index("soojin")

# Step 5. 고객 리스트 정렬 (튜플은 변경하지 말고 sorted()로 리스트 형태로 출력)
sorted_users = sorted(users)

# 🔽 출력 결과 확인
print("복원된 고객 정보:", restored_user)
print(f"{name}님의 나이는 {age}세이며, 거주 도시는 {city}입니다.")
print(f"'minji'는 {count_minji}번 등장합니다.")
print(f"'soojin'은 {index_soojin}번 인덱스에 있습니다.")
print("정렬된 고객 리스트:", sorted_users)