import numpy as np

# array.ravel() 
# 다차원 배열을 1차원 배열로 펼침
# 결과를 view로 반환(view를 변경시 원본도 변경)
a = np.array([[1,2,3],[4,5,6]])
print(a) 
# [[1 2 3]
#  [4 5 6]]

flat = a.ravel()
print(flat) # [1 2 3 4 5 6]

flat[2] = 100
print(flat) # [  1   2 100   4   5   6]
print(a)    # [[  1   2 100]
            #  [  4   5   6]]

# array.flatten()
# 다차원 배열을 1차원 배열로 펼침
# 결과를 복사본으로 반환(복사본 변경시 원본은 변경되지 않음)
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

flat = a.flatten()
print(flat) # [1 2 3 4 5 6 7 8]

flat[4] = 0
print(flat) # [1 2 3 4 0 6 7 8]
print(a)    # [[[1 2]
            #   [3 4]]
            #
            #  [[5 6]
            #   [7 8]]]

# np.expand_dims(a, axis)
# 지정한 위치에 차원 추가(차원 확장)
# 추가되는 차원은 1
a = np.array([[1,2,3],[4,5,6]]) # 2 x 3
print("원본:", a.shape)         # 원본: (2, 3)

# axis=0
a0 = np.expand_dims(a, axis=0)
print("a0", a0.shape)           # a0 (1, 2, 3)
print("a0", a0)
# [[[1 2 3]
#   [4 5 6]]]

# axis=1
a1 = np.expand_dims(a, axis=1)
print("a1", a1.shape)           # a1 (2, 1, 3)
print("a1", a1)
# [[[1 2 3]]
#
#  [[4 5 6]]]

# axis=2
a2 = np.expand_dims(a, axis=2)
print("a1", a2.shape)           # a1 (2, 3, 1)
print("a1", a2)
# [[[1]
#   [2]
#   [3]]
#
#  [[4]
#   [5]
#   [6]]]

# np.squeeze(a, axis)
# 배열에서 크기가 1인 차원을 제거해주는 함수(차원 축소)
a = np.array([[[[1],[2],[3]]], [[[1],[2],[3]]]])
print(a.shape)                  # (2, 1, 3, 1)
s = np.squeeze(a)
print(s)
# [[1 2 3]
#  [1 2 3]]
print(s.shape)                  # (2, 3)

# axis 지정하는 경우
a2 = np.zeros((1,4,1,2))
print(a2.shape)                 # (1, 4, 1, 2)

s1 = np.squeeze(a2, axis=0)
print(s1.shape)                 # (4, 1, 2)

s2 = np.squeeze(a2, axis=2)
print(s2.shape)                 # (1, 4, 2)

# 차원의 크기가 1이 아닌 차원은 제거할 수 X
# s3 = np.squeeze(a2, axis=1)  # ValueError: cannot select an axis to squeeze out which has size not equal to one

# np.unique() 
# 배열에서 중복된 요소를 제거
a = np.array([1,1,1,5,5,2,2,2,2,4,4,4,3,3,3])
u1 = np.unique(a) # 고유값의 오름차순 배열 반환
print(u1) # [1 2 3 4 5]

u2, idx, inv, cnt = np.unique(a, return_index=True, return_inverse=True, return_counts=True)
print("인덱스:", idx)                 # 인덱스: [ 0  5 12  9  3]
print("원본의 고유값 인덱스:", inv)    # 원본의 고유값 인덱스: [0 0 0 4 4 1 1 1 1 3 3 3 2 2 2]
print("값의 등장 횟수:", cnt)          # 값의 등장 횟수: [3 4 3 3 2]

# 실습1.
# 문제1. 아래의 배열을 사용해서
# ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
# arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요
arr = np.array([[10, 20], [30, 40], [50, 60]])

r = arr.ravel()
f = arr.flatten()
print("r:",r)    # r: [10 20 30 40 50 60]
print("f:",f)    # f: [10 20 30 40 50 60]

arr[0,0] = 999
print("r:",r)    # r: [999  20  30  40  50  60]
print("f:",f)    # f: [10 20 30 40 50 60]

# 문제2. 크기가 32x32인 이미지 데이터를 가정하고,
# 이 배열에 대해 expand_dims를 사용하여 shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img = np.random.rand(32, 32)
img2 = np.expand_dims(img, axis=0)
print(img2)         # array of shape (1, 32, 32) (랜덤 값들)
print(img2.shape)   # (1, 32, 32)

# 문제3.아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img = np.random.randint(0, 255, (1, 28, 28, 1))
result = np.squeeze(img)
print(result)       # array of shape (28, 28) (랜덤 정수)
print(result.shape) # (28, 28)

# 문제4. 아래 2차원 배열을 
# 1) 1차원 배열로 만든 후
# 2) 중복값을 제거한 뒤 shape (1, n)으로 재구성하세요.
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])
flat = arr.flatten()
print(flat)         # [3 1 2 2 1 2 3 1 2 2 1 4]
uniq = np.unique(flat)
print(uniq)         # [1 2 3 4]
result = uniq.reshape(1,-1) # -1을 입력할시 자동으로 계산해줌
print(result)       # [[1 2 3 4]]

