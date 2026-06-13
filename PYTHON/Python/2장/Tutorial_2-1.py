print("==========숫자형==========")

# 숫자형
integer = 123 # 정수형
Real_Number = 1.14 # 실수형
Binary = 0b1010 # 2진수
Octal = 0o177 # 8진수
Hexadecimal = 0x123 # 16진수
print("정수형 :",integer)
print("실수형 :",Real_Number)
print("2진수 :",Binary)
print("8진수 :",Octal)
print("16진수 :",Hexadecimal)

print("==========연산자==========")
# 연산자
a = 5
b = 7
Operator = {
    "+": a + b, # 덧셈
    "-": a - b, # 뺄셈
    "*": a * b, # 곱셈
    "/": a / b, # 나눗셈
    "%": a % b, # 나머지
    "**": a ** b, # 제곱근
    "//": a // b # 몫
}
print(Operator)

print("==========복합 연산형==========")
# 복합 연산자
a += 1
print('a +=',a)
a -= 1
print('a -=',a)
a *= 1
print('a *=',a)
a /= 1
print('a /=',a)
a //= 1
print('a //=',a)
a %= 1
print('a %=',a)
a **= 1
print('a **=',a)

print("==========문자형==========")
# 문자열
str1 = 'Python String! 한글 1234 !@#$%^'
str2 = "Python String! 한글 1234 !@#$%^"
str3 = '''Python String! 한글 1234 !@#$%^'''
str4 = """Python String! 한글 1234 !@#$%^"""
print(str1)
print(str2)
print(str3)
print(str4)

# 문자열 안에 따옴표 자체를 포함하는 방법
str5 = 'Python String! "한글" 1234 !@#$%^'
str6 = 'Python String! \'한글\' 1234 !@#$%^'
str7 = "Python String! '한글' 1234 !@#$%^"
str8 = "Python String! \"한글\" 1234 !@#$%^"
print(str5)
print(str6)
print(str7)
print(str8)

print("==========리스트 자료형==========")
# 리스트 인덱싱
print("[인덱싱]")
Indexing = [1,2,3,4,5]
print(Indexing[0]) # 0번째 '1'출력
print(Indexing[0] + Indexing[3]) # 0번쨰 '1' 과 3번쨰 '4' 를 더한다.
print(Indexing) # 안에 있는 리스트값들을 모두 출력

# 리스트의 슬라이싱
print("[슬라이싱]")
Slicing = [6,7,8,9,10]
print(Slicing[0:2]) # 0번부터 2번 전까지 출력
print(Slicing[:4]) # 0번부터 4번 전까지 출력
print(Slicing[2:]) # 2번부터 끝까지 출력

# 리스트 연산
a = [1,5,3,2]
b = [4,5,6]
# 리스트 더하기
print("[연산]")
print(a+b)
# 리스트 반복하기
print("[반복]")
print(a*3)
# 리스트 길이 구하기
print("[길이]")
print(len(a))
# 리스트 값 수정
print("[값수정]")
a[2] = 4
print(a)
# 리스트 값 삭제
print("[값수정]")
del a[1]
print(a)
# 리스트에 요소 추가하기
print("[요소 추가]")
a.append(2)
print(a)
# 리스트에 정렬
print("[정렬]")
a.sort()
print(a)
# 리스트 뒤집기
print("[뒤집기]")
a.reverse()
print(a)
# 리스트 인덱스 반환
print("[반환]")
print(a.index(4))
# 리스트에 요소 삽입
print("[삽입]")
a.insert(1,3)
print(a)
# 리스트 요소 제거
print("[제거]")
a.remove(3)
print(a)
# 리스트 요소 끄집어 내기
print("[꺼내기]")
print(a.pop())
# 리스트에 포함된 요소 n의 개수 세기
print("[N의 개수세기]")
print(a.count(2))
# 리스트 확장
print("[확장]")
a.extend([1,2,3])
print(a)

print("==========튜플 자료형==========")
# 튜플 요소값을 삭제(튜플값은 지우거나 변경하거나 삭제가 불가능함)
print("[튜플 요소값 삭제]")
print("(튜플값은 지우거나 삭제가 불가능함)")
# 튜플 요솟값을 변경
print("[튜플 요소값 변경]")
print("===튜플 다루기===")
t1 = (1,2,3)
t2 = (4,5,6)
# 튜플 인덱싱
print("[튜플 인덱싱하기]")
print(t1[0])
# 튜플 슬라이싱
print("[튜플 슬라이싱하기]")
print(t1[1:])
# 튜플 더하기
print("[튜플 더하기]")
print(t1 + t2)
# 튜플 곱하기
print("[튜플 곱하기]")
print(t1*3)
# 튜플 길이 구하기
print("[튜플 길이 구하기]")
print(len(t1))

print("==========딕셔너리 자료형==========")
dic = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# 딕셔너리 쌍 추가
print("[딕셔너리 쌍 추가]")
dic['key4'] = 'value4'
print(dic)
# 딕셔너리 요소 삭제
print("[딕셔너리 요소 삭제]")
del dic['key4']
print(dic)
# 딕셔너리에서 Key를 사용해 Value 얻기
print("[Key를 사용해 Value 얻기]")
print(dic['key2'])
# Key 리스트 만들기
print("[Key 리스트 만들기]")
print(dic.keys())
# Value 리스트 만들기
print("[Value 리스트 만들기]")
print(dic.values())
# Key, Value 쌍 얻기
print("[Key, Value 쌍 얻기]")
print(dic.items())
# Key: Value 쌍 모두 지우기
print("[# Key: Value 쌍 모두 지우기]")
print(dic.clear())
# Key로 Value 얻기
print("[Key로 Value 얻기 ]")
print(dic.get('key1'))
# 해당 Key가 딕셔너리 안에 있는지 조사하기
print("[Key가 딕셔너리 안에 있는지 조사]")
print('key1' in dic)
# Key로 Value 얻기
print("[Key로 Value 얻기]")
print(dic.pop('key3'))