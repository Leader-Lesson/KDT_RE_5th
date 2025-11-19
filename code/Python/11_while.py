# #!/usr/bin/env python
# # coding: utf-8

# # ### 11. while문
# # - 조건이 True인 동안 코드를 반복하는 반복문
# # - 조건이 False가 되면 반복을 멈춤
# #   - 반복 횟수가 정해지지 않았을 때 사용




# # while문 기본 문법
# # 조건 : 참/거짓을 구분할 수 있는 문장 → True, False를 반환하는 문장이 와야 함

# # while 조건:
#   # 반복할 코드





# # 무한루프 
# # 사용시 주의해야 함
# # 반드시 종료조건이 있어야 함!
# while True:
#   print("반복중")





# # 예제1
# light = "green"

# while light == "green":
#   print("계속 가세요!")
#   light = input("신호등의 신호를 입력해주세요(green/yellow/red)")
# print("중지!!")





# import time

# # 예제2 : 별도의 반복 변수를 정의
# # ⚠️반복 변수를 갱신하지 않을시 무한루프에 빠지게 됨
# i = 0

# while i < 5:
#   print(i, "반복")
#   # i += 1
#   time.sleep(1)
# print("반복 종료")





# # 실습 1.
# # 문제 1.
# secret_code = "codingonre3"
# user_input = ""

# # 비밀코드와 사용자 입력이 같지 않을때 반복
# while user_input != secret_code:
#   user_input = input("비밀 코드를 입력하세요:")

# print("입장이 허용되었습니다!")





# import random

# # 문제 2.

# answer = random.randint(1,100)
# num = 0 # 사용자 입력 받을 변수
# time = 0 # 실행횟수를 저장할 변수

# # 사용자 입력과 정답이 같지 않을 때 반복
# while num != answer:
#   num = int(input("1~100사이의 수를 입력해주세요: "))
#   time += 1

#   if num > answer:
#     print(f"정답이 {num}보다는 작아요.")

#   elif num < answer:
#     print(f"정답이 {num}보다 커요.")

# print(f"{time}번 만에 정답을 맞췄습니다.")





# # 루프 제어문
# running = True
# while running:
#   if 조건1: 
#     running = False
#   if 조건2:
#     running = False

# # break
# while True:
#   if 조건:
#     break





# # 예제1
# i = 0

# while True:
#   print(i, "실행")
#   my_select = input("메뉴를 골라주세요:")

#   if my_select == "종료":
#     break

#   if i < 5:
#     break

#   i += 1
# print("반복문 종료")





# # 예제1-2
# i = 0

# while True:
#   i += 1
#   if i > 5:
#     break

#   print(i, "실행")
# print("반복문 종료")





# # 예제1-3
# i = 0

# while i < 6:
#   i += 1

#   print(i, "실행")
# print("반복문 종료")

# # 일반적으로 while의 조건에 따라 while문을 종료시키면 실행블록이 끝까지 실행 된후 종료되지만
# # break로 종료를 시키면, 이후 실행블록의 코드는 무시되고 바로 반복문을 탈출함





# # continue
# # 예제2
# i = 0 
# while i < 5:
#   i += 1
#   if i % 2 == 0:
#     continue
#   print(i)
# print("반복 종료")





# # 실습 2. 
# # 문제 1.
# secret_code = "codingonre3"
# user_input = ""

# # 비밀코드와 사용자 입력이 같지 않을때 반복
# while True:
#   user_input = input("비밀 코드를 입력하세요:")

#   if user_input == secret_code:
#     print("입장 완료! 환영합니다.")
#     break
#   else:
#     print("비밀 코드가 틀렸습니다. 다시 시도하세요.")





# # 문제 2.

# times = 0
# sum_age = 0

# while times < 5:
#   age = int(input("나이를 입력하세요: "))

#   # 나이가 0이하 이거나(또는), 120초과이면 건너뜀
#   if age <= 0 or age > 120:
#     continue

#   times += 1
#   sum_age += age

# print(f"총 나이 합계는 {sum_age}, 평균은 {int(sum_age / times)}")





# # 중첩 while문
# # 예제

# dan = 2
# while dan <= 9:
#   num = 1
#   print(f"[ {dan}단 ]")

#   while num <=9:
#     print(f"{dan} x {num} = {dan * num}") 
#     num += 1

#   print()
#   dan += 1
  
  
# # 중첩 while문 반복문 제어 예시
# # - 해당 제어문이 쓰인 반복문 안에서만 유효하다

# dan = 2
# while dan <= 9:
#     num = 1
#     print(f"[ {dan}단 ]")
    
#     while num <= 9:
#         num += 1
#         if num % 2 != 0:
#             break
#         else:
#             print(f"{dan} X {num} = {dan * num}")
        
            
#     print()
#     dan += 1





# # 실습3
# # 아이디와 비밀번호를 저장할 변수
user_id = "codingon"
user_pw = "abc123"

# # 1) ID 먼저 검사하는 경우
# while True:
#   # 아이디 확인
#   id_input = input("ID를 입력하세요: ")

#   # 아이디가 일치하지 않을시
#   if id_input != user_id:
#     print("ID가 일치하지 않습니다.")
#     continue

#   while True:
#     # 비밀번호 확인
#     pw_input = input("비밀번호를 입력하세요: ")

#     if pw_input != user_pw:
#       print("비밀번호가 일치하지 않습니다.")
#       continue

#     print("로그인 성공!")
#     break

#     # if pw_input == user_pw:
#     #   print("로그인 성공")
#     #   break

#     # print("비밀번호가 일치하지 않습니다.")
#     # continue

#   break




# 2) ID, PW 동시에 받는 경우

user_id = "codingon"
user_pw = "abc123"

while True:   # 전체 프로그램 반복
  print("=== 로그인 화면 ===")
  print("1. 로그인")
  print("2. 종료")
  main_sel = input("선택: ")

  if main_sel == "2":
    print("프로그램을 종료합니다.")
    break  # 바깥 while 종료 → 프로그램 끝

  elif main_sel != "1":
    print("잘못 선택하셨습니다.\n")
    continue

  # 여기서부터 로그인 과정
  id_input = input("ID : ")
  pw_input = input("PW : ")

  if id_input != user_id or pw_input != user_pw:
    print("로그인 실패! 다시 시도해주세요.\n")
    continue

  print("로그인 성공!\n")

  # 로그인 후 메뉴 화면
  while True:
    print("===== 메뉴 =====")
    print("1. 정보 보기")
    print("2. 설정")
    print("3. 로그아웃")
    print("================")

    sel = input("메뉴 선택: ")

    if sel == "1":
      print("회원 정보입니다.\n")
      continue

    elif sel == "2":
      print("설정 메뉴입니다.\n")
      continue

    elif sel == "3":
      print("로그아웃합니다.\n")
      break  # 안쪽 while만 끊고 로그인 화면으로

    else:
      print("잘못 입력하셨습니다.\n")
      continue




