import pandas as pd
import numpy as np

print(pd.__version__)  # 예: '2.2.5' (환경에 따라 다름)

# 시리즈 생성
# 1. 리스트로 생성
data = [10,20,30,40]
s = pd.Series(data)
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 2. 인덱스를 직접 지정
data = [10,20,30,40]
s = pd.Series(data, index=["a","b","c","d"])
print(s)
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# 3. 딕셔너리로 생성
data = {"서울":100, "부산":200, "대구":300}
s = pd.Series(data)
print(s)
# 서울    100
# 부산    200
# 대구    300
# dtype: int64

# 4. 하나의 값으로 시리즈 생성
s = pd.Series(7, index=["가","나","다"])
print(s)
# 가    7
# 나    7
# 다    7
# dtype: int64

# 시리즈의 주요 속성
data = [10,20,30,40]
s = pd.Series(data, index=["a","b","c","d"], name="test data")

print("values:", s.values)  # 실제 데이터 배열 -> values: [10 20 30 40]
print("index:", s.index)    # 인덱스 객체 -> index: Index(['a','b','c','d'], dtype='object')
print("dtype:", s.dtype)    # 실제 데이터의 타입 -> dtype: int64 (환경에 따라 다름)
print("size:", s.size)      # 데이터의 개수 -> size: 4
print("shape:", s.shape)    # 배열의 형태 -> shape: (4,)
print("name:", s.name)      # 시리즈의 이름 -> name: test data

# 시리즈의 연산
s1 = pd.Series([10,20,30], index=["a","b","c"])
s2 = pd.Series([5,6,7], index=["b","c","d"])

result = s1 + s2
print(result)
# a     NaN
# b    25.0
# c    36.0
# d     NaN
# dtype: float64

# 정렬되지 않은 인덱스 간 연산
# 인덱스 기준로 연산후 정렬해줌
s1 = pd.Series([10,20,30], index=["b", "a", "c"])
s2 = pd.Series([5,6,7], index=["c","b","a"])

result = s1 + s2
print(result)
# a    26.0
# b    15.0
# c    37.0
# dtype: float64

# 브로드 캐스팅
s = pd.Series([5,10,15], index=["a","b","c"])

print(s + 3)
# a     8
# b    13
# c    18
# dtype: int64
print(s * 2)
# a     10
# b     20
# c     30
# dtype: int64

# 불리언 연산 및 인덱싱
s = pd.Series([50,60,70,80,90,100], index=["a","b","c","d","e","f"])

# 불리언 연산(조건식)
mask = s > 70
print(mask)
# a    False
# b    False
# c    False
# d     True
# e     True
# f     True
# dtype: bool
print(s[mask])
# d     80
# e     90
# f    100
# dtype: int64

# 시리즈와 NumPy 배열 연산 / 파이썬 리스트 연산
s = pd.Series([10,20,30], index=["a", "b", "c"])
a = np.array([1,2,3])
l = [100,200,300]

print(s + a)
# a    11
# b    22
# c    33
# dtype: int64
print(s + l)
# a    110
# b    220
# c    330
# dtype: int64

# 실습1.
# 문제1. 파이썬 리스트 [5, 10, 15, 20]을 이용해 Series를 생성하세요. 
data = [5, 10, 15, 20]
s = pd.Series(data)
print(s)
# 0     5
# 1    10
# 2    15
# 3    20
# dtype: int64

# 문제2. 값 [90, 80, 85, 70]에 대해
# 인덱스를 각각 '국어', '영어', '수학', '과학'으로 지정한 Series를 만드세요.
data = [90, 80, 85, 70]
idx = ['국어', '영어', '수학', '과학']
s = pd.Series(data, index=idx)
print(s)
# 국어    90
# 영어    80
# 수학    85
# 과학    70
# dtype: int64

# 문제3. {'서울': 950, '부산': 340, '인천': 520} 딕셔너리를 이용해 Series를 만들고,
# 인천의 값을 출력하세요.
data = {'서울': 950, '부산': 340, '인천': 520}
s = pd.Series(data)
print(s)
# 서울    950
# 부산    340
# 인천    520
# dtype: int64
print(s["인천"])  # 520

# 문제4. Series [1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
data = [1, 2, 3, 4]
s = pd.Series(data)
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
print(s.dtype)  # int64 (환경에 따라 다름)

