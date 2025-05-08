
# 1단계 : 출력과 변수
# ex1) 제 이름은 OOO이고, 나이는 XX살입니다.

def test1():
    name = "최호림"
    age = 26
    print(f"제 이름은 {name}이고, 나이는 {age}살 입니다.")
# test1()

# ex2)
# x = 5
# y = 3
# z = x + y
def test2():
    x = 5
    y = 3
    z = x + y
    print(f"x는 {x}이고, y는 {y}이기에 둘이 더하면 {z}이다")
# test2()

# ex3) 10과 20을 더한 결과는 30입니다.
def test3():
    a = 10
    b = 20
    c = a + b
    print(f"{a}과 {b}을 더한 결과는 {c}입니다.")
# test3()

# 2단계 : 데이터 타입
# ex1) 좋아하는 음식 3가지를 리스트로 만들어 출력해보세요.
def test4():
    food = ["순두부 찌개", "제육볶음", "도가니탕"]
    print(f"제가 좋아하는 음식은 {food}입니다.")
# test4()

# ex2) 사람의 정보를 딕셔너리로 표현해보세요. (이름, 나이, 학교)
def test5():
    person = {"name": "최호림", "age": 26,"school": "서울호서직업전문학교"}
    print(f"제 이름은 {person['name']}이고, 나이는 {person['age']}살이며, 다니는 학교는 {person['school']}입니다.")
# test5()

# ex3)아래 리스트에서 두 번째 값을 출력해보세요.
def test6():
    colors = ["빨강", "초록", "파랑"]
    print(f"리스트의 두 번째 값은 {colors[1]}입니다.")
# test6()

# 3단계 : 조건문
# ex1) 사용자에게 나이를 입력받아,
# 19세 이상이면 "성인입니다", 아니면 "청소년입니다"라고 출력하는 코드를 작성하세요.
def test7():
    age = int(input("나이를 입력해주세요 => "))
    if age >= 19:
        print("성인입니다.")
    else:
        print("청소년입니다.")
# test7()

# ex2) 두 숫자 중 어떤 숫자가 더 큰지 판별해서 출력하는 프로그램을 만드세요.
def test8():
    num1 = int (input("첫 번째 숫자를 입력하세요 => "))
    num2 = int (input("두 번째 숫자를 입력하세요 => "))
    if num1 > num2:
        print(f"{num1}이 {num2}보다 큽니다.")
    elif num1 <  num2:
        print(f"{num2}이 {num1}보다 큽니다.")
    else:
        print("두 숫자는 같습니다.")
# test8()

# ex3) 점수를 입력받아 다음 기준에 따라 학점을 출력하는 코드를 작성하세요.
def test9():
    num = int(input("점수를 입력하세요 => "))
    if num >= 90:
        print("A학점입니다.")
    elif num >= 80:
        print("B학점입니다.")
    elif num >= 70:
        print("C학점입니다.")
    else:
         print("F학점입니다.")
# test9()

# 4단계 : 반복문
# ex1) 1부터 10까지 출력하는 프로그램을 작성하세요. (for 사용)
def test10():
 for i in range(1,11):
    print(i)
# test10()

# ex2) 다음 리스트의 값을 하나씩 출력해보세요.
def test11():
    animals = ["강아지", "고양이", "토끼"]
    for animals in animals:
        print(animals)
# test11()

# ex3) 사용자로부터 숫자 하나를 입력받아, 그 숫자만큼 "Hello"를 출력하세요. (while 사용)
def test12():
    num = int(input("숫자를 입력하세요 => "))
    cont = 0
    while cont < num:
        print("Hello")
        cont += 1
# test12()

# 5단계 : 함수
def test13(a,b):
    return a + b

# ex1)
# 두 수를 더해서 결과를 반환하는 함수를 작성하세요.
result = test13(3, 5)
print(f" 3 + 5 = {result}")

# ex2)
# 이름을 전달하면 "안녕하세요, OOO님!"이라고 출력하는 함수를 작성하세요.
def test14(name):
    print(f"안녕하세요, {name}님!")
# test14("최호림")

# ex3)
# 리스트를 전달받아 평균을 계산해 출력하는 함수를 작성하세요.
list = [30,40,50,60,70]
list1 = ["국어", "영어", "수학", "과학", "사회"]
def test15(list):
    sum = 0
    for i in list:
        sum += i
        avg = sum / len(list)
        for j in list1:
            j = list1[list.index(i)]
            print(f"{j}의 평균은 {avg}입니다.")
            break
# test15(list)

# 구구단 여러방면 구현해보기
# [1] 기본 구구단 (한 단만)
def test16():
    for j in range(1, 10):
        print(f" 2 X {j} = {2 * j}")
test16()

# [2] 사용자로부터 단 입력받기
def test17():
    dan = int(input("원하는 단을 입력하세요 =>"))
    for j in range(1, 10):
        print(f"{dan} X {j} = {dan * j}")
test17()

# [3] 함수로 구구단 출력
def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} X {i} = {dan * i}")
gugudan(6)

# [4] 전체 구구단 출력
def all_gugudan():
    for dan in range(1, 10):
        print("======================")
        print(f"{dan} 단")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan * i}")
all_gugudan()

# [5] 표 형식 구구단 출력
def gugudan_print():
    for i in range(2, 10):
        print(f"========= {i}단 =========")
        for j in range(1, 10):
            print(f"{i} X {j} = {i * j}", end="\t")
        print()
gugudan_print()

# [6] 사용자 입력 + 전체 구구단 함수화
def print_gugudan_all():
    for dan in range(2, 10):
        print(f"========= {dan}단 =========")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan * i}", end="\t")
        print()

def print_gugudan_one(dan):
    if 2 <= dan <= 9:
        print(f"========= {dan}단 =========")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan * i}", end="\t")
    else:
        print("2단 ~ 9단까지만 입력이 가능합니다.")

mode = input("전체 출력은 all, 하나의 단 출력은 one => ")

if mode == "all":
    print_gugudan_all()
elif mode == "one":
    d = int(input("원하는 단을 입력하세요 => "))
    print_gugudan_one(d)
else:
    print("잘못된 입력입니다.")

# [7] 홀수 단만 출력하기
def odd_gugudan():
    for dan in range(3, 10, 2):
        print(f"========= {dan}단 =========")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan * i}", end="\t")
odd_gugudan()

# [8] 짝수 곱만 출력하기(2단 ~ 9단중에서)
def even_gugudan():
    for dan in range(2, 10):
        print(f"========= {dan}단 =========")
        for i in range(1, 10):
            result = dan * i
            if result % 2 == 0:
                print(f"{dan} X {i} = {result}", end="\t")
even_gugudan()








