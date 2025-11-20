import numpy as np

# 배열 간 연산(1차원)
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1 + a2) # [5 7 9]
print(a1 - a2) # [-3 -3 -3]
print(a1 * a2) # [ 4 10 18]

# 배열 간 연산(2차원)
a1 = np.arange(1,5).reshape(2,2)
a2 = np.arange(11,15).reshape(2,2)
print(a1) # [[1 2]
          #  [3 4]]
print(a2) # [[11 12]
          #  [13 14]]
print(a1 + a2)  # [[12 14]
                #  [16 18]]
print(a2 - a1)  # [[10 10]
                #  [10 10]]

# 배열과 스칼라 연산(1차원)
a1 = np.array([1,2,3,4])
print(a1 + 10) # [11 12 13 14]
print(a1 * 2)  # [2 4 6 8]

# 배열과 스칼라 연산(2차원)
a1 = np.arange(1,5).reshape(2,2)
a2 = np.arange(11,15).reshape(2,2)
print(a1) # [[1 2]
          #  [3 4]]
print(a2) # [[11 12]
          #  [13 14]]
print(a1 + 5)   # [[6 7]
                #  [8 9]]
print(a2 * 3)   # [[33 36]
                #  [39 42]]
print(a2 / 2)   # [[ 5.5  6. ]
                #  [ 6.5  7. ]]

# 배열의 구조가 다를 경우
a1 = np.array([1,2])
a2 = np.array([1,2,3])
# print(a1+a2)  # ValueError: operands could not be broadcast together with shapes (2,) (3,)

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

print(a1 + a2) # [[11 22 33]
               #  [14 25 36]]

# 브로드캐스팅 예제
a1 = np.array([[1], [2], [3]]) # (3, 1)
a2 = np.array([10, 20, 30]) # (3,)
print("a1 shape:", a1.shape)  # a1 shape: (3, 1)
print("a2 shape:", a2.shape)  # a2 shape: (3,)

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

print(a1 + a2) # [[11 21 31]
               #  [12 22 32]
               #  [13 23 33]]

# 브로드캐스팅 불가능한 경우
a1 = np.ones((2,3))
a2 = np.ones((3,2))
# a1 + a2  # ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

# 실습1
# 문제1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
print(arr + 3) # [4 5 6 7]

# 문제2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10], [15, 20]])
print(arr * -1) # [[ -5 -10]
                #  [-15 -20]]

# 문제3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])

print(arr1 * arr2) # [ 2  8 18]
print(arr1 / arr2) # [2. 2. 2.]

# 문제4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해
# 필요한 값을 더한 결과 배열을 만드세요.
arr = np.array([[95, 97], [80, 85]])
add_values = 100 - arr
print(add_values)       # [[ 5  3]
                        #  [20 15]]
print(arr + add_values) # [[100 100]
                        #  [100 100]]

# 문제5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
# 첫 번째 행은 10을 곱하고
# 두 번째 행은 100을 곱해야 합니다.
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10], [100]])

print(arr * arr2) # [[ 10  20  30]
                  #  [400 500 600]]

# 문제6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
arr = np.array([10, 20, 30, 40, 50, 60]).reshape(3,2) # (3,2)
# arr2 = np.array([[100],[200],[300]])
arr2 = np.array([100,200,300]).reshape(3,1)
print(arr + arr2) # [[110 120]
                  #  [230 240]
                  #  [350 360]]





# 통계 함수 및 집계 연산

a = np.array([[1,2,3],[4,5,6]])

print("원소의합:", np.sum(a))      # 원소의합: 21
print("원소의평균:", np.mean(a))   # 원소의평균: 3.5
print("표준편차:", np.std(a))      # 표준편차: 1.707825127659933
print("최대값:", np.max(a))        # 최대값: 6
print("최소값:", np.min(a))        # 최소값: 1
print("최대값의 인덱스:", np.argmax(a))  # 최대값의 인덱스: 5
print("최소값의 인덱스:", np.argmin(a))  # 최소값의 인덱스: 0

# 축(axis) 단위 연산
# axis = 0 → 가장 높은 차원 기준 → 행기준
  # 행기준 = 행을 따라 연산 = 행을 증가시키며 연산
# axis = 1 → 그 다음 차원 기준 → 열기준
  # 열기준 = 열을 따라 연산 = 열을 증가시키며 연산

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("행기준합", np.sum(a, axis=0))   # 행기준합 [12 15 18]
print("열기준합", np.sum(a, axis=1))   # 열기준합 [ 6 15 24]
print("행기준평균", np.mean(a, axis=0))# 행기준평균 [4. 5. 6.]
print("열기준평균", np.mean(a, axis=1))# 열기준평균 [2. 5. 8.]