# 문제5. 아래 두 Series의 합을 구하세요.
s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
# 연산 결과 (주석으로 출력)
print(s1 + s2)
# a     NaN
# b    15.0
# c    27.0
# d     NaN
# dtype: float64

# 문제6. Series [1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
data = [1, 2, 3, 4, 5]
s = pd.Series(data)

print(s + 10)
# 0    11
# 1    12
# 2    13
# 3    14
# 4    15
# dtype: int64


# DataFrame 생성
# 1. 딕셔너리로 생성
data = {
  "이름" : ["이안","안태현","이민정"],
  "나이" : [15, 25, 23],
  "도시" : ["창동", "연신내", "응암"]
}

df = pd.DataFrame(data)
df
print(df)
#     이름   나이    도시
# 0   이안   15    창동
# 1  안태현   25   연신내
# 2  이민정   23    응암

# 2. 리스트의 리스트(2차원 리스트)로 생성
data = [[1, "a"], [2, "b"], [3, "c"]]
df = pd.DataFrame(data, columns=["번호", "코드"])
df
print(df)
#    번호 코드
# 0   1  a
# 1   2  b
# 2   3  c

# 3. 딕셔너리의 리스트로 생성
data = [
  {"이름":"이안","나이":15,"사는곳":"창동"},
  {"이름":"최하연","나이":25,"사는곳":"전주"},
  {"이름":"김진선","나이":26,"사는곳":"동탄"},
  {"이름":"오왕경","나이":25,"사는곳":"춘천"},
]

df = pd.DataFrame(data, index=["a","b","c","d"])
df
print(df)
#       이름  나이   사는곳
# a    이안  15    창동
# b   최하연  25    전주
# c   김진선  26    동탄
# d   오왕경  25    춘천

# 4. 시리즈의 딕셔너리로 생성
s1 = pd.Series(["국어","수학","영어"], index=["a","b","c"])
s2 = pd.Series([100,90,85], index=["a","b","c"])
df = pd.DataFrame({"과목": s1, "점수": s2})
print(df)
#    과목  점수
# a  국어  100
# b  수학   90
# c  영어   85

# 데이터 프레임 기본 속성
data = [
  {"이름":"이안","나이":15,"사는곳":"창동"},
  {"이름":"최하연","나이":25,"사는곳":"전주"},
  {"이름":"김진선","나이":26,"사는곳":"동탄"},
  {"이름":"오왕경","나이":25,"사는곳":"춘천"},
]

df = pd.DataFrame(data)

print("shape:", df.shape)    # shape: (4, 3)
print("columns:", df.columns) # columns: Index(['이름','나이','사는곳'], dtype='object')
print("index:", df.index)    # index: RangeIndex(start=0, stop=4, step=1)
print("dtypes:", df.dtypes)  # dtypes: 이름    object; 나이    int64; 사는곳    object
print("values:", df.values)  # values: ndarray (rows x cols)
print("info")
df.info()  # 출력은 DataFrame 구조와 메모리 정보 등

# 실습2.
# 문제1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
data = [['홍길동', 28, '서울'],
        ['김철수', 33, '부산'],
        ['이영희', 25, '대구']] 
df = pd.DataFrame(data, columns=['이름', '나이', '도시'])
df
print(df)
#    이름   나이  도시
# 0  홍길동  28  서울
# 1  김철수  33  부산
# 2  이영희  25  대구

# 문제2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6

