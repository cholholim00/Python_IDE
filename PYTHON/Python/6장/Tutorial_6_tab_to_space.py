import sys

if len(sys.argv) < 3:
    print("사용법: python Tutorial_6_tab_to_space.py source.txt result.txt")
    exit()

src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\t', ' ' * 4)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)
