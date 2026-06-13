# 3중 Y축 구현 (주가, 거래량, 보조지표)
import plotly.graph_objects as go

fig = go.Figure()

x_data = [1, 2, 3, 4, 5]

# Trace 1: 주가 (왼쪽 기본 축)
fig.add_trace(go.Scatter(
    x=x_data, y=[1000, 1100, 1050, 1200, 1300],
    name="Price"
))

# Trace 2: 거래량 (오른쪽 첫 번째 축)
fig.add_trace(go.Bar(
    x=x_data, y=[500, 600, 400, 700, 800],
    name="Volume",
    yaxis="y2",
    opacity=0.3
))

# Trace 3: RSI 지표 (오른쪽 두 번째 축)
fig.add_trace(go.Scatter(
    x=x_data, y=[30, 70, 45, 80, 60],
    name="RSI",
    yaxis="y3",
    line=dict(color='red', dash='dot')
))

# Layout 설정 수정
fig.update_layout(
    xaxis=dict(domain=[0.1, 0.85]), # 오른쪽 축 자리를 비우기 위해 domain 조정
    
    # Y축 1 (왼쪽) - titlefont 대신 title=dict(font=...) 사용
    yaxis=dict(
        title=dict(text="Price", font=dict(color="#1f77b4")),
        tickfont=dict(color="#1f77b4")
    ),
    
    # Y축 2 (오른쪽 1)
    yaxis2=dict(
        title=dict(text="Volume", font=dict(color="gray")),
        tickfont=dict(color="gray"),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    
    # Y축 3 (오른쪽 2)
    yaxis3=dict(
        title=dict(text="RSI", font=dict(color="red")),
        tickfont=dict(color="red"),
        anchor="free",
        overlaying="y",
        side="right",
        position=0.95 # 차트 오른쪽 끝에 배치
    )
)

fig.show()