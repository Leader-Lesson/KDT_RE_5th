import numpy as np

# # ndarray의 생성
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([1.0, 3.14, 1.24])

# # 배열의 구조
# print(f"배열의 구조: {a.shape}")

# # 배열의 차원 수
# print(f"배열의 차원: {a.ndim}")

# # 데이터 타입
# print(f"배열의 데이터타입: {a.dtype}")
# print(f"배열의 데이터타입: {b.dtype}")

# # 형변환
# new_a = a.astype(np.float64)
# print(f"수정한 배열의 데이터타입: {new_a.dtype}")


# # 3차원 행렬
# a = np.array([[[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]]])
# print(f"배열의 구조: {a.shape}")
# print(f"배열의 차원: {a.ndim}")

# # 4차원 행렬
# a = np.array([[[[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]]],
#               [[[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]],
#               [[1,2,3],[4,5,6]]]])
# print(f"배열의 구조: {a.shape}")
# print(f"배열의 차원: {a.ndim}")

# # 만들 수 없는 배열
# # 내부 배열의 구조가 같아야 함
# # a = np.array([[1],[2,3]])

# # 모든 요소가 0인 배열 생성
# np.zeros((3, 4)) # 2차원
# np.zeros((2, 3, 4), dtype=np.int64) # 3차원

# # 모든 요소가 1인 배열 생성
# np.ones((5, 6))

# # (원소의 값이) 초기화 되지 않은 배열 생성
# np.empty((2, 3))

# # 주어진 값으로 채운 배열
# np.full((3,3), 7)

# # 단위 행렬
# np.eye(3, 3)
# np.eye(3, 5, 1) # 3번째 인자를 입력 → 1이 오른쪽으로 이동

# # arange : range()와 유사한 기능을 제공
# # 시작 이상 끝 미만의 정수 배열을 지정한 간격으로 생성
# np.arange(0, 10)
# np.arange(0, 10, 2) # 간격 지정

# # linspace : 시작~끝까지 균일 간격으로 지정한 개수만큼 숫자를 생성
# # 끝을 포함
# np.linspace(10, 100, 10)
# np.linspace(0.1, 1, 10)

# # reshape : 배열의 구조를 재배치
# np.linspace(1,10,10).reshape((2,3)) # 원소의 개수가 같아야 함
np.linspace(5,100,20).reshape((4,5)) # 등간격으로 20개 생성 후 (4,5) 구조로 재배치

# # random.rand(m, n) : 0~1 사이의 난수로 초기화
# np.random.rand(2,3)

# # random.randn(m, n) : 표준정규분포를 따르는 난수로 초기화
# # 표준정규분포 : 평균 0, 분산 1인 정규분포
# np.random.randn(2,4,5)

# # random.normal(평균, 분산, 사이즈)
# # 정규분포
# np.random.normal(10, 20, (2,4))

# # random.randint(low, high, (size))
# print(np.random.randint(0, 101, (3 ,3)))

# print(">>>>>>>>>>>>>>>>>>>>>>>")
# # random.seed() : 난수 생성시 시작값 제공
# np.random.seed(42)
# print(np.random.rand(2,3))
# print(np.random.randn(2,2))
# print(np.random.randint(0, 101, (3 ,3)))

# # RNG(Random Number Generator)
# # 최근 NumPy 사용에서 권장되는 방식
# from numpy.random import default_rng

# rng = default_rng(seed=42)
# rng2 = default_rng(seed=10)
# rng3 = default_rng()

# print(rng.random((3,2))) # 0~1사이의 난수
# print(rng2.normal(0, 1, (4,5))) # 정규분포
# print(rng3.integers(0, 100, (2,2))) # 정수 난수
# print(rng.uniform(0, 100, (4,4))) # 균등 분포

# # 실습1. 배열 초기화 및 생성(1)
# # 1. 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요. 
# a1 = np.zeros((3,4))
# a1_2 = np.full((3,4),5)
# print("문제1:", a1, a1_2, sep="\n")

# # 2. 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
# a2 = np.arange(0, 21, 2)
# print("\n문제2:", a2)

# # 3. 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
# a3 = np.random.rand(2,3)
# print("\n문제3:", a3)

# # 4. 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하세요.
# a4 = np.random.normal(100, 20, 6)
# print("\n문제4:", a4)

# # 5. 1부터 20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4, 5) 크기의 2차원 배열로 변환하세요.
# a5 = np.arange(1,21).reshape(4,5)
# print("\n문제5:", a5)

# # 6. 0부터 1까지 균등 간격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3, 4) 크기로 변환하세요. 
# a6 = np.linspace(0, 1, 12).reshape(3,4)
# print("\n문제6:", a6)

