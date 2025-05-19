import sys
from os import rename, listdir

PATH = '파일이 들어있는 폴더의 경로'

filelist = listdir(PATH)

for name in filelist:
    if name.find('.') < 0:
        continue
    replaced = name.replace("jfif","jpg")
    rename(PATH+'\\'+name, PATH+'\\'+replaced)
    print(name,' -> ',replaced)

print('변환 완료')