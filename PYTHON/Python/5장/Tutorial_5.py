print("========== 클래스 ==========")
# 클래스의 기본 구조부터 캡슐화(돈을 함부로 수정 못 하게 함)와 상속
class BankAccount:
    def __init__(self, owner, balance=0):
        # 생성자: 객체가 만들어질 때 이름과 초기 잔액을 설정합니다.
        self.owner = owner          # 예금주 (속성)
        self.__balance = balance    # 잔액 (속성, __를 붙여 외부에서 직접 수정 못하게 보호)

    def deposit(self, amount):
        """입금 동작: 잔액을 증가시킵니다."""
        if amount > 0:
            self.__balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.__balance}원")
        else:
            print("입금액은 0원보다 커야 합니다.")

    def withdraw(self, amount):
        """출금 동작: 잔액이 충분할 때만 차감합니다."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}원이 출금되었습니다. 남은 잔액: {self.__balance}원")
        else:
            print("잔액이 부족하거나 잘못된 금액입니다.")

    def get_balance(self):
        """잔액 조회: 보호된 잔액을 안전하게 확인하는 메서드입니다."""
        return f"{self.owner}님의 현재 잔액은 {self.__balance}원입니다."

# 상속받은 특수 계좌 (상속과 재정의)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        # 부모 클래스의 생성자를 호출하여 이름과 잔액을 초기화합니다.
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # 이자율 속성 추가

    def add_interest(self):
        """이자 계산: 현재 잔액에 이자율을 곱해 입금합니다."""
        # 부모의 메서드인 get_balance나 deposit을 활용할 수 있습니다.
        # 여기서는 간단히 이자 계산 로직만 구현합니다.
        print(f"이자율 {self.interest_rate}%가 적용됩니다.")

        # 실제 이자 계산 로직 (기초적인 예시)
        # 참고: 상속받은 부모의 __balance는 직접 접근이 안되므로
        # 실제로는 부모 클래스에 별도의 접근 메서드를 더 만들어 사용합니다.

# 1. 철수의 일반 계좌 생성
chulsu_acc = BankAccount("김철수", 1000)

# 2. 입금과 출금 테스트
chulsu_acc.deposit(500)   # 1500원 됨
chulsu_acc.withdraw(2000) # 잔액 부족 메시지 출력
chulsu_acc.withdraw(700)  # 800원 남음

# 3. 잔액 확인 (직접 변수에 접근하면 에러가 나거나 접근이 안 됨)
# print(chulsu_acc.__balance)  <- 이 코드는 에러가 발생합니다 (캡슐화)
print(chulsu_acc.get_balance())

# 4. 영희의 이자 계좌 생성 (상속 활용)
younghee_acc = SavingsAccount("이영희", 5000, 0.05)
younghee_acc.deposit(1000) # 부모 클래스의 기능을 그대로 사용 가능
print(younghee_acc.get_balance())

print("========== 모듈 ==========")
print("1. 모듈 만들기 (공구함 채우기)")
# 이것이 하나의 '모듈'이 됩니다.
class Calc:
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b

def welcome():
    print("계산기 모듈에 오신 것을 환영합니다!")

print("2. 모듈 사용하기 (공구함 꺼내 쓰기)")
# 1. calculator.py 모듈을 통째로 가져옵니다.
import calculator
# 2. 모듈 안의 함수 사용하기
calculator.welcome()
# 3. 모듈 안의 클래스 사용하기
my_calc = calculator.Calc("내 계산기")
result = my_calc.add(10, 20)

print(f"{my_calc.name}의 결과: {result}")

print("3. 자주 쓰는 모듈 사용 팁 (주석 설명)")
# 방법 1: 모듈 전체를 가져오기 (가장 표준적인 방법)
import calculator
calculator.welcome()

# 방법 2: 모듈에서 특정 클래스나 함수만 골라서 가져오기
# 이렇게 하면 'calculator.'을 앞에 안 붙여도 바로 쓸 수 있습니다.
from calculator import Calc, welcome
my_calc = Calc("빠른 계산기")
welcome()

# 방법 3: 모듈 이름이 너무 길 때 별명(alias) 붙이기
import calculator as cal
cal.welcome()

print("========== 패키지 ==========")
print("========== 예외처리 ==========")
print("========== 내장 함수 ==========")
print("========== 표준 라이브러리 ==========")
print("========== 외부 라이브러리 ==========")