# 누적 연산
arr = np.array([1,2,3,4])
print(np.cumsum(arr)) # [ 1  3  6 10]
print(np.cumprod(arr))# [ 1  2  6 24]

# 실습2.
# 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print("합", np.sum(arr))   # 합 50
print("평균", np.mean(arr))# 평균 12.5

# 문제2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1], [9, 2, 8]])
print("최대값", np.max(arr)) # 최대값 9
print("최소값", np.min(arr)) # 최소값 1

# 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("각 열의 합계:", np.sum(arr, axis=0)) # 각 열의 합계: [12 15 18]
print("각 행의 합계:", np.sum(arr, axis=1)) # 각 행의 합계: [ 6 15 24]

# 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20],[30, 40],[50, 60]])
print("행별 평균:", np.mean(arr, axis=1)) # 행별 평균: [15. 35. 55.]
print("열별 평균:", np.mean(arr, axis=0)) # 열별 평균: [30. 40.]

# 1차원 배열에서 전체 표준편차를 구하고,
# 각 요소가 평균으로부터 얼마나 떨어져 있는지 편차 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
arr_std = np.std(arr)
arr_mean = np.mean(arr)
deviation = arr - arr_mean
print("평균", arr_mean)      # 평균 5.0
print("표준편차", arr_std)   # 표준편차 2.0
print("편차배열", deviation) # 편차배열 [-3. -1. -1. -1.  0.  0.  2.  4.]

# 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("행 단위 누적 합\n", np.cumsum(arr, axis=1))
# 행 단위 누적 합
# [[ 1  3  6]
#  [ 4  9 15]]
print("열 단위 누적 곱\n", np.cumprod(arr, axis=0))
# 열 단위 누적 곱
# [[ 1  2  3]
#  [ 4 10 18]]

# np.where()
# 조건 기반 선택 함수
arr = np.array([10,20,30,40,50])
result = np.where(arr > 30, "High", "Low")
print(result) # ['Low' 'Low' 'Low' 'High' 'High']

arr = np.array([10,20,30,40,50])
# 조건만 넣을 경우 조건을 만족하는 원소의 인덱스를 반환
result = np.where(arr > 30)
print(result)         # (array([3, 4]),)
print(arr[result])    # [40 50]  # 원본 배열에 Fancy indexing

# 논리 연산
# and : & - 모든 조건이 True여야 True
# or : | - 조건중 하나라도 True면 True
# not : ~ - True를 False로, False를 True

# and연산(&)
arr = np.array([10,20,30,40,50])
mask = (arr > 10) & (arr < 50)
print(mask)           # [False  True  True  True False]
print("&연산", arr[mask]) # &연산 [20 30 40]

# or연산(|)
mask_or = (arr < 20) | (arr > 40)
print("|연산", arr[mask_or]) # |연산 [10 15 50] -> 주의: 이전 arr의 예시와 다른 경우가 있으므로 위 출력은 이 배열 기준: [10 50]

# not연산(~)
mask_not = ~(arr > 30)
print("~연산", arr[mask_not]) # ~연산 [10 20 30]

arr = np.arange(0,100)
mask = (arr % 2 == 0) & (arr > 50)
print(arr[mask]) # [52 54 56 ... 98]

# 실습3.
# 문제1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
arr1 = np.array([5, 12, 18, 7, 30, 25])
print(arr1[(arr1 > 10) & (arr1 < 20)]) # [12 18]

# 문제2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
arr2 = np.array([10, 15, 20, 25, 30, 35])
print(arr2[(arr2 <= 15) | (arr2 >= 30)]) # [10 15 30 35]

# 문제3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
arr3 = np.array([3, 8, 15, 6, 2, 20])
# print(np.where(arr3 >= 10, 0, arr3))
arr3[arr3 >= 10] = 0
print(arr3) # [3 8 0 6 2 0]

# 문제4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High",
# 나머지는 "Low"로 표시하는 새로운 배열을 생성하세요.
arr4 = np.array([7, 14, 21, 28, 35])
print(np.where(arr4 >= 20, "High", "Low")) # ['Low' 'Low' 'High' 'High' 'High']

# 문제5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr5 = np.arange(10)
print(np.where(arr5 % 2 == 0, arr5, arr5 * 10)) # [ 0 10  2 30  4 50  6 70  8 90]

# 문제6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
arr6 = np.array([[10, 25, 30],
      [40, 5, 15],
      [20, 35, 50]])

mask = (arr6 >= 20) & (arr6 <= 40)
print(arr6[mask]) # [25 30 40 20 35]

# 문제7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr7 = np.array([1, 2, 3, 4, 5, 6])
mask = ~(arr7 % 3 == 0)
print(arr7[mask]) # [1 2 4 5]

