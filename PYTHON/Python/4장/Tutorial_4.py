print("========== 함수 ==========")
print("[가장 단순한 함수]")
def say_hello(): # 그냥 정해진 문구만 출력하는 함수입니다.
    print("안녕하세요! 반가워요.")
say_hello()

print("[매개변수가 있는 함수]")
def greet(name): # 데이터를 전달받아 처리하는 함수입니다.
    print(f"{name}님, 환영합니다!")
greet("철수")

print("[반환값이 있는 함수]")
def add(a,b):
    return a+b
result = add(5,3)
print(result)

print("========== 사용자 입출력 ==========")
print("[input()함수]")
name = input("이름을 입력하세요: ")
print(name + "님, 안녕하세요!")
print("⚠️ 주의: 숫자 입력받기")
age = input("나이를 입력하세요: ") # print(age + 1)  <- 에러 발생! (문자와 숫자는 더할 수 없음)
# 정수로 변환 후 계산
age_int = int(age)
print(f"내년에는 {age_int + 1}살이 되시는군요!")

print("[print()함수]")
print("여러 값 출력하기")
print("Life", "is", "too short") # 결과: Life is too short
print("문자열 연결하기")
print("Python" + "is" + "Fun") # 결과: PythonisFun

print("[더 편리한 f-string]")
apple_count = 5
print(f"나는 사과를 {apple_count}개 먹었습니다.")

print("간단한 더하기 계산기")
# 1. 두 수를 더하는 함수 정의
def add_numbers(n1, n2):
    return n1 + n2
# 2. 사용자로부터 입력 받기
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
# 3. 함수 호출 및 출력
result = add_numbers(num1, num2)
print(f"두 수의 합은 {result}입니다.")

print("========== 파일 읽고 쓰기 ==========")
print("파일 생성하기")
f = open("새파일.txt", 'w') # r(읽기모드), w(쓰기모드), a(추가모드)
f.close()
print("‘새파일.txt’ 파일을 C:/doit 디렉터리에 생성")
f = open("C:/doit/새파일.txt", 'w')
f.close()
print("파일을 쓰기 모드로 열어 내용 쓰기")
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
print("[파일을 읽는 여러 가지 방법]")
print("readline 함수 이용하기")
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
##만약 모든 줄을 읽어 화면에 출력하고 싶다면
# f = open("C:/doit/새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

print("readlines 함수 사용하기")
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

print("read 함수 사용하기")
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

print("파일 객체를 for 문과 함께 사용하기")
f = open("C:/doit/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

print("원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우")
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print("[with 문과 함께 사용하기]")
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

print("파일을 열고 닫는 것을 자동으로 처리")
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

print("with 문과 스코프(Scope) 규칙")
print("1. 함수 스코프") # 함수 안에서 선언된 변수는 함수 밖에서 접근할 수 없다.
def my_function():
    func_var = "함수 안의 변수"

my_function()
# print(func_var)  # 오류! 함수 밖에서는 접근 불가

print("2. 블록 스코프") # if, for, while, with 등의 블록 안에서 선언된 변수는 블록 밖에서도 접근할 수 있다.
# if 문 블록의 예
if True:
    if_var = "if 블록 안의 변수"

print(if_var)  # 정상 작동! "if 블록 안의 변수" 출력

# for 문 블록의 예
for i in range(3):
    loop_var = "반복문 안의 변수"

print(i)         # 정상 작동! 2 출력
print(loop_var)  # 정상 작동! "반복문 안의 변수" 출력

# with 문에서 변수 사용 예제
with open("test.txt", "w") as f:
    content = "Hello, Python!"  # with 블록 내에서 변수 선언
    f.write(content)

# with 블록을 벗어난 후에도 변수에 접근 가능
print(content)  # "Hello, Python!" 출력

print("[파일 처리 시 주의사항]")
# 한글 파일 쓰기
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")
# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print("========== sys 모듈 사용하기 ==========")
import sys
args = sys.argv[1:]
for i in args:
    print(i)
# 터미널에 python sys1.py aaa bbb ccc 라고 입력

print("모두 대문자로 바꾸어 주는 간단한 프로그램")
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# 터미널에 python sys2.py life is too short, you need python 라고 입력