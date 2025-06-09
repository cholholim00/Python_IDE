import sqlite3  # SQLite 데이터베이스를 사용하기 위한 모듈 임포트

def init_db():
    # 데이터베이스 연결(없으면 새로 생성)
    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    # books 테이블이 없으면 생성
    c.execute('''
                CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                publisher TEXT,
                year TEXT,
                stock INTEGER
                )''')
    conn.commit()  # 변경사항 저장
    conn.close()   # 연결 종료

def get_next_id():
    # 데이터베이스 연결
    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    # id를 오름차순으로 모두 조회
    c.execute("SELECT id FROM books ORDER BY id")
    rows = c.fetchall()
    conn.close()

    # 사용 중인 id 리스트 생성
    used_ids = [row[0] for row in rows]
    next_id = 1
    # 비어있는 가장 작은 id 찾기
    for uid in used_ids:
        if uid != next_id:
            break
        next_id += 1
    return next_id

def add_book():
    new_id = get_next_id()  # 새 도서의 id 결정
    # 사용자로부터 도서 정보 입력 받기
    title = input("제목 입력: ")
    author = input("저자 입력: ")
    publisher = input("출판사 입력: ")
    year = input("출판년도 입력: ")
    stock = int(input("재고 수량 입력: "))

    # 데이터베이스 연결 및 도서 정보 삽입
    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    c.execute("INSERT INTO books (id, title, author, publisher, year, stock) VALUES (?, ?, ?, ?, ?, ?)",
              (new_id, title, author, publisher, year, stock))
    conn.commit()
    conn.close()
    print(f"✅ 도서 {new_id}번 추가 완료!")

def delete_book():
    # 삭제할 도서 id 입력 받기
    book_id = int(input("삭제할 도서 ID 입력: "))
    # 데이터베이스 연결 및 해당 id의 도서 삭제
    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ {book_id}번 도서 삭제 완료")

def update_book():
    # 수정할 도서 id 입력 받기
    book_id = int(input("수정할 도서 ID 입력: "))

    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    # 해당 id의 도서 정보 조회
    c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = c.fetchone()

    if book is None:
        print("❌ 해당 ID의 도서가 존재하지 않습니다.")
        conn.close()
        return

    # 현재 도서 정보 출력
    print(f"\n🔍 현재 정보:")
    print(f"제목: {book[1]}, 저자: {book[2]}, 출판사: {book[3]}, 출판년도: {book[4]}, 재고: {book[5]}")

    # 새 정보 입력(Enter 입력 시 기존 값 유지)
    new_title = input(f"새 제목 (현재: {book[1]}) => ") or book[1]
    new_author = input(f"새 저자 (현재: {book[2]}) => ") or book[2]
    new_publisher = input(f"새 출판사 (현재: {book[3]}) => ") or book[3]
    new_year = input(f"새 출판년도 (현재: {book[4]}) => ") or book[4]

    try:
        new_stock_input = input(f"새 재고 (현재: {book[5]}) => ")
        new_stock = int(new_stock_input) if new_stock_input else book[5]
    except ValueError:
        print("❗ 잘못된 재고 입력입니다. 숫자로 입력해주세요.")
        conn.close()
        return

    # 도서 정보 업데이트
    c.execute('''
              UPDATE books
              SET title = ?, author = ?, publisher = ?, year = ?, stock = ?
              WHERE id = ?
              ''', (new_title, new_author, new_publisher, new_year, new_stock, book_id))

    conn.commit()
    conn.close()
    print(f"✅ 도서 {book_id}번 정보가 수정되었습니다.")

def list_books():
    # 데이터베이스 연결 및 모든 도서 조회
    conn = sqlite3.connect("2024201019.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books ORDER BY id")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("📂 등록된 도서가 없습니다.")
        return

    # 도서 목록 출력
    print("\n📚 현재 도서 목록:")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | 재고: {row[5]}")

def main():
    init_db()  # 프로그램 시작 시 DB 초기화(테이블 없으면 생성)
    while True:
        # 메뉴 출력 및 사용자 선택
        print("\n1. 도서 추가 | 2. 도서 삭제 | 3. 도서 수정 | 4. 도서 목록 | exit. 종료")
        choice = input("선택: ")

        # 선택에 따라 함수 호출
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            list_books()
        elif choice == "exit":
            print("📕 프로그램 종료.")
            break
        else:
            print("❗ 잘못된 입력입니다.")

if __name__ == "__main__":
    main()  # 프로그램 실행 진입점