import sqlite3  # SQLite 데이터베이스 사용을 위한 표준 라이브러리 import

# 데이터베이스 연결 및 books 테이블 생성 함수
def connect_db():
    # 2024102011.db라는 파일에 SQLite 연결
    conn = sqlite3.connect("2024201019.db")

    # books 테이블이 없으면 생성
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS books (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,  
                     title TEXT NOT NULL,                   
                     author TEXT NOT NULL,                  
                     publisher TEXT,                        
                     year INTEGER,                          
                     stock INTEGER                         
                     )
                 """)
    return conn  # 연결 객체 반환

# 책 추가 함수 (사용자 입력 기반)
def add_book(conn):
    # 사용자로부터 책 정보 입력 받기
    title = input("제목: ")
    author = input("저자: ")
    publisher = input("출판사: ")
    year = int(input("출판년도: "))
    stock = int(input("재고수량: "))

    # books 테이블에 데이터 삽입
    conn.execute("INSERT INTO books (title, author, publisher, year, stock) VALUES (?, ?, ?, ?, ?)",
                 (title, author, publisher, year, stock))
    conn.commit()  # 변경사항 저장
    print("도서가 추가되었습니다.")

# 전체 도서 목록 출력 함수
def view_books(conn):
    cursor = conn.execute("SELECT * FROM books")  # 모든 도서 조회
    for row in cursor:
        # 각 도서 정보를 보기 좋게 출력
        print(f"[{row[0]}] 제목: {row[1]}, 저자: {row[2]}, 출판사: {row[3]}, 연도: {row[4]}, 재고: {row[5]}")

# 재고 수정 함수
def update_book(conn):
    book_id = input("수정할 도서 ID: ")  # 수정할 도서의 ID 입력
    stock = input("새 재고 수량: ")      # 새 재고 수량 입력
    # 해당 도서의 재고 정보 수정
    conn.execute("UPDATE books SET stock = ? WHERE id = ?", (stock, book_id))
    conn.commit()
    print("재고가 수정되었습니다.")

# 도서 삭제 함수
def delete_book(conn):
    book_id = input("삭제할 도서 ID: ")  # 삭제할 도서의 ID 입력
    # 해당 ID의 도서 삭제
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    print("도서가 삭제되었습니다.")

# 프로그램의 메인 함수
def main():
    conn = connect_db()  # DB 연결 및 테이블 생성

    # 무한 루프를 통해 사용자 메뉴 제공
    while True:
        print("\n1. 도서 추가(add)\n2. 도서 목록(view)\n3. 도서 수정(update)\n4. 도서 삭제(delete)\n5. 종료(end)")
        choice = input("선택: ")

        # 사용자 입력에 따라 기능 호출
        if choice == "1":
            add_book(conn)
        elif choice == "2":
            view_books(conn)
        elif choice == "3":
            update_book(conn)
        elif choice == "4":
            delete_book(conn)
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")  # 예외 처리: 잘못된 번호 입력 시

    conn.close()  # DB 연결 종료

# 이 파일이 메인 프로그램으로 실행될 때만 main() 실행
if __name__ == "__main__":
    main()
