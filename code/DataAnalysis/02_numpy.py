import numpy as np

# 배열 간 연산(1차원)
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1 + a2)
print(a1 - a2)

# 배열 간 연산(2차원)
a1 = np.arange(1,5).reshape(2,2)
a2 = np.arange(11,15).reshape(2,2)
print(a1)
print(a2)
print(a1 + a2)
print(a2 - a1)

# 배열과 스칼라 연산(1차원)
a1 = np.array([1,2,3,4])
print(a1 + 10)
print(a1 * 2)

# 배열과 스칼라 연산(2차원)
a1 = np.arange(1,5).reshape(2,2)
a2 = np.arange(11,15).reshape(2,2)
print(a1)
print(a2)
print(a1 + 5)
print(a2 * 3)
print(a2 / 2)

# 배열의 구조가 다를 경우
a1 = np.array([1,2])
a2 = np.array([1,2,3])
print(a1+a2)

# 브로드캐스팅 
# 자동으로 배열의 크기를 확장 → 서로 다른 크기의 배열 간 연산을 가능하게 하는 기능
# 1. 두 배열의 차원을 뒤(낮은 차원)에서부터 비교
# 2. 크기가 같거나
# 3. 한쪽이 1인 경우 확장이 가능

a1 = np.array([[1,2,3],
              [4,5,6]]) # 2x3 배열
a2 = np.array([10,20,30]) # 길이가 3인 1차원 배열

# 1차원 길이3
[10,20,30]

# 2차원으로 변형 (1,3)
[[10,20,30]]

# 2차원의 행이 2로 확장
[[10,20,30],
[10,20,30]]

print(a1 + a2)

# 브로드캐스팅 예제
a1 = np.array([[1], [2], [3]]) # (3, 1)
a2 = np.array([10, 20, 30]) # (3,)
print("a1 shape:", a1.shape)
print("a2 shape:", a2.shape)

# a2 : (3,) → (1, 3)로 변형
[[10, 20, 30]]

# a1과 a2비교: a1 = (3, 1), a2 = (1, 3)
# 2차원의 경우 : 3 vs 1 → a2의 2차원이 3으로 확장
[[10, 20, 30], [10, 20, 30], [10, 20, 30]]

# 1차원의 경우 : 1 vs 3 → a1의 1차원이 3으로 확장
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# a1
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
              # +
# a2
[[10, 20, 30], [10, 20, 30], [10, 20, 30]]

print(a1 + a2)

# 브로드캐스팅 불가능한 경우
a1 = np.ones((2,3))
a2 = np.ones((3,2))
a1 + a2

# 실습1
# 문제1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
print(arr + 3)

# 문제2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10], [15, 20]])
print(arr * -1)

# 문제3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])

print(arr1 * arr2)
print(arr1 / arr2)

# 문제4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해
# 필요한 값을 더한 결과 배열을 만드세요.
arr = np.array([[95, 97], [80, 85]])
add_values = 100 - arr
print(add_values)
print(arr + add_values)

# 문제5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
# 첫 번째 행은 10을 곱하고
# 두 번째 행은 100을 곱해야 합니다.
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10], [100]])

print(arr * arr2)

# 문제6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
arr = np.array([10, 20, 30, 40, 50, 60]).reshape(3,2) # (3,2)
# arr2 = np.array([[100],[200],[300]])
arr2 = np.array([100,200,300]).reshape(3,1)
print(arr + arr2)

a = np.array([[1,2,3],[4,5,6]])

print("원소의합:", np.sum(a))
print("원소의평균:", np.mean(a))
print("표준편차:", np.std(a))
print("최대값:", np.max(a))
print("최소값:", np.min(a))
print("최대값의 인덱스:", np.argmax(a))
print("최소값의 인덱스:", np.argmin(a))

# 축(axis) 단위 연산
# axis = 0 → 가장 높은 차원 기준 → 행기준
  # 행기준 = 행을 따라 연산 = 행을 증가시키며 연산
# axis = 1 → 그 다음 차원 기준 → 열기준
  # 열기준 = 열을 따라 연산 = 열을 증가시키며 연산

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("행기준합", np.sum(a, axis=0))
print("열기준합", np.sum(a, axis=1))
print("행기준평균", np.mean(a, axis=0))
print("열기준평균", np.mean(a, axis=1))

# 누적 연산
arr = np.array([1,2,3,4])
print(np.cumsum(arr))
print(np.cumprod(arr))

# 실습2.
# 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print("합", np.sum(arr))
print("평균", np.mean(arr))

# 문제2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1], [9, 2, 8]])
print("최대값", np.max(arr))
print("최소값", np.min(arr))

# 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("각 열의 합계:", np.sum(arr, axis=0))
print("각 행의 합계:", np.sum(arr, axis=1))

# 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20],[30, 40],[50, 60]])
print("행별 평균:", np.mean(arr, axis=1))
print("열별 평균:", np.mean(arr, axis=0))

# 1차원 배열에서 전체 표준편차를 구하고,
# 각 요소가 평균으로부터 얼마나 떨어져 있는지 편차 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
arr_std = np.std(arr)
arr_mean = np.mean(arr)
deviation = arr - arr_mean
print("평균", arr_mean)
print("표준편차", arr_std)
print("편차배열", deviation)

# 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("행 단위 누적 합\n", np.cumsum(arr, axis=1))
print("열 단위 누적 곱\n", np.cumprod(arr, axis=0))

# np.where()
# 조건 기반 선택 함수
arr = np.array([10,20,30,40,50])
result = np.where(arr > 30, "High", "Low")
print(result)

