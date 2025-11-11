#!/usr/bin/env python
# coding: utf-8

# ### 07. set(집합)
# - 원소의 중복을 허용하지 않는 여러 데이터의 모음
# - 순서가 없는 컬렉션 자료형




# set 만들기
s1 = {1, 2, 3}
print(s1, type(s1))

s2 = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4}
print(s2)

# 빈 set 만들기
# 🚨유의사항 : 중괄호에 원소를 넣지 않고 선언하면 
# 빈 dict로 인식됨
s3 = {}
print(type(s3))

# set 함수로 생성
s4 = set()
print(s4, type(s4))

# 💡set 함수의 활용 : 원소의 중복 제거
my_list = [1,1,2,2,2,2,2,3,3,3,3,4,4,4,10,10,10,10]
s5 = set(my_list) # set으로 변환 → 중복 원소 제거
print(s5)
my_list = list(s5)
print(my_list, type(my_list))





# 인덱싱
s1 = {10,20,30}
# s1[1]

s_list = list(s1) # 변환하는 과정에서 순서가 보장되지 않을 수 있음
s_list[2]





# 자료형 제한
# 가변 자료형은 원소로 사용할 수 없음
s1 = {1,2,3,[1,2,3],[4,5,6]}





# set 연산
# 집합의 연산 : 합집합, 교집합, 차집합, 대칭차집합
a = {1,2,3}
b = {3,4,5}

# 합집합(|, .union)
s_union1 = a | b
s_union2 = a.union(b)
print("합집합1", s_union1)
print("합집합2", s_union2)

# 교집합(&, .intersection)
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합1", s_inter1)
print("교집합2", s_inter2)

# 차집합
s_diff1 = a -b
s_diff2 = a.difference(b)
print("차집합1", s_diff1)
print("차집합2", s_diff2)

# 대칭차집합
s_symm1 = (a | b) - (a & b)
s_symm2 = a ^ b
s_symm3 = a.symmetric_difference(b)

print("대칭차집합1", s_symm1)
print("대칭차집합2", s_symm2)
print("대칭차집합3", s_symm3)





# set 메서드
s1 = {1, 2, 3}

# 원소 추가
s1.add(4)
print("원소 추가", s1)

# 여러 원소 추가
s1.update((5,6,7))
print("여러 원소 추가", s1)

# 원소 제거
s1.remove(4)
print("원소 제거1", s1)
# s1.remove(100) # 존재하지 않는 원소 삭제시도시 에러
s1.discard(100)
s1.discard(6)
print("원소 제거2", s1)
deleted = s1.pop() # 임의의 값 하나 제거
print("원소 제거3", s1, deleted)





# 부분집합(subset) 관련 메서드
a = {10, 20, 30, 40, 50} # 상위집합(superset)
b = {20, 30, 40} # 부분집합(subset)
c = {10, 200, 300, 400, 500}

# 부분집합 여부 판단
print(b.issubset(a))
print(a.issubset(b))

# 상위집합 여부 판단
print(a.issuperset(b))
print(b.issuperset(a))

# 공통 원소가 없는지 확인
print(a.isdisjoint(b))
print(a.isdisjoint(c))
print(b.isdisjoint(c))





# 문제 1. 중복 제거 및 개수 세기 
# 어떤 학급의 학생들이 제출한 팀 과제 파일 이름 목록이 아래와 같습니다.
# 중복 제출된 경우도 포함되어 있습니다.
# 중복을 제거한 후, 총 몇 명이 제출했는지 출력하는 프로그램을 작성하세요.
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']

unique_studnets = set(submissions)

# 학생수
print(f"제출한 학생수: {len(unique_studnets)}") 
# 제출자명단
print(f"제출자 명단: {unique_studnets}")



# 문제 2. 공통 관심사 찾기
# 두 명의 사용자가 각자 좋아하는 영화 장르를 아래와 같이 입력했습니다.
# 두 사용자의 공통 관심 장르, 서로 다른 장르, 모든 장르 목록을 출력하세요.
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

# 공통 관심 장르(교집합)
common = user1 & user2

# 서로 다른 장르(대칭차집합)
diff = user1 ^ user2

# 모든 장르 목록(합집합)
total = user1 | user2

print(f"공통 관심 장르: {common}")
print(f"서로 다른 장르: {diff}")
print(f"모든 장르 목록: {total}")



# 문제 3. 부분집합 관계 판단
# 어떤 유저가 가지고 있는 자격증 목록과 특정 직무에 필요한 자격증 목록이 주어집니다.
# 이 사용자가 지원 자격을 갖추었는지 확인하세요.
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

# 지원 자격 충족 여부
is_qualified = job_required.issubset(my_certificates)

print(f"지원 자격 충족 여부: {is_qualified}")

