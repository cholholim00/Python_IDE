import cv2

def vide_cap_create():
    video_path = "test_set.mp4"
    cap = cv2.VideoCapture(video_path)
    return cap

def get_vide_fps(in_cap):
    fps = int (in_cap.get(cv2.CAP_PROP_FPS))
    return fps

def get_video_width(in_cap):
    width = int(in_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    return width

def get_video_height(in_cap):
    height = int(in_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return height

def change_video_wh(in_fram, in_width, hin_eight):
    re_frame = cv2.resize(in_fram, (in_width, hin_eight))
    return re_frame

def save_video_image(in_cap, in_fps):
    cnt = 0
    while True:
        ret, frame = in_cap.read()
        if not ret:
            return -1
        else:
            if cnt % in_fps == 0:
                file_name ="img"+str(cnt)+".jpg"
                re_frame = change_video_wh(frame, 300, 400)
                cv2.imwrite(file_name, re_frame)
            cnt += 1
            print(cnt)


cap = vide_cap_create()
save_video_image(cap,24)
fps = get_vide_fps(cap)
width = get_video_width(cap)
height = get_video_height(cap)

print("width = ", width)
print("height = ", height)
print("fps = ",fps)