arr = np.array([10,20,30,40,50])
# 조건만 넣을 경우 조건을 만족하는 원소의 인덱스를 반환
result = np.where(arr > 30)
print(result)
print(arr[result]) # 원본 배열에 Fancy indexing

# 논리 연산
# and : & - 모든 조건이 True여야 True
# or : | - 조건중 하나라도 True면 True
# not : ~ - True를 False로, False를 True

# and연산(&)
arr = np.array([10,20,30,40,50])
mask = (arr > 10) & (arr < 50)
print(mask)
print("&연산", arr[mask])

# or연산(|)
mask_or = (arr < 20) | (arr > 40)
print("|연산", arr[mask_or])

# not연산(~)
mask_not = ~(arr > 30)
print("~연산", arr[mask_not])

arr = np.arange(0,100)
mask = (arr % 2 == 0) & (arr > 50)
print(arr[mask])

# 실습3.
# 문제1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
arr1 = np.array([5, 12, 18, 7, 30, 25])
print(arr1[(arr1 > 10) & (arr1 < 20)])

# 문제2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
arr2 = np.array([10, 15, 20, 25, 30, 35])
print(arr2[(arr2 <= 15) | (arr2 >= 30)])

# 문제3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
arr3 = np.array([3, 8, 15, 6, 2, 20])
# print(np.where(arr3 >= 10, 0, arr3))
arr3[arr3 >= 10] = 0
print(arr3)

# 문제4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High",
# 나머지는 "Low"로 표시하는 새로운 배열을 생성하세요.
arr4 = np.array([7, 14, 21, 28, 35])
print(np.where(arr4 >= 20, "High", "Low"))

# 문제5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr5 = np.arange(10)
print(np.where(arr5 % 2 == 0, arr5, arr5 * 10))

# 문제6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
arr6 = np.array([[10, 25, 30],
      [40, 5, 15],
      [20, 35, 50]])

mask = (arr6 >= 20) & (arr6 <= 40)
print(arr6[mask])

# 문제7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr7 = np.array([1, 2, 3, 4, 5, 6])
mask = ~(arr7 % 3 == 0)
print(arr7[mask])

# 문제8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# 50 이상인 값은 그대로
# 50 미만인 값은 50으로 변경
arr8 = np.random.randint(0, 101, size=10)
print(arr8)
print(np.where(arr8 >= 50, arr8, 50))

# 문제9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# 70 이상 → "A"
# 30 이상 70 미만 → "B"
# 30 미만 → "C“
arr9 =np.array([[5, 50, 95],
              [20, 75, 10],
              [60, 30, 85]])

result = np.where(arr9 >= 70, "A", 
                  np.where(arr9 >= 30, "B", "C"))

print(result)

# np.dot(a,b) : 배열의 내적 연산
# 스칼라 연산(OD)
a = np.array(3)
b = np.array(4)

print(np.dot(a,b))

# 1차원 배열간 연산 → 내적
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

# 물건 구매
# 데이터분석에서 벡터란 배열
c = [1000, 2000, 5000, 10000]
d = [10, 3, 5, 7]
print(np.dot(c,d))

# 2차원 배열간 연산 → 행렬 곱셈
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
print(np.dot(a,b))

# np.matmul(a,b)
# Matrix Multiplication
# 스칼라 연산 시도시 에러
a = np.array(3)
a = np.array(4)
print(np.matmul(a,b))

# 1차원 배열간 연산 → 내적
a = np.array([1,2])
b = np.array([3,4])
print(np.matmul(a,b))

# 2차원 배열간 연산 → 행렬 곱셈
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
print(np.matmul(a,b))

# 2d * 1d 간 연산 
c = np.array([[1,2],[3,4]])
d = np.array([5,6])
print(np.matmul(c,d))
print(np.matmul(d,c))

# @ 연산자
e = np.array([[1,2,3]])
f = np.array([[1,2],[3,4],[5,6]])
# print(np.matmul(e,f))
print(e @ f)

# 실습4.
# 문제1. 1부터 9까지의 정수로 채워진 (3, 3) 배열 A와,
# 모두 2로 채워진 (3, 2) 배열 B를 만들고 곱하세요.
a = np.arange(1,10).reshape(3,3)
print(a)
b = np.full((3,2),2)
print(b)
print(np.matmul(a,b))
print(a @ b)

# 문제2. 4×4 단위행렬 I와, 4×4 난수 행렬 M(0~9 사이 정수) 간의 곱을 구하고,
# 결과와 M이 동일한지 확인하세요.
I = np.eye(4)
print(I)
M = np.random.randint(0, 10, (4, 4))
print(M)

print(I @ M)
print(M @ I)

# 같은 위치에 있는 원소끼리 곱함
M * I

# 문제3. 모든 값이 1인 (2, 5) 배열 X와,
# 5부터 14까지의 연속된 정수로 채워진 (5, 2) 배열 Y를 만들어 곱하세요.
X = np.ones((2,5))
print(X)
Y = np.arange(5,15).reshape(5,2)
print(Y)
print(X @ Y)

# 문제4. 0 이상 5 미만의 임의의 정수로 채워진 (3, 2) 배열 C와
# (2, 3) 배열 D를 각각 만들어 곱한 결과의 shape와 값을 출력하세요.
a = np.random.randint(0, 5, (3, 2))
b = np.random.randint(0, 5, (2, 3))

print(a)
print(b)
result = a @ b
print(result)
print(result.shape)