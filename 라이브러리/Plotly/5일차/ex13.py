# 차트 타입 변환기 (Bar ↔ Scatter)
import plotly.graph_objects as go

x = ["A", "B", "C", "D"]
y = [10, 15, 7, 12]

fig = go.Figure()

# 초기 상태: Bar Chart
fig.add_trace(go.Bar(x=x, y=y, name="Data"))

fig.update_layout(
    title="차트 변신 로봇",
    updatemenus=[
        dict(
            type="buttons", # 'dropdown'으로 바꾸면 콤보박스가 됨
            direction="left",
            buttons=list([
                # 버튼 1: Bar Chart로 변환 (restyle)
                dict(
                    label="Bar Chart",
                    method="restyle",
                    args=[{"type": "bar", "marker.color": "teal"}] # 데이터 속성 변경
                ),
                # 버튼 2: Scatter Chart로 변환 (restyle)
                dict(
                    label="Line Chart",
                    method="restyle",
                    args=[{"type": "scatter", "mode": "lines+markers", "line.color": "crimson"}]
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.5, xanchor="center", y=1.15, yanchor="top"
        ),
    ]
)

fig.show()