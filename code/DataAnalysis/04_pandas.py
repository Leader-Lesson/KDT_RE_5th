import pandas as pd
import numpy as np

print(pd.__version__)

# 시리즈 생성
# 1. 리스트로 생성
data = [10,20,30,40]
s = pd.Series(data)
print(s)

# 2. 인덱스를 직접 지정
data = [10,20,30,40]
s = pd.Series(data, index=["a","b","c","d"])
print(s)

# 3. 딕셔너리로 생성
data = {"서울":100, "부산":200, "대구":300}
s = pd.Series(data)
print(s)

# 4. 하나의 값으로 시리즈 생성
s = pd.Series(7, index=["가","나","다"])
print(s)

# 시리즈의 주요 속성
data = [10,20,30,40]
s = pd.Series(data, index=["a","b","c","d"], name="test data")

print("values:", s.values)  # 실제 데이터 배열
print("index:", s.index)    # 인덱스 객체
print("dtype:", s.dtype)    # 실제 데이터의 타입
print("size:", s.size)      # 데이터의 개수
print("shape:", s.shape)    # 배열의 형태
print("name:", s.name)      # 시리즈의 이름

# 시리즈의 연산
s1 = pd.Series([10,20,30], index=["a","b","c"])
s2 = pd.Series([5,6,7], index=["b","c","d"])

result = s1 + s2
print(result)

# 정렬되지 않은 인덱스 간 연산
# 인덱스 기준로 연산후 정렬해줌
s1 = pd.Series([10,20,30], index=["b", "a", "c"])
s2 = pd.Series([5,6,7], index=["c","b","a"])

result = s1 + s2
print(result)

# 브로드 캐스팅
s = pd.Series([5,10,15], index=["a","b","c"])

print(s + 3)
print(s * 2)

# 불리언 연산 및 인덱싱
s = pd.Series([50,60,70,80,90,100], index=["a","b","c","d","e","f"])

# 불리언 연산(조건식)
mask = s > 70
print(mask)
print(s[mask])

# 시리즈와 NumPy 배열 연산 / 파이썬 리스트 연산
s = pd.Series([10,20,30], index=["a", "b", "c"])
a = np.array([1,2,3])
l = [100,200,300]

print(s + a)
print(s + l)

# 실습1.
# 문제1. 파이썬 리스트 [5, 10, 15, 20]을 이용해 Series를 생성하세요. 
data = [5, 10, 15, 20]
s = pd.Series(data)
print(s)

# 문제2. 값 [90, 80, 85, 70]에 대해
# 인덱스를 각각 '국어', '영어', '수학', '과학'으로 지정한 Series를 만드세요.
data = [90, 80, 85, 70]
idx = ['국어', '영어', '수학', '과학']
s = pd.Series(data, index=idx)
print(s)

# 문제3. {'서울': 950, '부산': 340, '인천': 520} 딕셔너리를 이용해 Series를 만들고,
# 인천의 값을 출력하세요.
data = {'서울': 950, '부산': 340, '인천': 520}
s = pd.Series(data)
print(s)
print(s["인천"])

# 문제4. Series [1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
data = [1, 2, 3, 4]
s = pd.Series(data)
print(s)
print(s.dtype)

# 문제5. 아래 두 Series의 합을 구하세요.
s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])


# 문제6. Series [1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
data = [1, 2, 3, 4, 5]
s = pd.Series(data)

print(s + 10)


# DataFrame 생성
# 1. 딕셔너리로 생성
data = {
  "이름" : ["이안","안태현","이민정"],
  "나이" : [15, 25, 23],
  "도시" : ["창동", "연신내", "응암"]
}

df = pd.DataFrame(data)
df

# 2. 리스트의 리스트(2차원 리스트)로 생성
data = [[1, "a"], [2, "b"], [3, "c"]]
df = pd.DataFrame(data, columns=["번호", "코드"])
df

# 3. 딕셔너리의 리스트로 생성
data = [
  {"이름":"이안","나이":15,"사는곳":"창동"},
  {"이름":"최하연","나이":25,"사는곳":"전주"},
  {"이름":"김진선","나이":26,"사는곳":"동탄"},
  {"이름":"오왕경","나이":25,"사는곳":"춘천"},
]

df = pd.DataFrame(data, index=["a","b","c","d"])
df

# 4. 시리즈의 딕셔너리로 생성
s1 = pd.Series(["국어","수학","영어"], index=["a","b","c"])
s2 = pd.Series([100,90,85], index=["a","b","c"])
df = pd.DataFrame({"과목": s1, "점수": s2})
df

