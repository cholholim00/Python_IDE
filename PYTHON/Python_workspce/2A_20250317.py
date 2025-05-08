def test1():
    a = int(10.3)
    b = float(10.3)
    c = str((b))
    print(a,b,c)
    print(type(a), type(b), type(c))
# test1()

def test2():
    # print("오늘의 점심은 뭘 먹을까?")
    # food = input()
    # print(f"yo~~~{food} 낫베드!")
    
    # food = input("오늘 점심 메뉴는?")
    # print(f"오늘의 점심은{food}이구나")
    
    print("당신의 이름과 나이와 학년은?")
    name = input()
    age = input()
    grade = input()
    grade = int(grade)
    print(f"당신의 이름은 {name}이고 나이는{age}이고 학년은{grade}이군요")
    print(type(name),type(age),type(grade))
# test2()

def test3():
    age = int(input("당신의 나이는 몇살입니까?"))
    if age >= 40:
        print("입장가능합니다 행님")
    else:
        print("입장불가해요 선생님 돌아가세요") 
# test3()
    
def test4():
    score = int(input("당신의 점수를 입력하세요"))
    
    if score >= 90:
        print('A학점')
    elif score >= 80:
         print('B학점')
    elif score >= 70:
         print('C학점')
    elif score >= 60:
       print('D학점')
    elif score < 60:
        print('F학점')
# test4()


def test5():
    
    ko = int(input("당신의 국어점수를 입력하세요"))
    en = int(input("당신의 영어점수를 입력하세요"))
    ma = int(input("당신의 수학점수를 입력하세요"))
    
    hap = int(ko+en+ma) / 3
    
    if hap >= 90:
        grade = 'A'
    elif hap >= 80:
          grade = 'B'
    elif hap >= 70:
         grade = 'C'
    elif hap >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"국어:{ko},수학:{ma},영어:{en},등급:{hap}")
# test5()


def test6():
    year = int(input("당신이 태어난 연도를 입력하세요."))
    age = 2025 - year + 1
    
    if age <= 26 and age >= 20:
        grade = '대학생'
    elif age <= 17 and age < 20:
          grade = '고등학생'
    elif age <= 14 and age < 17:
         grade = '중학생'
    elif age <= 8 and age < 14:
        grade = '초등학생'
    else:
        grade = '학생이 아직 아닙니다'
        
    print(f"당신은{age}입니다.")
# test6()
    

def test7():
    # for looper in [1,2,3,4,5]:
        
    #     print(looper,": hello")
    
    # for looper in range(0,100):
    #     print(looper)
    
     # sum = 0
    # for looper in range(1,101,1):
    #     sum += looper
    #     print(sum)
    
    even_sum = 0
    odd_sum = 0
    for i in range(1,101,1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        print(f"짝수의합:{even_sum},홀수의합:{odd_sum}")      
# test7()
    
def test8():
    first = int(input("시작값: "))
    last = int(input("끝값: "))
    even_sum = odd_sum = 0
    for i in range(first, last+1, 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        print(f"{first}부터, {last}사이의 홀수의 합은:{odd_sum},짝수의 합은:{even_sum}")    
# test8()   
    
def test9():
     i = 1 
     sum = 0
     while i <=100:
         sum += i
         i += 1
        
     print(sum)    
# test9()
     
def test10():
    sum = 0 
    even_sum = odd_sum = 0
    first = int(input("시작값: "))
    last = int(input("끝값: "))
    i = first
    while i <= last:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
            i += 1
        print(f"홀수의 합은:{odd_sum},짝수의 합은:{even_sum}")
# test10()