# 문제3. 아래 데이터를 사용해 DataFrame을 만드세요.
data = [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
df = pd.DataFrame(data)
print(df)
#    과목  점수
# 0  수학  90
# 1  영어  85
# 2  과학  95

# 문제4. 아래 데이터를 사용해 DataFrame을 생성하되,
# 인덱스를 ['학생1', '학생2', '학생3']으로 지정하세요.
data = {'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]}

df = pd.DataFrame(data, index=['학생1', '학생2', '학생3'])
print(df)
#         이름  점수
# 학생1   민수  80
# 학생2   영희  92
# 학생3   철수  77

# 문제5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c']) 
data = {"국어": kor, "영어":eng}
df = pd.DataFrame(data)
print(df)
#    국어  영어
# a  90  95
# b  85  88
# c  80  82

# 문제6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
data = {'A': [1, 2], 'B': [3, 4]}

df = pd.DataFrame(data, columns=['B', 'A'])
print(df)
#    B  A
# 0  3  1
# 1  4  2

# 문제7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
data = [['펜', 1000, 50],
        ['노트', 2000, 30]]
column_name = ['product', 'price', 'stock']
df = pd.DataFrame(data, columns=column_name)
print(df)
#   product  price  stock
# 0     펜   1000     50
# 1    노트   2000     30

# 문제8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
data = {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
df = pd.DataFrame(data)
print(df["국가"])
# 0    한국
# 1    일본
# 2    미국
# Name: 국가, dtype: object

# 데이터 탐색과 요약
data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}
df = pd.DataFrame(data)
print(df.head(3))
#    이름  나이   직업
# 0  홍길동  23   학생
# 1  이순신  35   군인
# 2  김유신  31   장군

print(df.tail(2))
#     이름  나이   직업
# 4  장보고  28   상인
# 5  이방원  34   왕자

# info() 함수
df.info()  # 출력: 데이터프레임 정보(컬럼, non-null count, dtype 등)

# describe() 함수
print(df.describe())                 # 수치형 컬럼 요약 (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe(include="object")) # 문자열 컬럼 요약
print(df.describe(include="all"))    # 모든 컬럼 요약

# 인덱싱 : 컬럼에 대해 인덱싱 적용
# 특정 컬럼(시리즈) 선택
print(df["이름"])
# 0    홍길동
# 1    이순신
# 2    김유신
# 3    강감찬
# 4    장보고
# 5    이방원
# Name: 이름, dtype: object

# 여러 컬럼을 리스트로 선택
print(df[["이름", "나이"]])
#     이름  나이
# 0  홍길동  23
# 1  이순신  35
# 2  김유신  31
# 3  강감찬  40
# 4  장보고  28
# 5  이방원  34

df = pd.DataFrame({
    'name': ['Tom', 'Jane', 'Mike'],
    'age': [20, 25, 30]
})

print(df["name"])
# 0    Tom
# 1    Jane
# 2    Mike
# Name: name, dtype: object

# .으로도 조회가 가능함
print(df.name)
# 0    Tom
# 1    Jane
# 2    Mike
# Name: name, dtype: object

# 슬라이싱
print(df[1:4])
#    name  age
# 1  Jane   25
# 2  Mike   30

print(df[-3:])
#    name  age
# 0   Tom   20
# 1  Jane   25
# 2  Mike   30

# 슬라이싱 후 인덱싱
print(df[1:4]["name"])
# 1    Jane
# 2    Mike
# Name: name, dtype: object

# iloc 
# Interger Location
# 정수 위치 기반의 인덱싱, 슬라이싱
# NumPy의 슬라이싱과 유사함(거의 같음)!!!

# 단일 행/열 선택
print(df.iloc[0]) # 첫번째 행
# name    Tom
# age      20
# Name: 0, dtype: object
print(df.iloc[:, 1]) # 두번째 열
# 0    20
# 1    25
# 2    30
# Name: age, dtype: int64

# 여러 행/열 동시 선택
print(df.iloc[1:4])
#    name  age
# 1  Jane   25
# 2  Mike   30

print(df.iloc[:, 0:2])
#    name  age
# 0   Tom   20
# 1  Jane   25
# 2  Mike   30

print(df.iloc[1:4, 0:2])
#    name  age
# 1  Jane   25
# 2  Mike   30

# fancy indexing
print(df.iloc[[0,2,]]) 
#    name  age
# 0   Tom   20
# 2  Mike   30

print(df.iloc[:,[1]]) 
#    age
# 0   20
# 1   25
# 2   30

# 음수 인덱스 슬라이싱
print(df.iloc[-1])
# name    Mike
# age       30
# Name: 2, dtype: object
print(df.iloc[:,-1:])
#    age
# 0   20
# 1   25
# 2   30

# loc
# location의 약자
# 라벨의 이름 기준으로 인덱싱/슬라이싱
# 단일 행/열 선택
# 시작과 끝을 모두 포함
# 음수 인덱스 사용X
print(df.loc[0])
# name    Tom
# age      20
# Name: 0, dtype: object
print(df.loc[:,"name"])
# 0     Tom
# 1    Jane
# 2    Mike
# Name: name, dtype: object

# 여러 행/열 선택
print(df.loc[0:1, ["name"]])
#    name
# 0   Tom
# 1  Jane

# 조건식
mask = df["age"] >= 25
print(df.loc[mask, ["name","age"]])
#    name  age
# 1  Jane   25
# 2  Mike   30

# 컬럼을 인덱스로 지정
df2 = df.set_index("name")
print(df2)
#       age
# name     
# Tom    20
# Jane   25
# Mike   30

# df2.loc["Tom"]
# df2.loc[["Tom","Mike"]]

s1 = pd.Series(["국어","수학","영어"], index=["a","b","c"])
s2 = pd.Series([100,90,85], index=["a","b","c"])
df = pd.DataFrame({"과목": s1, "점수": s2})
print(df)
#    과목  점수
# a  국어  100
# b  수학   90
# c  영어   85

# 행에 라벨이 있을 경우 라벨을 이용해서 인덱싱/슬라이싱 가능
print(df.loc[["a","c"],["과목"]])
#    과목
# a  국어
# c  영어

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원", "최무선", "정도전"],
    "나이": [23, 35, 31, 40, 28, 34, 42, 29],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자", "과학자", "정치가"],
    "점수": [85, 90, 75, 88, 92, 95, 87, 83]
}
df = pd.DataFrame(data)
print(df.head(3))
#     이름  나이   직업  점수
# 0  홍길동  23   학생  85
# 1  이순신  35   군인  90
# 2  김유신  31   장군  75

# 실습3.
# 문제1. iloc을 사용해 인덱스 2~5(포함 안함) 행, 1~3(포함 안함) 열만 선택해 출력하세요.
print(df.iloc[2:5, 1:3])
#    직업  점수
# 2  장군  75
# 3  장군  88
# 4  상인  92

# 문제2. loc을 사용해 인덱스 3~6(포함!) 행, '이름'과 '점수' 컬럼만 출력하세요.
print(df.loc[3:6, ["이름","점수"]])
#      이름  점수
# 3  강감찬  88
# 4  장보고  92
# 5  이방원  95
# 6  최무선  87

# 문제3. iloc을 사용해, 마지막 3개 행의 '직업'과 '점수' 컬럼만 선택해 출력하세요.
print(df.iloc[-3:,-2:])
#        직업  점수
# 5     왕자  95
# 6    과학자  87
# 7    정치가  83

print(df.loc[5:,["직업","점수"]])
#        직업  점수
# 5     왕자  95
# 6    과학자  87
# 7    정치가  83

# 문제4. iloc을 사용해, 홀수번째(1, 3, 5, 7번 인덱스) 행, 모든 열을 선택하세요.
print(df.iloc[[1,3,5,7]])
#     이름  나이   직업  점수
# 1  이순신  35   군인  90
# 3  강감찬  40   장군  88
# 5  이방원  34   왕자  95
# 7  정도전  29  정치가  83

# 문제5. loc을 사용해, 인덱스 4~7번 행, '나이', '점수' 컬럼만 출력하세요.
print(df.loc[4:7, ["나이","점수"]])
#    나이  점수
# 4  28  92
# 5  34  95
# 6  42  87
# 7  29  83

# 문제6. iloc을 사용해, 짝수번째(0,2,4,6) 행과 짝수번째(0,2) 열만 선택하세요.
print(df.iloc[[0,2,4,6],[0,2]])
#      이름   직업
# 0  홍길동   학생
# 2  김유신   장군
# 4  장보고   상인
# 6  최무선  과학자

data = {
    "상품명": ["무선 이어폰", "스마트 워치", "텀블러", "노트북", "블루투스 스피커", "무드등"],
    "가격": [129000, 250000, 15000, 1200000, 85000, 22000],
    "재고": [23, 12, 54, 5, 17, 31]
}
df = pd.DataFrame(data)
print(df)
#          상품명      가격  재고
# 0    무선 이어폰  129000  23
# 1    스마트 워치  250000  12
# 2        텀블러   15000  54
# 3       노트북 1200000   5
# 4  블루투스 스피커   85000  17
# 5        무드등   22000  31

print(df.describe(include="all"))  # 요약 통계 출력

# 평균
print(df["가격"].mean())  # 예: 평균값 (숫자)

# 중앙값
print(df["재고"].median())  # 예: 중앙값 (숫자)

# 표준편차
print(df["가격"].std())  # 예: 표준편차 (숫자)

# 분산
print(df["재고"].var())  # 예: 분산 (숫자)

# 값의 개수
print(df["상품명"].count())  # 6

# 최대값
print(df["가격"].max())  # 1200000

# 최소값
print(df["재고"].min())  # 5

# 합계
print(df["가격"].sum())  # 가격 합계 (숫자)

# 최대값의 위치와 최소값의 위치
print(df.idxmax())       # 각 컬럼의 최대값 인덱스
print(df["재고"].idxmax()) # 재고 최대값 인덱스 (예: 2)

print(df.idxmin())       # 각 컬럼의 최소값 인덱스
print(df["가격"].idxmin()) # 가격 최소값 인덱스 (예: 2)

data = {
    "이름": ["서준", "하은", "민준", "서연", "이안", "지민"],
    "나이": [22, 28, np.nan, 31, 27, 24],
    "점수": [89, np.nan, 83, 90, 88, 93]
}
df = pd.DataFrame(data)
print(df)
#     이름    나이    점수
# 0  서준  22.0  89.0
# 1  하은  28.0   NaN
# 2  민준   NaN  83.0
# 3  서연  31.0  90.0
# 4  이안  27.0  88.0
# 5  지민  24.0  93.0

# 결측값 탐지
print(df.isnull())
# 출력: True/False 데이터프레임

# 각 컬럼의 결측값의 수 계산
print(df.isnull().sum())
# 나이    1
# 점수    1
# dtype: int64

# 데이터의 전체 결측값 수 계산
print(df.isnull().sum().sum())
# 2

# notnull 결측값이 아니면 True, 맞으면 False
print(df.notnull())
# 출력: True/False 데이터프레임

# dropna 결측값이 있는 행 삭제
df2 = df.dropna()
print(df2)
# 남은 행들 (결측값 없는 행만)

# 결측값이 있는 열 삭제
df3 = df.dropna(axis=1)
print(df3)
# 결측값이 있는 열이 제거된 데이터프레임

# fillna 결측값을 0으로 대체
df4 = df.fillna(0)
print(df4)
# 결측값이 0으로 채워진 데이터프레임

avg_age = df["나이"].mean()
df["나이"] = df["나이"].fillna(avg_age)
print(df)
# 나이 결측값이 평균으로 채워진 데이터프레임

# 이전 값으로 결측값 채우기(forward fill)
df5 = df.fillna(method="ffill")
print(df5)
# 결측값이 앞값으로 채워진 결과

# 뒤의 값으로 결측값 채우기(backward fill)
df6 = df.fillna(method="bfill")
print(df6)
# 결측값이 뒷값으로 채워진 결과

# 실습4.
data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)
print(df)
#      도시   미세먼지  초미세먼지   강수량
# 0    서울   45.0   20.0   0.0
# 1    부산   51.0    NaN   2.5
# 2    광주    NaN   17.0   1.0
# 3    대구   38.0   18.0   NaN
# 4    NaN   49.0   22.0   3.1
# 5    춘천    NaN   19.0   0.0

