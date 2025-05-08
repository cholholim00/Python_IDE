def test1():
    sentence = "I LOVE YOU"
    re_sentence = ""
    for char in sentence:
        #print(char)
        re_sentence = char + re_sentence
        print(re_sentence)
# test1()        
        
def test2():
    
    original = num = 17
    result = ""
    while True:
        num1 = num // 2 # 몫
        num2 = num % 2 # 나누기
        num = num1
        result = str(num2) + result
        if num1 == 0:
            break
        print(f"(10진수){num} => (2진수){result}")
        
# test2() 

# def test3(num):
#     binary = ""
    
#     while num !=0:
#         value = num %2
#         if value  == 0:
#             binary = "0" + binary
#         else:
#             binary = "1" + binary
#         num = num // 2
#         print("num :", num)
#     return binary
        
# decNum = int(input("10진수를 입력하세요 : "))
# print("10진수", decNum, "을 2진수로 변환하면 :", test3(decNum), "(2)")

def test4():
    while True:
        num = input("10진수[종료:quit] ")
        if num == "quit":
            break
        original = num = int(num)
        divider = int(input("2진수 or 8진수 :"))
        result = ""
        while True:
            num1 = num // divider
            num2 = num % divider
            num = num1
            result = str(num2) + result
            if num1 == 0:
                print(f"(10진수){original} => ({divider}진수){result}")
                break
# test4()   

def test5():
     while True:
        num = input("10진수[종료:quit] ")
        if num == "quit":
            break
        original = num = int(num)
        divider = int(input("2진수 || 8진수 || 16진수 :"))
        result = ""
        
        hex = "0123456789ABCDEF" # 16진수 변환을 위한 매핑
        
        while True:
            num1 = num // divider
            num2 = num % divider
            num = num1
            if divider == 16:  # 16진수일 경우, hex_map을 사용하여 문자로 변환
                result = hex[num2] + result
            else:
                result = str(num2) + result
            if num1 == 0:
                print(f"(10진수){original} => ({divider}진수){result}")
                break          
# test5() 

def test6():
    sentence = "I LOVE YOU"
    print(sentence.upper())
    print(sentence.lower())
    print(len(sentence))
    print(sentence.find("l"))
    print(len(sentence),len(sentence.strip()))
# test6()

def test7():
    """단을 입력받아 구구단을 출력하기[종료:quit]"""
    while True:
        dan = input("단을 입력하세요[종료:quit] ")
        if dan.upper == "QUIT":
            break
        if not dan.isdigit():
            print("숫자만 입력하세요")
            continue
        dan = int(dan)
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}") 
# test7()

def test8():
   names = "홍길동", "이몽룡", "성춘향", "변학도"
   name_list = names.split(",")
   print(name_list)

# test8()

def test9():
    
    dan = input("원하는 단을 입력하세요 : ")
    dan_list = dan.split()
    for dan in dan_list:
        print(f"{dan}단 >>>> ")
        dan = int(dan)
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}")
# test9()   

def test10():
    """n명의 국어,영어,수학 점수를 입력받아 학생평균과 과목평균을 구하기"""
    subject_name = ["국어", "영어", "수학"]
    students_scores = []
    while True:
        scores = input("이름,국어,영어,수학 점수 [종료:quit]: ")
        if scores.upper() == "QUIT":
            break
        students_scores.append(scores.split())
    
    students_mean_value = []
    subjects_mean_value = [0,0,0]
    for scores in students_scores:
        sum = 0
        index = 0
        for score in scores[1:]:
            sum += int(score)
            subjects_mean_value[index] += int(score)
            index += 1
            students_mean_value.append(sum / 3)
            count = len(students_scores)
            ko, en, ma = subjects_mean_value
            subjects_mean_value = [ko / count, en / count, ma / count]
            
            index = 0    
            for student in students_scores:
                print("{student[0]} :  {students_mean_value[index]}")
                index += 1
            for i in range(len(subjects_mean_value)):
                print(f"{subject_name[i]} : {subjects_mean_value[i]}")    
            print(f"학생평균 : {students_mean_value}")
            print("과목평균 : ",subjects_mean_value)
# test10()    
        
        
        
        