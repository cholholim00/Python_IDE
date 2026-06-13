# 0만 개 데이터 렌더링 성능 테스트
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 10만 개 난수 생성
N = 100000
df = pd.DataFrame({
    'x': np.random.randn(N),
    'y': np.random.randn(N),
    'color': np.random.randn(N)
})

# 일반 Scatter vs WebGL Scatter 비교
# fig = go.Figure(go.Scatter(...)) # 느림 (SVG 렌더링)

fig = go.Figure(data=go.Scattergl( # 빠름 (WebGL GPU 가속)
    x=df['x'],
    y=df['y'],
    mode='markers',
    marker=dict(
        color=df['color'],
        colorscale='Viridis',
        line_width=0, # 선 없애야 성능 더 좋음
        opacity=0.5
    )
))

fig.update_layout(title=f"WebGL Performance Test: {N} Points")
fig.show()