import pandas as pd
import numpy as np

data = {
    '이름': ['홍길동', '김철수', '이영희', '박민수'],
    '점수': [90, 70, 95, 95],
    '반': [2, 1, 1, 2]
}
df = pd.DataFrame(data)
df

mask = df["점수"] >= 80
filtered = df[mask]
filtered

# 여러조건 결합
# and : &
# or : |
# not : ~

# & 예시
df[(df["반"] == 1) & (df["점수"] >= 80)]

# | 예시
mask = (df["반"] == 2) | (df["점수"] >= 90)
df[mask]

# isin()
# 여러 값 중에 하나에 해당하는지 여부를 판단할 때 사용

# mask = (df["이름"] == "홍길동") | (df["이름"] == "박민수") | (df["이름"] == "이영희") 
mask = df["이름"].isin(["홍길동", "박민수"])
df[mask]

# not 사용 예시
mask = ~df["이름"].isin(["홍길동", "박민수"])
df[mask]

# reset_index
# 조건 필터링, 행 삭제 등을 통해 인덱스가 변경됐을시
# reset_index를 사용해서 인덱스를 초기화
mask = (df["반"] == 2) | (df["점수"] >= 90)
df2 = df[mask]
print(df2)

# 인덱스 리셋
# df2 = df2.reset_index()
# print(df2)

# 기존 인덱스 삭제
df2 = df2.reset_index(drop=True)
print(df2)

# 실습1.
df = pd.DataFrame({
    '이름': ['민준', '서연', '지후', '서준', '지민'],
    '점수': [78, 92, 85, 60, 88],
    '반': [1, 2, 1, 2, 1]
})
df

# 문제1. 점수(score)가 80점 이상인 학생만 추출하세요.
mask = df["점수"] >= 80
df[mask]

# 문제2. 1반(반==1) 학생들 중, 점수가 85점 이상인 학생만 추출하세요.
mask = (df["반"] == 1) & (df["점수"] >= 85)
df[mask]

# 문제3. 이름이 '서연' 또는 '지민'인 학생만 추출하세요.
# mask = (df["이름"] == "서연") | (df["이름"] == "지민")
mask = df["이름"].isin(["서연", "지민"])
df3 = df[mask]
df3

# 문제4. 문제 3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력하세요.
df4 = df3.reset_index(drop=True)
df4

# 문제5. 점수가 80점 미만이거나 2반인 학생만 추출하세요.
mask = (df["점수"] < 80) | (df["반"] == 2)
df5 = df[mask]
df5

# 문제6. 문제 5의 결과에서 '점수' 컬럼이 70점 이상인 학생만 다시 추출하고,
# 인덱스를 재정렬하여 출력하세요.
mask = df5["점수"] >= 70
df6 = df5[mask].reset_index(drop=True)
df6

# 열 추가 및 수정
# df["컬럼명"] = "값"
# 컬럼이 존재하면 수정 / 컬럼이 존재하지 않으면 추가
df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '국어': [90, 80, 70],
    '영어': [85, 78, 92]
})
df

# 같은 값을 한번에 추가
df["반"] = "1반"
df

# 조건문을 통한 추가
df["국어_합격여부"] = df["국어"] >= 80
df

# 리스트/시리즈를 통한 열 추가
df["학번"] = [101, 102, 103]
df

# 시리즈의 연산 결과로 새 열 추가
df["총점"] = df["국어"] + df["영어"]
df

# 기존 값을 한번에 변경
df["영어"] = 100
df

# 새로운 컬럼 추가시, 행의 개수가 맞지 않으면 에러 발생!
df["새로운열"] = [1,2]

# 열 삭제: drop
# 단일 열 삭제
df2 = df.drop("반", axis=1)
df2

# 여러 열 삭제
df3 = df2.drop(["총점","국어_합격여부"], axis=1)
df3

# 원본에서 삭제
df.drop("반", axis=1, inplace=True)
df

# 기타 삭제 방법(1)
del df["총점"]
df

# 기타 삭제 방법(2)
deleted = df.pop("국어_합격여부")
deleted

df = pd.DataFrame({
    '이름': ['김철수', '이영희'],
    '나이': [23, 25]
})
df

