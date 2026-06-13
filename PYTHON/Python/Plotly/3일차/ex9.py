# Picture-in-Picture (PIP) 구현
import plotly.graph_objects as go
fig = go.Figure()

# 메인 차트 (전체 영역 사용)
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4], y=[10, 15, 13, 17],
    name="Main Trend"
))

# Inset 차트 (왼쪽 상단 작게 배치)
# xaxis2, yaxis2를 새로 정의하고 domain을 지정
fig.add_trace(go.Scatter(
    x=[1, 2], y=[10, 12],
    xaxis="x2", yaxis="y2", # 두 번째 축 사용
    name="Zoom In",
    line=dict(color="red")
))

fig.update_layout(
    xaxis=dict(domain=[0, 1]), # 메인 X축 (전체)
    yaxis=dict(domain=[0, 1]), # 메인 Y축 (전체)
    
    # Inset 축 정의 (왼쪽 상단 30% 영역 차지)
    xaxis2=dict(domain=[0.05, 0.35], anchor="y2"), 
    yaxis2=dict(domain=[0.65, 0.95], anchor="x2"),
    
    title="Inset Plot Example (PIP)"
)

fig.show()