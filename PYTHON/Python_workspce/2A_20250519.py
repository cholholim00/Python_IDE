import os
# 폴더가 없으면 생성
folder_path = 'gugudan_EXCEL'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
import  openpyxl

def test1():
    """구구단 출력하여 엑셀파일로 저장하기
    """
    # 엑셀파일 생성
    wb = openpyxl.Workbook()
    ws = wb.create_sheet("구구단")

    # ws['A1'] = '2단'
    # ws['B1'] = '3단'
    # ws['C1'] = '4단'
    # ws['D1'] = '5단'
    # ws['E1'] = '6단'
    # ws['F1'] = '7단'
    # ws['G1'] = '8단'
    # ws['H1'] = '9단'

    ws['A2'] = "2X1=2"
    ws['A3'] = "2X2=4"
    ws['A4'] = "2X3=6"
    # ...
    ws['A10'] = "2X9=18"

    cols = "ABCDEFGH"
    dan = 2
    for col in cols:
        ws[f"{col}1"] = f"{dan}단"
        # 구구단 출력
        for i in range(1, 10):
         ws[f"{col}{i+1}"] = f"{dan} X {i} = {dan*i}"
        dan += 1
    # 엑셀파일 저장
    wb.save(os.path.join(folder_path,'gugudan.xlsx'))
    print('엑셀파일 저장 완료')
# test1()

def test2():
    """엑셀파일에서 구구단 읽어오기
    """
    # 엑셀파일 열기
    wb = openpyxl.load_workbook(os.path.join(folder_path,'gugudan.xlsx'))
    ws = wb['구구단']

    cols = "ABCDEFGH"
    for col in cols:
        for i in range(1, 11):
            print(ws[f"{col}{i}"].value)
        print()
# test2()

def test3():
    pass
# test3()

class circle():
    """원을 나타내는 클래스
    필드: 반지름(redius)
    메소드: 둘레(get_around, 면적(get_area) 구하기
    """
    def __init__(self, radius):
        self.radius = radius
        
    def get_around(self):
        """원의 둘레를 구하는 메소드
        """
        return 2 * 3.141592 * self.radius
    
    def get_area(self):
        """원의 면적을 구하는 메소드
        """
        return 3.141592 * self.radius ** 2
    
    def __str__(self):
        """원의 반지름을 문자열로 반환하는 메소드
        """
        return f"원의 반지름: {self.radius}, 둘레: {self.get_around()}, 면적: {self.get_area()}"

def test4():
    """circle 클래스 테스트
    """
    c1 = circle(10)
    c2 = circle(20)
    print(c1)
    print(c2)
# test4()

class Rectangle():
    """
    사각형을 나타내는 클래스
    속성: 넓이, 높이
    메소드: 면적, 둘레 구하기
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """사각형의 면적을 구하는 메소드
        """
        return self.width * self.height

    def get_around(self):
        """사각형의 둘레를 구하는 메소드
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """사각형의 넓이와 높이를 문자열로 반환하는 메소드
        """
        return f"사각형의 넓이: {self.get_area()}, 둘레: {self.get_around()}"

def test5():
    """Rectangle 클래스 테스트
    """
    r1 = Rectangle(10, 5)
    r2 = Rectangle(10, 10)
    print(r1)
    print(r2)
# test5()