# 문제1. ‘미세먼지’ 컬럼의 평균과 중앙값을 구하세요.
print(df["미세먼지"].mean())   # 예: 평균값 (NaN 제외)
print(df["미세먼지"].median()) # 예: 중앙값

# 문제2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요.
print(df["초미세먼지"].max()) # 22.0
print(df["초미세먼지"].min()) # 17.0

# 문제3. 각 컬럼별 결측값 개수를 구하세요.
print(df.isnull().sum())
# 도시       1
# 미세먼지    2
# 초미세먼지  1
# 강수량     1
# dtype: int64

# 문제4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
df2 = df.dropna()
print(df2)
# 결측값 없는 행들(예시: 인덱스 0,2 등)
print(df2["초미세먼지"].mean())  # 평균값 (df2 기준)

# 문제5. 결측값을 모두 0으로 채운 뒤, ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
df3 = df.fillna(0)
print(df3["미세먼지"].sum())    # 합계 (예시 숫자)
print(df3["초미세먼지"].sum())  # 합계 (예시 숫자)

# 문제6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
fd_mean = df["미세먼지"].mean()

# 원본을 변경시키지 않는 복사본
df4 = df.copy()
df4["미세먼지"] = df["미세먼지"].fillna(fd_mean)
print(df4["미세먼지"].std())  # 표준편차 (숫자)