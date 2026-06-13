import os

def search(dirname):
    for filename in os.listdir(dirname):
        full_path = os.path.join(dirname, filename)
        if os.path.isdir(full_path):
            search(full_path)
        else:
            print(full_path)

search("C:/Temp")  # 경로 수정 가능
