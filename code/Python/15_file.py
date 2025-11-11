#!/usr/bin/env python
# coding: utf-8

# ### 15. 파일 입출력
# - 저장장치에 저장된 파일을 읽어오거나 저장하는 작업




# 파일 열기와 닫기
# 파일 열기 : open()
# open("파일경로", mode="r", encoding="원하는인코딩")
# open으로 파일을 읽으면 '파일객체'를 반환함
f = open("example.txt", "w", encoding="utf-8")

f.write("파이썬 파일 입출력 예제입니다.\n")
f.write("파이썬 공부 너무너무 재밌어요.")

# 파일 닫기 : close()
# 열린 파일을 닫아 시스템 자원을 해제함 
f.close()





# 파일 읽기
# read() : 전체 내용을 한번에 읽기
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()





# readline() : 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print("첫번째 줄:", line1.strip())
print("두번째 줄:", line2)
f.close()





# for문으로 읽기
f = open("example.txt", "r", encoding="utf-8")
for line in f:
  print(line.strip())
f.close()





# readlines() : 모든 줄을 한번에 리스트로 읽기
f = open("example.txt", "r", encoding="utf-8")
contents = f.readlines()
print(contents)
f.close()





# tell() : 현재 읽고 있는 위치(바이트)를 반환
f = open("example.txt", "r", encoding="utf-8")
print("처음 위치:", f.tell())
f.read(5)
print("5바이트 읽은 후 위치:", f.tell())
f.close()





# seek() : 파일 포인터 위치를 이동
f = open("example.txt", "r", encoding="utf-8")
print(f.read(10))
f.seek(0)
print(f.read())
f.close()





# 파일 쓰기
# 파일 쓰기 모드 : 'w' vs 'a'
# w모드 : 덮어쓰기
f = open("example.txt", "w", encoding="utf-8")
f.write("파이썬 파일 입출력 예제입니다.\n")
f.write("파이썬 공부 너무너무 재밌어요.")
f.close()





# a모드 : 추가쓰기
f = open("example.txt", "a", encoding="utf-8")
f.write("\n추가한 내용입니다.")
f.close()





# with문
# 파일 입출력시에 자동으로 close()를 호출해주는 구문
# 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
  f1.write("with문으로 작성한 파일이에요.\n")
  f1.write("파일입출력 짱 쉬움.")





# 파일 읽기
with open("with_example.txt", "r", encoding="utf-8") as f2:
  data = f2.read()
  print(data)





# 예제1. 파일에서 랜덤 추출하기
with open("words.txt", "w", encoding="utf-8") as f1:
  words = [
      "apple", "banana", "orange", "grape", "lemon",
      "peach", "melon", "cherry", "plum", "pear",
      "school", "friend", "family", "flower", "garden",
      "window", "bottle", "pencil", "summer", "winter",
      "happy", "future", "travel", "animal", "market",
      "doctor", "planet", "energy", "nature", "memory"
  ]
  for i in words:
    f1.write(i + "\n")





import random

with open("words.txt", "r", encoding="utf-8") as f2:
  data = f2.readlines()
  for i in range(5):
    word = random.choice(data).strip()
    print(word)





# 예제2. 입력 받아 파일 쓰기
with open("with_example.txt", "a", encoding="utf-8") as f3:
  while True:
    text = input("저장할 내용을 입력해주세요(종료 : z):")
    if text == "Z" or text == "z":
      break
    f3.write(text + "\n")





# 실습1. 회원 명부 작성하기
# 회원 정보 3개를 파일에 기록
with open("member.txt", "a", encoding="utf-8") as f:
  for i in range(3):
    name = input(f"{i+1}번째 회원의 이름: ")
    password = input(f"{i+1}번째 회원의 비밀번호: ")
    f.write(f"이름: {name}, 비밀번호: {password}\n")

# 파일에 저장한 회원 명부 출력
with open("member.txt", "r", encoding="utf-8") as f:
  print("[회원명부]")
  print(f.read())



# 실습2~3. 회원 명부를 이용한 로그인 기능
import os

input_name = input("이름을 입력하세요: ")
input_password = input("비밀번호를 입력하세요: ")

login = False

with open("member.txt", "r", encoding="utf-8") as f:
  for line in f:
    parts = line.strip().split(",")
    name = parts[0].split(":")[1].strip()
    password = parts[1].split(":")[1].strip()

    if input_name == name and input_password == password:
      login = True
      break

if login:
  print("로그인 성공!")
  user_phone = input("전화번호를 입력하세요: ")

  phone_data = {}
  if os.path.exists("member_tel.txt"):
    with open("member_tel.txt", "r", encoding="utf-8") as f:
      for line in f:
        parts = line.strip().split(",")
        name = parts[0].split(":")[1].strip()
        phone = parts[1].split(":")[1].strip()
        phone_data[name] = phone

  phone_data[input_name] = user_phone

  with open("member_tel.txt", "w", encoding="utf-8") as f:
    for name, phone in phone_data.items():
      f.write(f"이름: {name}, 전화번호: {phone}\n")

  print("전화번호가 저장되었습니다.")

else:
  print("로그인 실패")


# 바이너리 파일 읽기
with open("./images/dog.jpg", "rb") as f:
  img = f.read()
  print(img)

# 바이너리 파일 쓰기
with open("./output/dog_copy.jpg", "wb") as f:
  f.write(img)




# 예외처리
try:
  num = int(input())
  print(10/num)
except ValueError as v:
  print("숫자가 아닙니다", v)
except ZeroDivisionError as z:
  print("0으로 나눌 수 없습니다", z)