# # 7. 0~99 사이의 정수 난수로 이루어진 (10, 10) 배열을 생성한 뒤,
# # np.eye()로 만든 단위 행렬을 더하여 대각선 요소가 1씩 증가된 배열을 만드세요.
# a7 = np.random.randint(0, 100, (10, 10))
# a7_eye = np.eye(10)
# a7_added = a7 + a7_eye
# print("\n문제7:", a7_added)

# # 8. 0~9 사이의 정수 난수로 이루어진 (2, 3, 4) 3차원 배열을 생성하세요.
# a8 = np.random.randint(0, 10, (2, 3, 4))
# print("\n문제8:", a8)



# /////////////////////////////
# ndarray의 인덱싱과 슬라이싱


# 인덱싱
a = np.array([10, 20, 30, 40, 50])
print(a[2])
print(a[-1])

# 다차원 인덱싱
# 파이썬 리스트
matrix = [[1,2,4],[4,5,6]]
print("파이썬 인덱싱:", matrix[1][1])

# NumPy 배열
a2 = np.array([[1,2,4],[4,5,6]])
print(a2.shape)
print("numpy 인덱싱:", a2[1, 2])

# 3차원 배열 인덱싱
a3 = np.arange(24).reshape(2, 3, 4)
print(a3)
print(a3.shape)
print("17", a3[1,1,1])
print("11", a3[0,2,3])
print("23", a3[1,2,3])





# 슬라이싱
# arr[행_슬라이스, 열_슬라이스]
# arr[..., 4차원슬라이스, 3차원슬라이스, 2차원슬라이스, 1차원슬라이스]
a1 = np.array([10, 20, 30, 40, 50])

print(a1[1:3])
print(a1[2:])
print(a1[:2])
print(a1[:])
print(a1[::2])
print(a1[::-1])

# 파이썬 리스트와의 차이
# 파이썬 리스트
py_list = [10, 20, 30, 40, 50]
sliced = py_list[1:4]
sliced[1] = 100
print("py원본:", py_list)
print("py슬라이싱:", sliced)
print()

# numpy 배열
a1 = np.array([10, 20, 30, 40, 50])
a1_sliced = a1[1:4]
a1_sliced[1] = 100
print("numpy원본:", a1)
print("numpy슬라이싱:", a1_sliced)

# 2차원 배열 슬라이싱
a2 = np.arange(1, 21).reshape(4, 5)
print(a2)
print()

# 행 슬라이싱(2차원 슬라이싱)
# print(a2[0])
# print(a2[1])
# print(a2[1:3])
# print(a2[2:])
# print()

# 열 슬라이싱(1차원 슬라이싱)
# print(a2[:, 2])
# print(a2[:, -1])
# print(a2[:, 1:3])
# print()

# 행과 열 슬라이싱
print(a2[1:3, 2:4])
print(a2[2:, 3:])
print(a2[::2, ::2])

# 3차원 슬라이싱
a3 = np.arange(36).reshape(3, 3, 4)
print(a3)
print(a3[1, 1, 1:3])

# 얕은 복사 : 복사본이 원본과 메모리를 공유 → 변경사항이 서로에게 영향을 줌
a1 = np.array([1,2,3])
a1_copied = a1.view()
a1_copied[1] = 10
print("원본", a1)
print("복사본", a1_copied)
print()

# 깊은 복사 : 복사본이 원본과 독립적으로 복사됨 → 서로 영향을 주지X
a2 = np.array([1,2,3])
a2_copied = a2.copy()
a2_copied[1] = 10
print("원본2", a2)
print("복사본2", a2_copied)




print("<<<<<< Fancy & Boolean Indexing >>>>>>")

# Fancy indexing
# 정수 배열을 사용하여 여러 인덱스로 여러 요소를 한번에 선택 ([] 두개 사용)
af = np.arange(1,21)
# print(af)
# print(af[[4,7,11]])

af2 = np.arange(1, 21).reshape(4, 5)
print(af2)
print(af2[[1,3],[2,4]]) # 행과 열을 짝으로 선택, (1,2), (3,4) -> 1행 2열, 3행 4열

# Boolean indexing
ab = np.linspace(10,100,10)
print(ab)
print(ab[ab > 40])
print()

# Boolean masking
ab2 = np.arange(0,21)
print(ab2)
mask = ab2 % 2 == 0
print(mask)
print(ab2[mask])

# 실습2
# 1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택하세요.
arr = np.arange(10, 30, 2)
print(arr)
answer = arr[[1,3,5]]
print(answer)


# 2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
arr = np.arange(1, 10).reshape(3, 3)
print(arr)
arr[[0,1,2],[0,1,2]]

# 3. 3x4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
arr[:, -1] = -1
arr

# 4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
arr = np.arange(1, 17).reshape(4, 4)
print(arr)


