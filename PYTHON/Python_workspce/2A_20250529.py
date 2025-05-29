# ******************************************
# 회원정보 관리하기
# ******************************************
import sqlite3
def db_setup():
    # conn = sqlite3.connect("2A.db", isolation_level=None)
    conn = sqlite3.connect("2A.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS member (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT
            )
    """)
    return conn
def insert_member(conn):
    cur = conn.cursor()
    name = input("이름: ")
    email = input("이메일: ")
    phone = input("전화번호: ")
    param = (name,email,phone)
    cur.execute("INSERT INTO member (name,email,phone) VALUES (?,?,?)", param)
    print("회원 등록 완료!\n")
def select_member(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    for row in cur.fetchall():
        print(f"ID:{row[0]} | 이름:{row[1]} | Email:{row[2]} | Phone:{row[3]}")
    print("회원 조회 완료!\n")
def update_member(conn):
    cur = conn.cursor()
    id = input("수정할 ID: ")    
    name = input("수정할 이름: ")
    email = input("수정할 이메일: ")
    phone = input("수정할 전화번호: ")
    param = (name,email,phone,id)
    cur.execute("UPDATE member SET name=?,email=?,phone=? WHERE id=?",param)
    print("회원 수정 완료!\n")
def update_member_new(conn):
    pass
def delete_member(conn):
    cur = conn.cursor()
    id = input("삭제할 ID: ")
    param = (id,)
    obj = cur.execute("DELETE FROM member WHERE id=?", param)
    if obj.rowcount == 0:
        print("[❌] 회원 정보가 없습니다!\n")
    else:
        print("[⭕] 회원 삭제 완료\n")
        
def main():
    conn = db_setup()
    while True:
        print(">>> 회원 관리 프로그램 <<<")
        print("1. 회원 등록")
        print("2. 회원 조회")
        print("3. 회원 수정")
        print("4. 회원 삭제")
        print("5. 종료")
        num = input("선택[1~5]: ")
        if num == "1":
            insert_member(conn)
        elif num == "2":
            select_member(conn)
        elif num == "3":
            update_member(conn)
        elif num == "4":
            delete_member(conn)
        elif num == "5":
            print("프로그램을 종료합니다!")
            break
        else:
            print("선택이 잘못되었습니다!")
    
    # conn.commit()
    conn.close()

# main()






def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    html = urlopen("https://www.naver.com")
    # print(html.read())
    bs_obj = BeautifulSoup(html.read(),"html.parser")
    print(bs_obj)

# test1()


def test2():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html_str = """
        <html>
            <body>
                <ul>
                    <li>hello</li>
                    <li>bye</li>
                    <li>welcome</li>
                </ul>
            </body>
        </html>
    """
    
    bs_obj = BeautifulSoup(html_str, "html.parser")
    # print(bs_obj)
    ul = bs_obj.find("ul")
    li = bs_obj.find("li")
    li_all = bs_obj.findAll("li")
    for item in li_all:
        print(item.text)

# test2()

def test3():
    from bs4 import BeautifulSoup
    html_str = """
        <html>
            <body>
                <ul class="greet">
                    <li>Hello</li>
                    <li>Bye</li>
                    <li>Welcome</li>
                </ul>
                <ul class="reply">
                    <li>ok</li>
                    <li>no</li>
                    <li>sure</li>
                </ul>
            </body>
        </html>
    """
    bs_obj = BeautifulSoup(html_str, "html.parser")
    ul_1 = bs_obj.find("ul",{"class":"greet"})
    
    ul_list = bs_obj.findAll("ul")
    for ul in ul_list:
        li_list = ul.findAll("li")
        for li in li_list:
            print(li.text)

# test3()

# find, findAll vs select_one, select
def test4():
    from bs4 import BeautifulSoup
    html_str = """
        <html>
            <body>
                <ul> 
                    <li><a href="https://www.naver.com">네이버</a></li>
                    <li><a href="https://www.daum.net">다음</a></li>
                </ul>
            </body>
        </html>
    """
    bs_obj = BeautifulSoup(html_str, "html.parser")
    a_list = bs_obj.findAll("a")
    for a in a_list:
        # print(a.text)
        print(a["href"])
    a_list2 = bs_obj.select("a")
    for a in a_list2:
        print(a["href"])
# test4()

def test5():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = "https://www.yes24.com"
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(),"html.parser")
    a_tag = bs_obj.select_one("#yesFixCorner > dl > dd > ul.yesCornerLi > li:nth-child(1) > a")
    
    # li_list = bs_obj.select("#wMbnSub_001 > div > div.cateTxt > ul > li")
    # for item in li_list:
    #     print(item.text)
    # print("-----------------------------")
        
    # h4_list = bs_obj.select("#wMbnSub_018 > div > div.cateTxt > h4")
    # li_list = bs_obj.select("#wMbnSub_018 > div > div.cateTxt > ul > li")
    # for item in li_list:
    #     print(item.text)
    # for item in h4_list:
    #     print(item.text)
    
    #ulCategoryList > li.cate001
    li_list = bs_obj.select("#ulCategoryList > li")
    for item in li_list:
        print(item.text)
    
test5()
