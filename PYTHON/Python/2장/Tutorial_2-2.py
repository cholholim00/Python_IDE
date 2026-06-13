print("==========집합 자료형==========")
print("[집합 자료형]")
s1 = set([1,2,3]) # 집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있다.
s2 = set("Hello") # set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력하여 만들 수도 있다.
s3 = {'a', 'b', 'c'} # 중괄호({})를 사용해서 집합 자료형을 직접 만들 수도 있다.
print(s1,s2,s3)
print("[집합 자료형에 저장된 값을 인덱싱하기]") # 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후에 해야 한다.
l1 = list(s1)
print(l1, "리스트형:첫번째 인덱싱 값:", + l1[0]) # 리스트형
t1 = tuple(s1)
print(t1, "튜플형:두번째 인덱싱 값:", + t1[1]) # 튜플형
# 교집합, 합집합, 차집합 구하기
set1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])
print("[교집합]")
print("방법1:",set1 & set2)
print("방법2:",set1.intersection(set2))
print("[차집합]")
print("방법1:",set1 - set2)
print("방법2:",set1.difference(set2))
print("[합집합]")
print("방법1:",set1 | set2)
print("방법2:",set1.union(set2))

print("[집합 자료형 관련 함수]")
print("[값 1개 추가하기 ]")
print(set1.add(7), set1)
print("[값 여러 개 추가하기]")
print(set1.update([8,9]), set1)
print("[특정 값 제거하기1]")
print(set1.remove(9), set1)
print("[특정 값 제거하기2]")
print(set1.discard(8),set1)
print("[모든 값 제거하기]")
print(set1.clear(),set1)

print("==========불 자료형==========")
a = True
b = False
print("[bool로 지정된 것을 확인]")
print("A:",type(a),"B:",type(b))
print("1과 1이 같은가?", a == a)
print("2보다 1이 더 큰가?", a < b)
print("1보다 2이 더 큰가?", b < a)
print("[불연산:자료형의 참과 거짓]")
print("값이 잇으면 진실/ 없다면 거짓이 나온다.")

print("[논리 연산자]")
print("[AND]")
print(True and True,
      True and False,
      False and False,
      False and True)
print("[OR]")
print(True or True,
      True or False,
      False or False,
      False or True)
print("[NOT]")
print(not True,
      not False,
      not 0,
      not 1)
print("[EX01]")
x = 5
y = 10
print(x > 0 and y > 0)
print("[EX02]")
print(x > 10 or y > 5)
print("[EX03]")
print(not (x > y))



