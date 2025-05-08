def test1():
    """로또 번호 추출기.
    로또 번호 1~45 까지의 수를 6개 중복되지 않게 생성하고 출력하기
    """
        
import random
    
# def getRandomNumber():
#     number = random.randint(1, 45)
#     return number
# lotto = []
# for i in range(6):
#     random_number = getRandomNumber()
#     if random_number not in lotto: # 랜덤값이 리스트 lotto안에 없으면
#         lotto.append(random_number)  # 얘도 좀 껴줘라~
# print(lotto)
    
# lotto_list =    
# while True:
#     num = random.randint(1,45)
#     if num  not in lotto_list:
#        lotto_list.append(num)
#     if len(lotto_list) == 6:
#                 break
#     print(lotto_list)   
    
#test1()

def test2():
    #구구단
    for i in range(2,10):
        for j in range(1,10):
            print(i,'X',j,'=',i*j)
            if(j == 9):
                print('---------------')
#test2()

def test3():
    i = 2
    while i<10:
        j = 1
        while j<10:
            print("{}*{}={}".format(i,j,i*j))
            j+=1
        i+=1
#test3()

def test4():
    """원하는 단을 입력받아 츨력
    """
    i = int(input('몇 단을 출력하시겠습니까? : '))
    for y in range(1, 10):
     print(i, "X", y, "=", i*y)
#test4()

def test5():
    """원하는 단을 입력받아 출력하는데(종료:quit)
    """
    while True:
        
      i = input('몇 단을 출력하시겠습니까?[종료시(quit)] : ')
      if i == 'quit':
       break
      i = int(i)
      for y in range(1,10):
          print(f"{i}X{y}={i*y}")
         
#test5()

def sum_even_odd(first, last):
    """구간안에서 짝수합, 홀수합 구하기.
    
    주어진 구간안에서 짝수합과 홀수합을 구하여 리턴하기
    Args:
        first (int): 구간의 시작값
        last (int): 구간의 종료값

    Returns:
        int,int: 짝수합,홀수합
    """
    sum_even = 0
    sum_odd = 0
    for i in range(first,last):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i    
    return sum_even,sum_odd

def test6():
    first = 1
    last = 10
    even_sum,odd_sum =sum_even_odd(first,last) #언패킹
    print(f"{first}부터 {last}까지의 짝수의합:{even_sum}, 홀수의합:{odd_sum}")
    
#test6()

def test7():
    korea_score = [60,70,80,90,100]
    eng_score = [50,60,70,80,90]
    math_score = [40,50,60,70,80]
    
    mid_score = [korea_score,eng_score,math_score]
    subject_name = ["국어","영어","수학"]
    student_name = ["학생1","학생2","학셍3","학셍4","학셍5"]
    
    subject_average = []
    # student_average = [150,180,210,240,270]
    student_average = [0,0,0,0,0]
    for subject in mid_score:
        sum = 0
        index = 0
        for score in subject:
            sum += score
            student_average[index] += score
            index += 1
        subject_average.append(sum/len(subject))
        
    # for i in range(len(student_average)):
    #     student_average[i] = student_average[i]/3
    
    a,b,c,d,e = student_average
    student_average = [a/3,b/3,c/3,d/3,e/3]
           
    # print(subject_name)
    # print(subject_average)
    
    for i in range(len(student_name)):
        print(f"{student_name[i]}: {student_average[i]}")
    print("*"*20)    
    for i in range(len(subject_name)):
         print(f"{subject_name[i]}: {subject_average[i]}")
         
test7()