# 5. 4x5 배열에서 가운데 2x3 부분을 슬라이싱한 뒤 copy()를 이용해 독립 배열을 만드세요.
arr = np.arange(1, 21).reshape(4, 5)
print(arr)
print("행을 역순\n", arr[::-1])
print("열을 역순\n", arr[:,::-1])

# 6. 3x4 배열에서 짝수이면서 10 이상인 값만 선택하세요.
arr = np.array([[ 4,  9, 12,  7],
                [10, 15, 18,  3],
                [ 2, 14,  6, 20]])
arr[(arr % 2 == 0) & (arr >= 10)]

# 7. 5x5 배열에서 2, 4번째 행을 선택하고, 선택된 행에서 열 순서를 [4, 0, 2]로 재배치하세요.
arr = np.arange(1, 26).reshape(5, 5)
print(arr)
result = arr[[1,3]]
print(result)

# 방법1.
# answer = []
# for i in result:
#   answer.append([i[4],i[0],i[2]])
# print(np.array(answer))

# 방법2.
result[:, [4,0,2]]

# 8. 5x3 배열에서 각 행의 첫 번째 값이 50 이상인 행만 Boolean Indexing으로 선택하세요.
arr = np.array([[10, 20, 30],
                [55, 65, 75],
                [40, 45, 50],
                [70, 80, 90],
                [15, 25, 35]])

arr[arr[:,0] >= 50]

# 9. 4x4 배열에서 (0,1), (1,3), (2,0), (3,2) 위치의 요소를 한 번에 선택하세요.
arr = np.arange(1, 17).reshape(4, 4)
arr[[0,1,2,3],[1,3,0,2]]

# 10. 3차원 배열 (2, 3, 4)에서 모든 블록에서 두 번째 열만 추출해 새로운 2차원 배열 (2, 3)을 만드세요.
arr3d = np.arange(24).reshape(2, 3, 4)
print(arr3d)
arr3d[:,:,1]

# 실습3.
# 문제1. 0부터 24까지 정수를 가진 배열을 만들고,
# (5, 5) 배열로 변환한 뒤 가운데 행(3번째 행)과 가운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
a1 = np.arange(25).reshape(5,5)
print(a1)
print(a1[2])
print(a1[:,2])

# 문제2. 0~99 정수난수로 이루어진 (10, 10) 배열을 생성하고,
# 짝수 인덱스의 행만 선택하여 출력하세요.
a2 = np.random.randint(0, 100, (10, 10))
print(a2)
print(a2[::2])

# 문제3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후,
# 2행 3열부터 4행 7열까지의 부분 배열을 추출하세요.
a3 = np.arange(50).reshape(5,10)
print(a3)
print(a3[1:4, 2:7])

# 문제4. 
# 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
# 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
# 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
a4 = np.random.randint(0,10,(4,4))
print(a4)
print(a4[[0,1,2,3],[0,1,2,3]])
print(a4[[0,1,2,3],[3,2,1,0]])

# 문제5.
# 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고,
# 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요.
a5 = np.random.randint(0,10,(3,4,5))
print(a5)
print(a5[1, 0, -1])

# 문제6. 35부터 74까지의 순차적인 정수로 이루어진 1차원 배열을 만들고
# 10x4 행렬로 변환 후 출력해주세요.
a6 = np.arange(35,75).reshape(10,4)
print("문제6\n", a6)

# 문제7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
a7 = a6[::-1]
print("문제7\n", a7)

# 문제8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지,
# 세번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.
a8 = a6[1:-1, 2:]
print("문제8\n", a8)


# 문제9. 1부터 50까지의 정수 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성하세요.
arr = np.random.randint(1, 51, (5, 6))
print(arr)
mask = arr % 2 == 0
print(mask)
a9 = arr[mask]
print(a9)

# 문제10. 0부터 99까지의 정수로 이루어진 (10, 10) 배열을 생성한 후,
# [1, 3, 5]번째 행과 [2, 4, 6]번째 열의 교차하는 원소들만 선택하여 출력하세요.
arr = np.arange(100).reshape(10,10)
print(arr)

# seleted_row = arr[[1,3,5]]
# seleted_row = arr[1:6:2]
# print(seleted_row)

# selected_col = seleted_row[:, [2,4,6]]
# selected_col = seleted_row[:, 2:7:2]
# print(selected_col)

a10 = arr[[1,3,5]][:, [2,4,6]]
print(a10)

# 문제11.
# 0~9 정수 난수로 이루어진 1차원 배열(길이 15)을 생성하고,
# 짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
arr = np.random.randint(0, 10, 15)
print(arr)
even_idx_values = arr[::2]
print(even_idx_values)
mask = even_idx_values >= 5
print(mask)
a11 = even_idx_values[mask]
print(a11)