from torchvision import transforms
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1단계 텐서 변환 및 정규화

# 전처리 가이드라인 만들기
my_transform = transforms.Compose([
    # 1. 0~255 정수를 0.0~1.0 실수로 바꾸고, PyTorch가 읽는 방식(Tensor)으로 변환
    transforms.ToTensor(),
    
    # 2. 정규화 (평균 0.1307, 표준편차 0.3081로 맞춤 - MNIST 공식 통계값)
    # 데이터가 한쪽으로 쏠리는 것을 방지합니다.
    transforms.Normalize((0.1307,), (0.3081,))
])

# 2단계 : 배치 사이즈 먄들기
# 위에서 만든 my_transform을 적용해서 다시 선언
train_dataset = datasets.MNIST(root='./dataset', train=True, download=True, transform=my_transform)

# 64개씩 묶어서 전달하는 '배달원' 생성
# shuffle=True: 공부할 때 순서를 외우지 못하게 매번 섞어줍니다.
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# 3단계: 모양 꺼내기
# 실제 데이터 한 묶음을 꺼내서 확인해봅시다.
images, labels = next(iter(train_loader))

print(f"배치 크기: {images.shape}") # [64, 1, 28, 28] -> 64장, 1채널, 가로28, 세로28

# 모델에 넣기 위해 784개로 펼치기
flatten_images = images.view(images.size(0), -1) 
print(f"펼쳐진 모양: {flatten_images.shape}") # [64, 784]

