import sys
import os

# ===============================
# 06-1 내가 프로그램을 만들 수 있을까?
# ===============================
name = input("이름을 입력하세요: ")
print(f"{name}님, 프로그램 만들기에 오신 걸 환영합니다!")


# ===============================
# 06-2 3과 5의 배수를 모두 더하기
# ===============================
total = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


# ===============================
# 06-3 게시판 페이징하기
# ===============================
def get_total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))
