from email import header
from importlib.resources import contents
import os
import csv
import persons


def test1():
    for i in range(10):
        try:
            print(10/i)
        except ZeroDivisionError:
            print("Not divisible by 0")
# test1()

def test2():
    for i in range(10):
        try:
            print(10/i)
        except ZeroDivisionError as e:
            print(e)
# test2()

def test3():
    while True:
        value = input("숫자[종료:quit]: ")
        if value.upper() == "quit":
            break
        for digit in value:
            if not digit in "0123456789":
                raise ValueError("숫자를 넣어야지!!!")
            print(f"정수값: {int(value)}")
# test3()

def test4():
    try:
        while True:
            value = input("숫자[종료:quit]: ")
            if value.upper() == "quit":
                break
            for digit in value:
                if not digit in "0123456789":
                    raise ValueError("숫자를 넣어야지!!!")
            print(f"정수값: {int(value)}")
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
# test4()

def test5():
    f = open("dream.txt", "r")
    contents = f.read()
    print(type(f), type(contents))
    print(contents)
    f.close()
# test5()

def test6():
    f = open("dream.txt", "r")
    contents_list = f.readlines()
    print(contents_list)
    for item in contents_list:
        print(item,end="")
# test6()

def test7():
    f = open("dream.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        print(line,end="")
# test7()

def test8():
    with open("dream.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line,end="")
# test8()

def test9():
    with open("dream.txt", "r") as f:
        contents = f.readlines()
    print(contents)

    contents2 = []
    for item in contents:
        contents2.append(item.replace("\n",""))

    print(contents2)
# test9()

def test10():
    with open("dream.txt", "r") as f:
        contents = f.read()

    contents_list = contents.split("\n")
    print(contents_list,len(contents_list))
# test10()

def test11():
    with open("count_log.txt", "a",encoding = "utf-8") as f:
        for i in range(1,11):
            f.write(f"{i}번째 줄이다.\n")
# test11()

def test12():
    if not os.path.isdir("log"):
        os.mkdir("log")

    with open("./log/count_log.txt", "a",encoding = "utf-8") as f:
        for i in range(1,11):
            f.write(f"{i}번째 줄이다.\n")
# test12()

def test13():
   persons = []
   for i in range(1,11):
       persons.append([f"홍길동{i}", i + 20])
   print(persons)

   header = ["이름","나이"]
   with open("person.csv", "w", encoding="utf-8", newline="") as f:
       # writer = csv.writer(f, delimiter=",", quotechar="", quoting=csv.QUOTE_ALL)
       writer = csv.writer(f, delimiter=",", quotechar="", quoting=csv.QUOTE_NONNUMERIC)
       writer.writerows(header)
       for item in persons:
           writer.writerow(item)
# test13()

def test14():
    persons = []
    for i in range(1,11):
        tmp_dict = {}
        tmp_dict["name"] = f"홍길동{i}"
        tmp_dict["age"] = i + 20
        persons.append(tmp_dict)

    header = ["이름","나이"]
    with open("person.csv", "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar="''",quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
        for item in persons:
            writer.writerow([item['name'],item['age']])
test14()

def test15():
    header = []
    person_list = []
    person_dict = []
    with open("person.csv", "r", encoding="utf8") as f:
        reader = csv.reader(f,delimiter=",", quotechar="'",quoting=csv.QUOTE_NONNUMERIC)
        count = 1
        for item in reader:
            if count == 1:
                header = item
                count += 1
            else:
                person_list.append(item)
                tmp_dict = {}
                tmp_dict["name"] = item[0]
                tmp_dict["age"] = item[1]
                person_dict.append(tmp_dict)

    print(header)
    print("-" * 20, "\n", person_list)
    print("-" * 20, "\n", person_dict)
# test15()






