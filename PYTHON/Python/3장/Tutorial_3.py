print("========== 제어문 ==========")
print("===[조건을 판단하는 if문]===")
print("돈이 있으면 택시를 타고, 돈이 없다면 걸어간다. 라는 상황을 가정해보자")
money = True # 나는 돈이 있어!(True)
if money:
    print("[돈이 있으니 택시를 타자.]") # (True)
else:
    print("[돈이 없으니 걸어가자.]") # (False)

print("만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라. 라는 상황을 가정해보자")
money = 2000
if money >= 3000: # money의 금약이 3000원 보다 크거나 같다(False)
    print("[돈이 가능할거같네 택시타자.]") # (True)
else:
    print("[돈이 없으니 걸어가자.]") # (False)

print("돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.. 라는 상황을 가정해보자")
money = 3000 # (True)
card = True # (True)
if money >= 3000 or card: # (True) or (True) = (True)
    print("[돈이 있으니 택시를 타고가라.]") # (True)
else:
    print("[돈이 없으니 걸어가라.]") # (False)

print("~ 안에 있나요?")
print("===[X in 리스트]===")
print(1 in [1,2,3])
print("===[X in 튜플]===")
print('a' in ['a','b','c'])
print("===[X in 문자열]===")
print('a' in 'abc')
print("~ 안에 있는데 없는거에요")
print("===[X in 리스트]===")
print(1 not in [1,2,3])
print("===[X in 튜플]===")
print('a' not in ['a','b','c'])
print("===[X in 문자열]===")
print('a' not in 'abc')
print("===[in  와 Not in 적용 예제]===")
print("만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.")
pocket = ['paper','cellphone','money' ]
if 'money' in pocket:
    print("[주머니에 돈이 있어서 택시를 타고가자.]")
else:
    print("[주머니에 돈이 없어서 걸어가자.]")

print("===[다양한 조건을 판단하는 elif문]===")
print("주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.")
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("[주머니에 돈이 있으니 택시를 타고 가자.]")
elif card:
    print("[주머니에 카드가 있으니 택시를 타고가자.]")
else:
    print("[주머니에 돈도 카드도 없으니 걸어가자.]")

print("===[비교 연산자의 연쇄 사용]===")
x = 5
print("x가 1보다 크고 10보다 작은가?")
print(1 < x < 10)
print((1 < x) and (x < 10)) # 더 간결하고 읽기 쉬운 코드
print("x가 10 이상 20 이하인가?")
print(10 <= x <= 20)
print((10 <= x) and (x <= 20)) # 더 간결하고 읽기 쉬운 코드

print("===[조건부 표현식]===")
print("점수가 60점 이상이면 \"합격\", 미만이면 \"불합격\"이라는 메시지를 저장하고 싶다고 해보자.")
score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result)
print("===[간단한 조건 분기일때]===")
result = "합격" if score >= 60 else "불합격"
print(result)

print("===[while문]===")
print("열 번 찍어 안 넘어가는 나무 없다’라는 속담을 파이썬 프로그램을 만들어보자")
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("쩌저저적!!! 나무가 넘어갑니다.")

print("여러 가지 선택지 중 하나를 선택해서 입력받는 예제")
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

print("커피 자판기 이야기를 파이썬 프로그램으로 표현")
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print("coffee.py")
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

print("[while 문의 맨 처음으로 돌아가기]")
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

print("[무한 루프]")
# while True:
#     print("수행할_문장1")
#     print("수행할_문장2")

print("while-else문")
count = 0
while count < 3:
    print(f"카운트:{count}")
    count += 1
else:
    print("while문이 정상 종료 되었습니다.")

print("중첩 while문")
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("===[for문]===")
print("===[전형적인 for문]===")
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print("===[다양한 for문의 사용]===")
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

print("===[for문의 응용]===")
print("===[총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.]===")
masks = [90, 65,84,42,53] # 학생 시험 점수 리스트

number = 0 # 학생에게 붙여줄 번호
for mask in masks: # 90, 65,84,42,53을 순서대로 mask에 대입
    number = number + 1
    if mask >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

print("===[for문과 continue 문]===")
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

print("===[for 문과 함께 자주 사용하는 range 함수]===")
a = range(10)
b = range(1,11)
print(a,b)

print("===[range 함수의 예시 살펴보기]===")
add = 0
for i in range(1,11):
    add = add + i
    print(add)

marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

print("===[for와 range를 이용한 구구단]===")
print("[방법1]")
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

print("[방법2]")
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")

print("===[리스트 컴프리헨션 사용하기]===")
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

print("===[더 간편하게 리스트 컴프리헨션 사용하기]===")
result = [num * 3 for num in a]
print(result)

print("===[만약 [1, 2, 3, 4] 중에서 짝수에만 3을 곱하여 담고 싶다면 리스트 컴프리헨션 안에 ‘if 조건문’을 사용]===")
result = [num * 3 for num in a if num % 2 == 0]
print(result)

print("===[구구단의 모든 결과를 리스트에 담고 싶다면 리스트 컴프리헨션을 사용]===")
result = [i * j  for i in range(2,10)
                 for j in range(1,10)]
print(result)

print("===[for 문과 break 문]===")
for i in range(10):
        if i == 5:
            break
        print(i)
print("===[for-else 문]===")
for i in range(5):
     print(i)
else:
     print("for 문이 정상 종료되었습니다.")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
     print("for 문이 정상 종료되었습니다.")

print("===[enumerate 함수 활용하기]===")
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits): # 0부터 시작
     print(f"{i}: {fruit}")

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 1):  # 1부터 시작
     print(f"{i}: {fruit}")

print("===[zip 함수로 여러 리스트 함께 순회하기]===")
print("두 개 이상의 리스트를 동시에 순회하고 싶을 때는 zip 함수")
name = ['홍길동','김철수','아영희']
score = [90,80,70]
for name,score in zip(name,score):
    print(f"{name} : {score}")

print("세 개 이상의 리스트도 함께 순회할 수 있다.")
names = ['홍길동', '김철수', '이영희']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, korean, english in zip(names, korean, english):
    print(f"{name} : 국어는 :{korean} 영어는 :{english}")