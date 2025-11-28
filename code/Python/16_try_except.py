# 예외처리
# - 에러: 프로그램이 실행이 되지 않게 하는 문제
# - 예외: 에러가 발생될 것 같은 부분을 예외로 처리
# => 프로그램이 예기치 않게 종료되는 것을 방지

# 예외 처리 기본 문법
try:
  # 예외가 발생할 수 있는 코드
  pass
except:
  # 예외가 발생했을 때 실행할 코드
  # 특정 에러를 지정 가능
  pass

# 예외 종류
# 1. 인덱스 에러
# - 리스트 인덱스 범위 오류
shop = ['반팔', '청바지', '이어폰', '키보드']
print(shop[2])
# print(shop[10]) # IndexError: list index out of range
print("예외 처리")

# 2. ValueError
# - 부적절한 값을 가진 인자를 받았을 때 발생
# number = int("hello") # ValueError: invalid literal for int() with base 10: 'hello'
# print(shop.index("x")) # ValueError: 'x' is not in list

# 3. ZeroDivisionError
# - 0으로 나눌 때 발생
# print(5 / 0) # ZeroDivisionError: division by zero

# 4. NameError
# - 존재하지 않는 변수를 호출할 때
# print(x) # NameError: name 'x' is not defined

# 5. FileNotFoundError
# - 존재하지 않는 파일을 호출할 때
# file = open('test.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'



# 예외 처리
# 1) 단일 except
# try:
#   num = int(input("숫자를 입력하세요: "))
#   print(10 / num)
# except:
#   print("예외 발생")
  
# 2) 특정 예외 처리
try:
  num = int(input("숫자를 입력하세요: "))
  print(10 / num)
except ValueError as e:
  print("숫자가 아닙니다", e)
except ZeroDivisionError as e:
  print("0으로 나눌 수 없습니다", e) 
  
  
# 예외 처리 구조
'''
try:
  # 예외가 발생할 수 있는 코드
except 오류내용1:
  # 예외가 발생했을 때 실행할 코드
  # 특정 에러를 지정 가능
except 오류내용2:
  # 특정 에러2
else:
  # 예외 없는 경우에 실행
finally:
  # 예외 발생 여부와 상관없이 실행
'''



# 실습 1
answer = input('Enter a number: ')

try:
  num = int(answer)
except:
  num = -1

if num > 0:
  print('0보다 큽니다!')
else:
  print('숫자가 아닙니다!')
  
  

# 실습 2
def print_result(n1, op, n2, result):
  print(f"{n1} {op} {n2} = {result}")

while True:
  try:
    num1 = float(input("첫 번째 숫자: "))
    op = input("연산자(+ - * /): ")
    num2 = float(input("두 번째 숫자: "))
    
    if op not in ['+', '-', '*', '/']:
      raise ValueError("잘못된 연산자입니다.")
    
    if op == '/' and num2 == 0:
      raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    
    # 계산
    if op == '+':
      result = num1 + num2
    elif op == '-':
      result = num1 - num2
    elif op == '*':
      result = num1 * num2
    else:
      result = num1 / num2
      
    print_result(num1, op, num2, result)
    break
  except ValueError:
    print("입력이 잘못되었습니다. 다시 입력하세요.\n")
  except ZeroDivisionError as e:
    print(e)
    print("다시 입력하세요.\n")
  except Exception:
    print("알 수 없는 오류가 발생했습니다.\n")