# 문제5. 다음 배열을 shape (10,)로 만든 뒤 고유값 배열을 구하세요.
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]])  # shape (1, 10, 1)
s = np.squeeze(arr)
print(s)            # [1 3 2 1 3 2 3 1 2 3]
u = np.unique(s)
print(u)            # [1 2 3]

# 문제6. 다음 배열을 1차원 배열로 만든 후 고유값만 추출해서
# shape (고유값 개수, 1)인 2차원 배열로 변환하세요.
arr = np.array([ [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]],
                [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] ])  # shape (2, 3, 4)
flat = arr.flatten()
uniq = np.unique(flat)
print(uniq)         # [0 1 2 3 4 5 6 7 8]
print(uniq.shape)   # (9,)
reshaped = np.expand_dims(uniq, axis=1)
print(reshaped)
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]
print(reshaped.shape) # (9, 1)





# 배열의 결합과 분리

# np.concatenate((arr1, arr2, ...), axis=0)
# 배열 시퀀스를 결합
# 기존 구조 안에서 결합
a = np.array([[1,2],[3,4]]) # (2, 2)
b = np.array([[5,6]])          # (1, 2)

result1 = np.concatenate((a, b), axis=0)
print(result1)
# [[1 2]
#  [3 4]
#  [5 6]]
print(result1.shape) # (3, 2)

# 결합이 불가 → 겹합하는 axis를 제외한 나머지 차원이 같아야 함
# result2 = np.concatenate((a, b), axis=1)

c = np.array([[7],[8],[9]]) # (3, 1)
result3 = np.concatenate((result1, c), axis=1)
print(result3)
# [[1 2 7]
#  [3 4 8]
#  [5 6 9]]
print(result3.shape) # (3, 3)


# np.stack((arr1, arr2, ...), axis=0)
# 새로운 차원을 추가하면서 결합
a = np.array([1,2,3]) # (3,)
b = np.array([4,5,6])

# axis=0
s1 = np.stack((a, b), axis=0)
print(s1)
# [[1 2 3]
#  [4 5 6]]
print(s1.shape) # (2, 3)

# axis=1
s2 = np.stack((a, b), axis=1)
print(s2)
# [[1 4]
#  [2 5]
#  [3 6]]
print(s2.shape) # (3, 2)

# np.split()
# 배열을 여러개의 하위배열로 분할
a = np.arange(9)
s = np.split(a, 3)
print(a)       # [0 1 2 3 4 5 6 7 8]
print(s)       # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
print(s[0])    # [0 1 2]
print(s[1])    # [3 4 5]
print(s[2])    # [6 7 8]

# 배열을 같은 크기로만 나눌 수 있음
a = np.arange(9)
# s = np.split(a, 4)  # ValueError: array split does not result in an equal division

a = np.arange(16).reshape(4,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

s1 = np.split(a, [1,3])
for part in s1:
  print(part)
# [[0 1 2 3]]
# [[ 4  5  6  7]
#  [ 8  9 10 11]]
# [[12 13 14 15]]

s2 = np.split(a, 2, axis=1)
for part in s2:
  print(part)
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

# 실습2.
# 문제1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a,b)))
# [[1 2]
#  [3 4]
#  [5 6]]

# 문제2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
result = np.split(a,3)
for part in result:
  print(part) 
# [0 1 2 3]
# [4 5 6 7]
# [ 8  9 10 11]

# 문제3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

result = np.stack((a,b,c), axis=0)
print(result)
# [[1 2]
#  [3 4]
#  [5 6]]
print(result.shape) # (3, 2)

# np.sort(array)
# 정렬된 복사본 반환
# array.sort()
# 원본 배열을 정렬

# 1차원 배열
a = np.array([3,1,4,2])

# 정렬한 배열을 반환
s = np.sort(a)
print(s) # [1 2 3 4]
print(a) # [3 1 4 2]

# 원본을 정렬
a.sort()
print(a) # [1 2 3 4]

# 내림차순 : sort한 후 배열을 뒤집어야 함
print(a[::-1]) # [4 3 2 1]

# 2차원 배열 정렬
a = [[6,5,4],[3,1,2]]
s1 = np.sort(a, axis=0)
print(s1)
# [[3 1 2]
#  [6 5 4]]
s2 = np.sort(a, axis=1)
print(s2)
# [[4 5 6]
#  [1 2 3]]

# np.argsort()
# 정렬 인덱스를 반환
a = np.array([3,5,1,2,4])
idx = np.argsort(a)
print(idx)   # [2 3 0 4 1]
print(a[idx])# [1 2 3 4 5]

# 실습3.
# 문제1.아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
arr = np.array([7, 2, 9, 4, 5])
asc = np.sort(arr)
desc = np.sort(arr)[::-1]
print(asc)   # [2 4 5 7 9]
print(desc)  # [9 7 5 4 2]

# 문제2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[9, 2, 5],
                [3, 8, 1]])
print(np.sort(arr, axis=1))
# [[2 5 9]
#  [1 3 8]]

# 문제3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고,
# 그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
arr = np.array([10, 3, 7, 1, 9])
idx = np.argsort(arr)
s = arr[idx]
print(idx)    # [3 1 2 4 0]
print(s)      # [1 3 7 9 10]

# 문제4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[4, 7, 2],
                                [9, 1, 5],
                                [6, 8, 3]])

s = np.sort(arr, axis=0)
print(s)
# [[4 1 2]
#  [6 7 3]
#  [9 8 5]]