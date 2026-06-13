from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# 다운로드부터 준비까지 세팅
train_dataset = datasets.MNIST(
    root='./dataset',           # 데이터가 저장될 폴더 이름
    train=True,              # 학습용 데이터를 가져올 것인가?
    download=True,           # ★ 폴더에 데이터가 없으면 인터넷에서 다운로드해라!
    transform=transforms.ToTensor() # 이미지를 숫자 배열(Tensor)로 변환
)

# 데이터셋에서 첫 번째 자료 꺼내기 (이미지 하나, 정답 하나)
image, label = train_dataset[0]

# 1. 이미지의 숫자 데이터(Tensor) 출력
print(f"이미지 데이터 구조: {image.shape}") # [1, 28, 28] -> 1채널(흑백), 가로 28, 세로 28
print(f"이 데이터의 실제 정답: {label}")

# 2. 화면에 그리기
# PyTorch는 [채널, 가로, 세로] 순서지만, 그릴 때는 [가로, 세로]만 필요합니다.
plt.imshow(image.squeeze(), cmap='gray')
print(f"이 이미지는 숫자 {label}입니다.")
plt.show()

print(f"전체 데이터 개수: {len(train_dataset)}")

