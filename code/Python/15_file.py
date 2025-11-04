# 파일 입출력 예제

# 파일 생성 및 쓰기
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example in Python.\n")

# 파일 읽기
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 파일 추가 쓰기
with open("example.txt", "a") as file:
    file.write("Appending a new line to the file.\n")

# 파일 읽기 (추가된 내용 포함)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 파일 삭제
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("example.txt has been deleted.")
else:
    print("The file does not exist.")