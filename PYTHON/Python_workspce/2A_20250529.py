# # db 연결 및 커서 획득, 쿼리 실행
import sqlite3
#회원 정보관리 프로그램
def db_setup():
    conn = sqlite3.connect('2024201019.db', isolation_level=None)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS member (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT
    )
    ''')
    return conn
def insert_member(conn):
    cur = conn.cursor()
    name = input("회원 이름을 입력하세요: ")
    email = input("회원 이메일을 입력하세요: ")
    phone = input("회원 전화번호를 입력하세요: ")
    param = (name, email, phone)
    cur.execute('INSERT INTO member (name, email, phone) VALUES (?, ?, ?)', param)
    print("회원 정보가 등록되었습니다.")
def select_member(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM member')
    for row in cur.fetchall():
        print(f"ID: {row[0]} | 이름: {row[1]} | 이메일: {row[2]} | 전화번호: {row[3]}")
    print('회원 조회 완료!\n')
def update_member(conn):
    cur = conn.cursor()
    id = input("수정할 회원의 ID를 입력하세요: ")
    name = input("새로운 이름을 입력하세요: ")
    email = input("새로운 이메일을 입력하세요: ")
    phone = input("새로운 전화번호를 입력하세요: ")
    param = (name, email, phone, id)
    cur.execute('UPDATE member SET name=?, email=?, phone=? WHERE id=?', param)
    print("회원 정보가 수정되었습니다.")
def update_member_new(conn):
    pass
def delete_member(conn):
    cur = conn.cursor()
    id = input("삭제할 회원의 ID를 입력하세요: ")
    cur.execute('DELETE FROM member WHERE id=?', (id,))
    print("회원 정보가 삭제되었습니다.")

def main():
    conn = db_setup()
    # 데이터베이스 연결 및 테이블 생성
    while True:
        print(">>> 회원 정보 관리 프로그램 <<<")
        print("1. 회원 등록")
        print("2. 회원 조회")
        print("3. 회원 수정")
        print("4. 회원 삭제")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        # 회원 등록, 조회, 수정, 삭제 선택
        if choice == '1':
            insert_member(conn)
        elif choice == '2':
            select_member(conn)
        elif choice == '3':
            update_member(conn)
        elif choice == '4':
            delete_member(conn)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")
        conn.close()
    insert_member()
    select_member()
    update_member()
    delete_member()