# 행추가 : concat
# 새 행을 추가하기
new_row = pd.DataFrame([{"이름": "이안", "나이":25}])

# df = pd.concat([df, new_row])

# 인덱스 재정렬
df = pd.concat([df, new_row], ignore_index=True)
df

# 여러 행 추가하기
new_rows = pd.DataFrame([{"이름": "안태현", "나이":25},
                        {"이름": "이민정", "나이":25}])
df = pd.concat([df, new_rows], ignore_index=True)
df

# 행 수정
# loc, iloc을 활용
df.loc[1] = ["김영희", 35]
df

df.loc[0, "나이"] = 18
df

df.loc[1:3, "나이"] = 15
df

df.loc[1:2, ["이름","나이"]] = [["최하연", 25], ["오왕경",25]]
df

# 행 삭제 : drop
# axis 기본값 0
# 단일 행 삭제
df2 = df.drop(1).reset_index(drop=True)
df2

# 여러 행 삭제
df3 = df.drop([0,2])
df3

df = df[df["나이"] >= 20]
df

# 실습2.
df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '국어': [90, 80, 70]
})
# 문제1. '수학' 점수 [95, 100, 88]을 새 열로 추가하세요.
df["수학"] = [95,100,88]

# 문제2. 1번 문제의 DataFrame에서 '이름' 열을 삭제하세요.
df.drop("이름", axis=1, inplace=True)
df

df = pd.DataFrame({
    '제품': ['A', 'B'],
    '가격': [1000, 2000]
})
# 문제3. 제품 'C', 가격 1500인 새 행을 추가하세요.
new_row = pd.DataFrame([{"제품":"C", "가격":1500}])
df = pd.concat([df, new_row], ignore_index=True)

# 문제4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
df = df.drop(0).reset_index(drop=True)
df

df = pd.DataFrame({
    '과목': ['국어', '영어', '수학'],
    '점수': [85, 90, 78]
})
# 문제5. '점수'가 80 미만인 행을 모두 삭제하세요.
df = df[df["점수"] >= 80]

# 문제6. '학년' 열(값은 모두 1)을 추가하세요.
df["학년"] = 1
df

df = pd.DataFrame({
    '이름': ['A', 'B'],
    '나이': [20, 22]
})
# 문제7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
# (단, '키'라는 새 열이 자동으로 추가되어야 함)
print(df)
new_row = pd.DataFrame([{"이름":"C", "나이":25, "키":np.nan}])
df = pd.concat([df, new_row], ignore_index=True)
df


df = pd.DataFrame({
    '부서': ['영업', '기획', '개발', '디자인'],
    '인원': [3, 2, 5, 1]
})
# 문제8. 인원이 2명 이하인 행을 모두 삭제하고,
df = df[df["인원"] > 2].reset_index(drop=True)

# 문제9. '평가' 열을 새로 추가해 모든 값을 '미정'으로 채우세요.
df["평가"] = "미정"
df

# 값 기준 정렬 : sort_values
data = {
    '이름': ['홍길동', '김철수', '이영희', '박민수'],
    '점수': [90, 70, 85, 95],
    '반': [2, 1, 1, 2]
}
df = pd.DataFrame(data)
df

# 오름차순 정렬
df2 = df.sort_values("점수").reset_index(drop=True)
df2

# 내림차순 정렬
# ascending = False
df3 = df.sort_values("점수", ascending=False).reset_index(drop=True)
df3

# 여러 기준으로 정렬
df4 = df.sort_values(["반","점수"], ascending=[True, False]).reset_index(drop=True)
df4

# 원본 변경
df.sort_values(["반","점수"], 
                ascending=[True, False],
                inplace=True
              )
df.reset_index(drop=True)

# 인덱스 기준 정렬 : sort_index
df_shuffled = df.sample(frac=1, random_state=42)
df_shuffled

# 행 인덱스 기준으로 정렬
df5 = df_shuffled.sort_index() # 오름차순
# df5 = df_shuffled.sort_index(ascending=False) # 내림차순
df5

# 열 이름 기준 정렬(알파벳순)
df6 = df.sort_index(axis=1)
df6

