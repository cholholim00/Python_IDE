# db 연결 및 커서 획득, 쿼리 실행
import sqlite3

# SQLite 데이터베이스 연결
def test1():
    print(sqlite3.version) # 모두의 버전 번호
    print(sqlite3.sqlite_version) # 라이브러리 버전 번호

    # 데이터베이스 연결 (파일이 없으면 새로 생성됨)
    conn = sqlite3.connect('testdb_1.db', isolation_level=None) # isolation_level=None은 자동 커밋 모드
    cur = conn.cursor() # 커서 객체 생성

    # 테이블 생성
    cur.execute("CREATE TABLE IF NOT EXISTS table1 (id INTEGER PRIMARY KEY, name TEXT , birthday TEXT)")
    conn.close()
# test1()

# 데이터 삽입- execute() 메서드 사용
def test2():
    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    # 데이터 삽입
    # cur.execute("INSERT INTO table1 (id, name, birthday) VALUES (?, ?, ?)", ('1','Lee', '2025-04-17'))
    cur.execute("INSERT INTO table1 (name, birthday) VALUES (?, ?)", ('Kim', '2025-04-20'))
    cur.execute("INSERT INTO table1 (name, birthday) VALUES (?, ?)", ('PARK', '2025-04-22'))
# test2()

# 데이터 삽입- executemany() 메서드 사용
def test3():
    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    test_tuple = (
        ('홍길동', '2025-04-23'),
        ('홍길순', '2025-04-15'),
        ('김태무', '2025-04-27')
    )

    # 데이터 삽입
    cur.executemany("INSERT INTO table1 (name, birthday) VALUES (?, ?)", test_tuple)
    conn.close()
# test3()

# 현재 날짜와 시간 삽입
def test4():
    import datetime

    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    # 현재 날짜와 시간
    today = datetime.date.today().strftime('%Y-%m-%d')
    # 데이터 삽입
    cur.execute("INSERT INTO table1 (name, birthday) VALUES (?, ?)", ('이순신', today))

    conn.close()
# test4()

# 데이터 조회- fetchone() 메서드 사용
def test5():
    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    # 데이터 조회
    cur.execute("SELECT * FROM table1")
    row = cur.fetchone()  # 한 행만 가져오기
    print(row)  # 출력: (1, 'Lee', '2025-04-17')

    conn.close()
# test5()

# 데이터 조회- fetchall() 메서드 사용
def test6():
    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    # 데이터 조회
    cur.execute("SELECT * FROM table1")

    tables = cur.fetchall()  # 모든 행 가져오기
    for row in tables:
        print(row)  # 출력: (1, 'Lee', '2025-04-17'), (2, 'Kim', '2025-04-20'), ...

    conn.close()
# test6()

# 데이터 조회(2)- fetchmany() 메서드 사용
def test7():
    conn = sqlite3.connect('testdb_1.db', isolation_level=None)
    cur = conn.cursor()

    # 데이터 조회 방법 1
    param1 = (2,)  # 튜플로 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id=?",param1)
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 2
    param2 = 2  # 정수형 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id=%s"% param2)
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 3
    param3 = {'ID': 2}  # 딕셔너리로 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id=:ID",param3)
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 4
    param4 = (2, 4) # 튜플로 여러 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id IN(?, ?)",param4)  # 모든 행 조회
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 5
    param5 = (2, 4) # 튜플로 여러 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id IN(%d, %d)" % param5)  # 모든 행 조회
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 6
    param6 = (2, 4) # 튜플로 여러 파라미터 전달
    cur.execute("SELECT * FROM table1 WHERE id BETWEEN ? AND ?",param6)  # 모든 행 조회
    print(cur.fetchall())
    print("====================================\n")

    # 데이터 조회 방법 7
    cur.execute("SELECT * FROM table1")  # 모든 행 조회

    # fetchmany() 메서드 사용
    tables = cur.fetchmany(2)  # 2행씩 가져오기
    for row in tables:
        print(row)  # 출력: (1, 'Lee', '2025-04-17'), (2, 'Kim', '2025-04-20')
    conn.close()
test7()

