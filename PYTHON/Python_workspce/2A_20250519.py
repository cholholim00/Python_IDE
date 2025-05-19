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
test3()