# 문제8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# 50 이상인 값은 그대로
# 50 미만인 값은 50으로 변경
arr8 = np.random.randint(0, 101, size=10)
print(arr8) # 예: [12 67 45 90  3 56 78 49 50 10] (랜덤)
print(np.where(arr8 >= 50, arr8, 50)) # 예: [50 67 50 90 50 56 78 50 50 50]

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
# [['C' 'B' 'A']
#  ['C' 'A' 'C']
#  ['B' 'B' 'A']]



# 행렬 곱셈




# np.dot(a,b) : 배열의 내적 연산
# 스칼라 연산(OD)
a = np.array(3)
b = np.array(4)

print(np.dot(a,b)) # 12

# 1차원 배열간 연산 → 내적
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b)) # 32

# 물건 구매
# 데이터분석에서 벡터란 배열
c = [1000, 2000, 5000, 10000]
d = [10, 3, 5, 7]
print(np.dot(c,d)) # 111000

# 2차원 배열간 연산 → 행렬 곱셈
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
print(np.dot(a,b)) # [[22 28]
                   #  [49 64]]

# np.matmul(a,b)
# Matrix Multiplication
# 스칼라 연산 시도시 에러
a = np.array(3)
a = np.array(4)
print(np.matmul(a,b)) # ValueError: matmul: Input operand 1 does not have enough dimensions

# 1차원 배열간 연산 → 내적
a = np.array([1,2])
b = np.array([3,4])
print(np.matmul(a,b)) # 11

# 2차원 배열간 연산 → 행렬 곱셈
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
print(np.matmul(a,b)) # [[22 28]
                      #  [49 64]]

# 2d * 1d 간 연산 
c = np.array([[1,2],[3,4]])
d = np.array([5,6])
print(np.matmul(c,d)) # [17 39]
print(np.matmul(d,c)) # [23 34]

# @ 연산자
e = np.array([[1,2,3]])
f = np.array([[1,2],[3,4],[5,6]])
# print(np.matmul(e,f))
print(e @ f) # [[22 28]]

# 실습4.
# 문제1. 1부터 9까지의 정수로 채워진 (3, 3) 배열 A와,
# 모두 2로 채워진 (3, 2) 배열 B를 만들고 곱하세요.
a = np.arange(1,10).reshape(3,3)
print(a) # [[1 2 3]
         #  [4 5 6]
         #  [7 8 9]]
b = np.full((3,2),2)
print(b) # [[2 2]
         #  [2 2]
         #  [2 2]]
print(np.matmul(a,b)) # [[12 12]
                      #  [30 30]
                      #  [48 48]]
print(a @ b)          # [[12 12]
                      #  [30 30]
                      #  [48 48]]

# 문제2. 4×4 단위행렬 I와, 4×4 난수 행렬 M(0~9 사이 정수) 간의 곱을 구하고,
# 결과와 M이 동일한지 확인하세요.
I = np.eye(4)
print(I) # [[1. 0. 0. 0.]
         #  [0. 1. 0. 0.]
         #  [0. 0. 1. 0.]
         #  [0. 0. 0. 1.]]
M = np.random.randint(0, 10, (4, 4))
print(M) # 예: [[3 7 1 2]
         #       [0 9 4 5]
         #       [6 2 8 1]
         #       [3 5 0 7]]

print(I @ M) # M (동일한 값)
print(M @ I) # M (동일한 값)

# 같은 위치에 있는 원소끼리 곱함
M * I  # 대각원소만 남고 나머지는 0인 배열

# 문제3. 모든 값이 1인 (2, 5) 배열 X와,
# 5부터 14까지의 연속된 정수로 채워진 (5, 2) 배열 Y를 만들어 곱하세요.
X = np.ones((2,5))
print(X) # [[1. 1. 1. 1. 1.]
         #  [1. 1. 1. 1. 1.]]
Y = np.arange(5,15).reshape(5,2)
print(Y) # [[ 5  6]
         #  [ 7  8]
         #  [ 9 10]
         #  [11 12]
         #  [13 14]]
print(X @ Y) # [[45. 50.]
             #  [45. 50.]]

# 문제4. 0 이상 5 미만의 임의의 정수로 채워진 (3, 2) 배열 C와
# (2, 3) 배열 D를 각각 만들어 곱한 결과의 shape와 값을 출력하세요.
a = np.random.randint(0, 5, (3, 2))
b = np.random.randint(0, 5, (2, 3))

print(a) # 예: [[1 4]
         #       [0 3]
         #       [2 1]]
print(b) # 예: [[2 0 3]
         #       [4 1 0]]
result = a @ b
print(result) # 예: [[18  4  3]
              #       [12  3  0]
              #       [ 8  5  6]]
print(result.shape) # (3, 3)