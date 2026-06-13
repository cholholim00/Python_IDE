# 3D 지형 및 등고선
import numpy as np
import plotly.graph_objects as go

# 3차원 데이터 생성 (Sinc 함수)
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) / R # 높이 값

fig = go.Figure(data=[go.Surface(z=Z, x=x, y=y)])

fig.update_layout(
    title='3D Surface Plot', 
    autosize=False,
    width=600, height=600,
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Amplitude'
    )
)
fig.show()