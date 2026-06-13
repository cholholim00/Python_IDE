# 품질 관리 차트 (허용 범위 시각화)
import numpy as np
import plotly.graph_objects as go

x = np.arange(100)
y = np.random.normal(50, 5, 100) # 평균 50, 표준편차 5

fig = go.Figure(go.Scatter(x=x, y=y, mode='markers+lines', name='Measured Value'))

# 정상 범위 (45~55) 녹색 음영 처리
fig.add_hrect(
    y0=45, y1=55,
    fillcolor="green", opacity=0.15,
    layer="below", line_width=0,
    annotation_text="Normal Range", annotation_position="top left"
)

# 위험 상한선 (60) 빨간 점선
fig.add_hline(
    y=60,
    line_dash="dot", line_color="red",
    annotation_text="Critical Limit (Upper)", 
    annotation_position="bottom right",
    annotation_font_color="red"
)

fig.update_layout(title="공정 품질 관리 모니터링")
fig.show()