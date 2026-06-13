import sys

if len(sys.argv) < 2:
    print("사용법:")
    print("추가: python Tutorial_6_memo.py -a \"메모 내용\"")
    print("보기: python Tutorial_6Tutorial_6_memo.py -v")
    exit()

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    with open('memo.txt', 'a', encoding='utf-8') as f:
        f.write(memo + '\n')

elif option == '-v':
    with open('memo.txt', 'r', encoding='utf-8') as f:
        print(f.read())
