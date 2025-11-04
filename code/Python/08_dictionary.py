#!/usr/bin/env python
# coding: utf-8

# ### 08. 딕셔너리
# - **키-값 쌍**으로 묶어 데이터를 저장하는 자료형
# - 키는 유일해야함. 값은 중복 가능
# - 변경가능한 자료형
# - 순서가 보장되지 않았다가 → py 3.7버전 이후 순서가 보장됨

# In[ ]:


# dict 만들기
d1 = {} # 빈 dict 만들기
print(d1, type(d1))

person = { "name" : "Ian", "age" : 25 }
print(person)

# dict 함수로 생성
d2 = dict() # 빈 dict 만들기
print(d2, type(d2))

# 키가 문자열 일 때 가능
movie = dict(title="interstellar", director="christopher nolan")
print(movie)

# 리스트나 튜플로 만들기
pairs = [("name", "ian"), ("age", 150), ("job", "developer")]
person2 = dict(pairs)
print(person2)

# zip 함수 활용
keys = ["title", "director", "year"]
values = ["기생충", "봉준호", "2019"]
# print(list(zip(keys, values)))
movie2 = dict(zip(keys, values))
print(movie2)


# In[ ]:


# 키로 사용할 수 없는 자료형
# 키는 불변자료형을 사용해야함
d1 = {(1,2,3) : (1,2,3)} # 튜플 사용 가능
d2 = { 1 : 10 }

d3 = {{1,2,3}: "리스트를 키로?"} # 가변 자료형은 키로 사용 불가능
d3


# In[ ]:


# dict 데이터 조회
person = { "name" : "Ian", "age" : 25, "job" : "developer" }

# 키를 통해 데이터 조회
print(person["name"])
print(person["age"])
# print(person["city"]) # 존재하지 않는 키로 조회 → KeyError

# get 메서드를 활용한 조회
print(person.get("name"))
print(person.get("job"))
# 존재하지 않는 키로 조회
print(person.get("email")) # default 지정 안 할 시 none 출력
print(person.get("email", "이메일이 존재하지 않습니다")) # default 값 지정 가능


# In[ ]:


# get 사용 예제
user_data = {
  "username" : "ian_leader",
  "email" : "ian@spreatics.com",
  "password" : "abc123"
}

key = input("조회할 정보를 입력하세요(username, email, password): ")
result = user_data.get(key, "존재하지 않는 데이터입니다.")
print(result)


# In[ ]:


# 데이터 추가 및 수정
user_data = {
  "username" : "ian_leader",
  "email" : "ian@spreatics.com",
}

# 기본적인 추가&수정 방법 
user_data["nickname"] = "예민왕"
user_data["username"] = "ian_superman"
# print(user_data)

# update 메서드 활용
movie_data = {
  "title" : "Superman",
  "director" : "James Gunn"
}

movie_data.update({
  "year" : 2025,
})

# 키가 문자열인 경우
movie_data.update(actor="배우 이름 뭐였더라..")

# 다른 딕셔너리 추가
extra_data = {"rating" : "4.0 / 5.0", "actor" : "뭐시기 브로스나한?"}
movie_data.update(extra_data)
print(movie_data)

# setdefault
movie_data.setdefault("year", "알 수 없음")
movie_data.setdefault("제작사", "DC_스튜디오")
print(movie_data)

# 데이터 삭제
del movie_data["actor"]
print(movie_data)

# 키로 제거
rating = movie_data.pop("rating")
print(movie_data, rating, sep=" /// ")

# 가장 마지막 요소 제거 : 키, 값 쌍 반환
year = movie_data.popitem()
print(movie, year, sep=" /// ")

# dict 비우기
movie_data.clear()
print(movie_data)

# dict 삭제하기
del movie_data
# print(movie_data) # NameError 발생


# In[3]:


# 딕셔너리 메서드
user_data = {
  "username" : "ian_leader",
  "email" : "ian@spreatics.com",
  "password" : "abc123"
}

# keys : 모든 키를 반환
print("키", list(user_data.keys())) # 리스트로 변환해서 출력

# values : 모든 값을 반환
print("값", list(user_data.values())) # 리스트로 변환해서 출력

# items : 모든 키값쌍을 반환
print("쌍", list(user_data.items())) # 리스트로 변환해서 출력


# In[51]:


# 문제1
# 1단계: 빈 딕셔너리 생성 : user라는 이름의 빈 딕셔너리를 생성하세요.
user = {}

# 2단계: 사용자 기본 정보 추가 
# "username": "skywalker"
# "email": "sky@example.com"
# "level": 5
# user["username"] = "skywalker"
# user["email"] = "sky@example.com"
# user["level"] = 5
user.update({
  "username": "skywalker",
  "email": "sky@example.com",
  "level": 5
})
print(user)

# 3단계: 값 읽기 - "email" 값을 변수 email_value에 저장하고 출력하세요.
email_value = user["email"]
print(email_value)

# 4단계: 값 수정 - "level" 값을 6으로 수정하세요.
user["level"] = 6

# 5단계: 안전하게 키 조회 
# 딕셔너리에 "phone" 키가 없다면 "미입력"이라는 문자열을 출력하도록 하세요.
phone = user.get("phone", "미입력")
print(phone)

# 6단계: 항목 추가 및 삭제
# update()를 사용해 "nickname": "sky" 항목을 추가하세요.
# "email" 항목을 삭제하세요.
# "signup_date" 키가 없다면 "2025-07-10"으로 추가하세요 (setdefault() 사용).
# 최종 user 딕셔너리를 출력하세요.
user.update(nickname="sky")
user.pop("email")
user.setdefault("signup_date", "2025-07-10")

print(user)


# In[53]:


# 문제2
# 1. 빈 딕셔너리 생성
students = {}

# 2. "Alice", "Bob", "Charlie" 세 학생의 점수를 각각 85, 90, 95로 추가한다.
students.update(Alice=85, Bob=90, Charlie=95)

# 3. "David" 학생의 점수(80)를 추가한다.
students["David"] = 80

# 4. "Alice"의 점수를 88로 수정한다.
students["Alice"] = 88

# 5. "Bob"을 딕셔너리에서 삭제한다.
students.pop("Bob")

# 6. 최종 students 딕셔너리를 출력한다.
print(students)

