def test1():
    print("1","2","3")
    print(1,2,3)
    print("%d %d %d" % (1,2,3))
    print("{} {} {}".format(1,2,3))
    h = "hello"
    print(f"{h} {3} {3*2}")
# test1()

def test2():
    student = []
    while True:
        str_value = input("이름 국어 영어 수학[종료:exit]")
        if str_value.upper() == "EXIT":
            break
        student = str_value.split()
        if len(student) != 4:
            is_all_digit = True
            for i in range(1,4):
                if not student[i].isdigit():
                    is_all_digit = False
            if is_all_digit:
                student.append([student[0], student[1], student[2], student[3]])
                # student.append(student)
        
        for student in student:
            print(student)
            
# test2()      
def test3():
    country_code = {}
    # list_country_coude = []    
    country_code["KOR"] = 82
    country_code["JPN"] = 81  
    country_code = {"AMERICA" : 1, "KOR" : 82, "JPN" : 81}
    print(country_code)
    
    for item in country_code:
        print(item)
    
    for key in country_code.keys():
        print(key)
        
    for value in country_code.values():
        print(value)
        
        print("-----------------------")
        for item in country_code.keys():
            print(f"{key}: {country_code[key]}")
            
        print("-----------------------")
        for key, value in country_code.items():
            print(f"{key}: {value}")    
# test3()    

def test4():
    """물품목록("코드":"물품명")작성
    예) "001" : "키보드","002" : "마우스"
    """
    
    products = {}
    while True:
        prod = input("물품코드 : 물품명[종료:exit]")
        if prod.upper() == "EXIT":
            break
        key,value = prod.split(",")
        products[key] = value
        
        for k, v in products.items():
            print(f"{k}: {v}")
        
# test4()

def test5():
    """학생정보(이름,나이,학교이름)-딕셔너리 이용
    """
    students = {}
    while True:
        student = input("이름,나이,학교이름[종료:exit]")
        if student.upper() == "EXIT":
          break
    name, age, s_name   = student.split()
    students[name] = [age, s_name]
        
    for key, value in students.items():
            print(f"{key}: {value}")
# test5()

def test6():
    """학생정보(이름,나이,학교이름)
    예) {"name":"홍길동", "age":20, "s_name":"서울대"}
        {"name":"이순신", "age":25, "s_name":"고려대"}
    """
    student_dict = []
    student_list = []
    
    while True:
        item = input("이름,나이,학교이름[종료:exit]")
        if item.upper() == "EXIT":
            break
        name, age, s_name = item.split()
        tmp_dict = {}
        tmp_dict["이름"] = name
        tmp_dict["나이"] = int(age)
        tmp_dict["학교"] = s_name
        student_dict.append(tmp_dict)
        student_list.append([name,int(age),s_name])
        
        print(">>>리스트 출력<<<")
        for student in student_list:
            print(student)
            
        print(">>>딕셔너리 출력<<<")
        for student in student_dict:
            print(f"student: {student}")
            
            for k,v in student.items():
                print(f"{k}: {v}", end =' | ')
        print()
test6()        