# 실습3.
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [88, 95, 70, 100]
})
# 문제1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
df1 = df.sort_values("score").reset_index(drop=True)
df1

# 문제2. score 컬럼 기준 내림차순으로 정렬한 후, 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를 출력하세요.
df2 = df.sort_values("score", ascending=False).reset_index(drop=True)
df2


df = pd.DataFrame({
    '이름': ['가', '나', '다', '라', '마'],
    '반': [2, 1, 1, 2, 1],
    '점수': [90, 85, 80, 95, 85]
})
# 문제3. 주어진 DataFrame에서,반(class) 기준 오름차순,
# 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결과를 출력하세요.
df3 = df.sort_values(["반","점수"], ascending=[True, False]).reset_index(drop=True)
df3

# 문제4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
df4 = df3.sort_index(axis=1)
df4


df = pd.DataFrame({
    'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])

print(df)

# 문제5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
df5 = df.sort_index()
df5

# 문제6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하세요.
df6 = df.sort_index(ascending=False)
df6
d7 = df.sort_values("value")

df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'B', 'C'],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
    'score': [90, 85, 80, 70, 95, 88]
})
df

# 단일 컬럼 기준 그룹화
grouped = df.groupby("team")

# 집계함수 적용
result_sum = grouped["score"].sum()
print(result_sum)

# 평균
result_mean = grouped["score"].mean()
print(result_mean)

# 개수
result_count = grouped["score"].count()
print(result_count)

df2 = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'B', 'C'],
    'gender': ['M', 'F', 'F', 'M', 'M', 'F'],
    'score': [90, 85, 80, 70, 95, 88],
    'age' : [21, 22, 23, 25, 20, 27]
})
df2

# 여러 컬럼 기준 그룹화
result = df2.groupby(["team", "gender"])["score"].mean()
result

# as_index=False 옵션
# 그룹라벨이 인덱스로 설정됨
result = df2.groupby("team", as_index=False)["score"].sum()
result

# 여러 집계 함수를 한번에 적용 : agg()
result = df2.groupby("team", as_index=False)["score"].agg(["sum","mean","count"])
result

# 그룹별로 여러 컬럼에 다른 집계 함수 적용
result = df2.groupby("team").agg({
  "score" : "mean",
  "age" : "max"
})
result

# 실습4.
# 문제1. 각 학년(grade)별 평균 국어 점수(kor)를 구하세요.
df = pd.DataFrame({
    'grade': [1, 2, 1, 2, 1, 3],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
    'kor': [85, 78, 90, 92, 80, 75]
})

result = df.groupby("grade")["kor"].mean()
result

# 문제2. 아래 DataFrame에서 반(class)별, 과목(subject)별로 시험에 응시한 학생 수(count)와
# 평균 점수(avg)를 구하세요.
df = pd.DataFrame({
    'class': [1, 1, 1, 2, 2, 2],
    'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
    'score': [80, 90, 85, 70, 95, 90]
})

result = df.groupby(["class", "subject"])["score"].agg(["count", "mean"])
result

# 문제3. 아래 DataFrame에서 지역(region)별 판매자(seller)별로
# 판매액(sales)의 합계와 최대값을 구하세요.
df = pd.DataFrame({
    'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu'],
    'seller': ['A', 'B', 'A', 'B', 'A'],
    'sales': [100, 200, 150, 120, 130]
})

result = df.groupby(["region", "seller"])["sales"].agg("sum", "max")
result

# 문제4. 아래 DataFrame에서 팀(team)별, 포지션(position)별로
# 결측치(NaN)를 포함한 점수(score)의 평균을 구하세요.
df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'A', 'B'],
    'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
    'score': [3, 2, None, 1, 4, 2]
})
result = df.groupby(["team","position"])["score"].mean()
result

# 문제5. 아래 DataFrame에서 부서(dept)별로 성별(gender)별 인원 수와,
# 총 연봉(salary) 합계를 구하세요.
df = pd.DataFrame({
    'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
    'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})

# result = df.groupby(["dept", "gender"])["salary"].agg(["count", "sum"])
result = df.groupby(["dept", "gender"]).agg(
    count=("salary", "count"),
    total_salary=("salary", "sum")
)
result