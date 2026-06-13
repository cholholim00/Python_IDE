# 실험 데이터와 신뢰구간
import plotly.graph_objects as go
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)
y_upper = y + 0.2 # 상한선 (오차 +0.2)
y_lower = y - 0.2 # 하한선 (오차 -0.2)

fig = go.Figure()

# 1. 신뢰구간 (배경에 깔기) - 채우기(fill) 기법
fig.add_trace(go.Scatter(
    x=np.concatenate([x, x[::-1]]), # x를 갔다가 다시 거꾸로 돌아옴 (폐곡선 만들기)
    y=np.concatenate([y_upper, y_lower[::-1]]), # 상한선 갔다가 하한선으로 돌아옴
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)', # 반투명 청록색
    line=dict(color='rgba(255,255,255,0)'), # 테두리 선 없음
    hoverinfo="skip",
    name="95% Confidence Interval"
))

# 2. 메인 데이터 라인
fig.add_trace(go.Scatter(x=x, y=y, line=dict(color='rgb(0,100,80)'), name="Mean Value"))

# 3. 특정 포인트에 오차 막대 추가 (샘플링)
sample_indices = np.arange(0, 100, 10)
fig.add_trace(go.Scatter(
    x=x[sample_indices], y=y[sample_indices],
    mode='markers',
    error_y=dict(
        type='data', 
        array=[0.3]*10, # 오차 값 (배열로 개별 지정 가능)
        visible=True
    ),
    name="Measurements"
))

fig.update_layout(title="Scientific Experiment Results")
fig.show()