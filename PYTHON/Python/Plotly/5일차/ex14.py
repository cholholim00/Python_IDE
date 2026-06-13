# 국가별 데이터 필터링 드롭다운
import plotly.graph_objects as go
import numpy as np

# 가상 데이터
countries = ["Korea", "USA", "Japan"]
data = {c: np.random.randn(10) + i*2 for i, c in enumerate(countries)}

fig = go.Figure()

# 1. 모든 국가의 선을 일단 다 그린다 (Trace 3개 생성)
for country in countries:
    fig.add_trace(go.Scatter(y=data[country], name=country, visible=True)) # 처음엔 다 보임

# 2. 드롭다운 버튼 생성 로직
buttons = []

# (1) 'All' 버튼
buttons.append(dict(
    label="All",
    method="update",
    args=[{"visible": [True, True, True]}, # Trace 1, 2, 3 모두 True
          {"title": "All Countries"}]      # 레이아웃 제목 변경
))

# (2) 각 국가별 버튼
# visible 리스트 생성 로직: [True, False, False], [False, True, False] ...
for i, country in enumerate(countries):
    visibility = [False] * len(countries)
    visibility[i] = True # 현재 국가만 True
    
    buttons.append(dict(
        label=country,
        method="update",
        args=[{"visible": visibility}, 
              {"title": f"{country} Performance"}]
    ))

fig.update_layout(
    updatemenus=[dict(
        active=0, # 첫 번째 버튼(All)이 기본 활성화
        buttons=buttons,
        x=1.1, y=1 # 위치: 우측 상단
    )]
)

fig.show()