# 데이터 프레임 기본 속성
data = [
  {"이름":"이안","나이":15,"사는곳":"창동"},
  {"이름":"최하연","나이":25,"사는곳":"전주"},
  {"이름":"김진선","나이":26,"사는곳":"동탄"},
  {"이름":"오왕경","나이":25,"사는곳":"춘천"},
]

df = pd.DataFrame(data)

print("shape:", df.shape)
print("columns:", df.columns)
print("index:", df.index)
print("dtypes:", df.dtypes)
print("values:", df.values)
print("info")
df.info()

# 실습2.
# 문제1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
data = [['홍길동', 28, '서울'],
        ['김철수', 33, '부산'],
        ['이영희', 25, '대구']] 
df = pd.DataFrame(data, columns=['이름', '나이', '도시'])
df

# 문제2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
df

# 문제3. 아래 데이터를 사용해 DataFrame을 만드세요.
data = [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
df = pd.DataFrame(data)
df

# 문제4. 아래 데이터를 사용해 DataFrame을 생성하되,
# 인덱스를 ['학생1', '학생2', '학생3']으로 지정하세요.
data = {'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]}

df = pd.DataFrame(data, index=['학생1', '학생2', '학생3'])
df

# 문제5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c']) 
data = {"국어": kor, "영어":eng}
df = pd.DataFrame(data)
df

# 문제6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
data = {'A': [1, 2], 'B': [3, 4]}

df = pd.DataFrame(data, columns=['B', 'A'])
df

# 문제7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
data = [['펜', 1000, 50],
        ['노트', 2000, 30]]
column_name = ['product', 'price', 'stock']
df = pd.DataFrame(data, columns=column_name)
df

# 문제8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
data = {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
df = pd.DataFrame(data)
df["국가"]

# 데이터 탐색과 요약
data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}
df = pd.DataFrame(data)
df

# 데이터 앞부분 미리 보기 : head(n)
# 기본값 n = 5
df.head()
df.head(3)

# 데이터 뒷부분 미리 보기 : tail(n)
# 기본값 n = 5
df.tail()
df.tail(2)

# info() 함수
df.info()

# describe() 함수
df.describe()                 # 기본적으로 수치형 컬럼만 요약
df.describe(include="object") # 문자열 컬럼만 요약
df.describe(include="all")    # 모든 컬럼 요약

# 인덱싱 : 컬럼에 대해 인덱싱 적용
# 특정 컬럼(시리즈) 선택
df["이름"]

# 여러 컬럼을 리스트로 선택
df[["이름", "나이"]]

df = pd.DataFrame({
    'name': ['Tom', 'Jane', 'Mike'],
    'age': [20, 25, 30]
})

df["name"]
# .으로도 조회가 가능함
# 변수명 규칙을 지켜야 함
df.name

# 슬라이싱
df[1:4]
df[-3:]

# 슬라이싱 후 인덱싱
df[1:4]["이름"]

# 슬라이싱은 행 기준으로 작동, 열 기준은 별도의 방법을 사용
df[:, 0:2] # 에러

# iloc 
# Interger Location
# 정수 위치 기반의 인덱싱, 슬라이싱
# NumPy의 슬라이싱과 유사함(거의 같음)!!!

# 단일 행/열 선택
df.iloc[0] # 첫번째 행
df.iloc[:, 1] # 두번째 열

# 여러 행/열 동시 선택
df.iloc[1:4]
df.iloc[:, 0:2]
df.iloc[1:4, 0:2]

# fancy indexing
df.iloc[[0,2,4]]
df.iloc[:,[1,2]]
df.iloc[[0,2,4],[1,2]]

# 음수 인덱스 슬라이싱
df.iloc[-1]
df.iloc[:,-2:]

# loc
# location의 약자
# 라벨의 이름 기준으로 인덱싱/슬라이싱
# 단일 행/열 선택
# 시작과 끝을 모두 포함
# 음수 인덱스 사용X
df.loc[0]
df.loc[:,"이름"]

# 여러 행/열 선택
df.loc[2:4, ["이름","직업"]]
df.loc[2:4, "이름":"직업"]

# 조건식
mask = df["나이"] >= 30
df.loc[mask, ["이름","나이"]]

# 컬럼을 인덱스로 지정
df2 = df.set_index("이름")
df2

# df2.loc["이순신"]
# df2.loc[["이순신","강감찬","장보고"]]

s1 = pd.Series(["국어","수학","영어"], index=["a","b","c"])
s2 = pd.Series([100,90,85], index=["a","b","c"])
df = pd.DataFrame({"과목": s1, "점수": s2})
df

# 행에 라벨이 있을 경우 라벨을 이용해서 인덱싱/슬라이싱 가능
df.loc[["a","c"],["과목"]]

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원", "최무선", "정도전"],
    "나이": [23, 35, 31, 40, 28, 34, 42, 29],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자", "과학자", "정치가"],
    "점수": [85, 90, 75, 88, 92, 95, 87, 83]
}
df = pd.DataFrame(data)
df

# 실습3.
# 문제1. iloc을 사용해 인덱스 2~5(포함 안함) 행, 1~3(포함 안함) 열만 선택해 출력하세요.
df.iloc[2:5, 1:3]

# 문제2. loc을 사용해 인덱스 3~6(포함!) 행, '이름'과 '점수' 컬럼만 출력하세요.
df.loc[3:6, ["이름","점수"]]

# 문제3. iloc을 사용해, 마지막 3개 행의 '직업'과 '점수' 컬럼만 선택해 출력하세요.
df.iloc[-3:,-2:]
df.loc[5:,["직업","점수"]]

# 문제4. iloc을 사용해, 홀수번째(1, 3, 5, 7번 인덱스) 행, 모든 열을 선택하세요.
df.iloc[[1,3,5,7]]

# 문제5. loc을 사용해, 인덱스 4~7번 행, '나이', '점수' 컬럼만 출력하세요.
df.loc[4:7, ["나이","점수"]]

# 문제6. iloc을 사용해, 짝수번째(0,2,4,6) 행과 짝수번째(0,2) 열만 선택하세요.
df.iloc[[0,2,4,6],[0,2]]

data = {
    "상품명": ["무선 이어폰", "스마트 워치", "텀블러", "노트북", "블루투스 스피커", "무드등"],
    "가격": [129000, 250000, 15000, 1200000, 85000, 22000],
    "재고": [23, 12, 54, 5, 17, 31]
}
df = pd.DataFrame(data)
df

df.describe(include="all")
# df["가격"].describe()

# 평균
df["가격"].mean()

# 중앙값
df["재고"].median()

# 표준편차
df["가격"].std()

# 분산
df["재고"].var()

# 값의 개수
df["상품명"].count()

# 최대값
df["가격"].max()

# 최소값
df["재고"].min()

# 합계
df["가격"].sum()

# 최대값의 위치와 최소값의 위치
df.idxmax()
df["재고"].idxmax()

df.idxmin()
df["가격"].idxmin()

data = {
    "이름": ["서준", "하은", "민준", "서연", "이안", "지민"],
    "나이": [22, 28, np.nan, 31, 27, 24],
    "점수": [89, np.nan, 83, 90, 88, 93]
}
df = pd.DataFrame(data)
df

# 결측값 탐지
# isnull 결측값이 맞으면 True 아니면 False
df.isnull()

# 각 컬럼의 결측값의 수 계산
df.isnull().sum()

# 데이터의 전체 결측값 수 계산
df.isnull().sum().sum()

# notnull 결측값이 아니면 True, 맞으면 False
df.notnull()

# dropna 결측값이 있는 행 삭제
df2 = df.dropna()
df2

# 결측값이 있는 열 삭제
df3 = df.dropna(axis=1)
df3

# fillna 결측값을 0으로 대체
df4 = df.fillna(0)
df4

avg_age = df["나이"].mean()
df["나이"] = df["나이"].fillna(avg_age)
df

# 이전 값으로 결측값 채우기(forward fill)
df5 = df.fillna(method="ffill")
df5

# 뒤의 값으로 결측값 채우기(backward fill)
df6 = df.fillna(method="bfill")
df6

# 실습4.
data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)
df

# 문제1. ‘미세먼지’ 컬럼의 평균과 중앙값을 구하세요.
print(df["미세먼지"].mean())
print(df["미세먼지"].median())

# 문제2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요.
print(df["초미세먼지"].max())
print(df["초미세먼지"].min())

# 문제3. 각 컬럼별 결측값 개수를 구하세요.
df.isnull().sum()

# 문제4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
df2 = df.dropna()
print(df2)
df2["초미세먼지"].mean()

# 문제5. 결측값을 모두 0으로 채운 뒤, ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
df3 = df.fillna(0)
print(df["미세먼지"].sum())
print(df["초미세먼지"].sum())

# 문제6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
fd_mean = df["미세먼지"].mean()

# 원본을 변경시키지 않는 복사본
df4 = df.copy()
df4["미세먼지"] = df["미세먼지"].fillna(fd_mean)
df4["미세먼지"].std()