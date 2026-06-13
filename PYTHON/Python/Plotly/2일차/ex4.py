# 워터마크와 고정 타이틀 배치
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 20, 30], name="Data"))

fig.update_layout(
    # 1. Paper 좌표계를 이용한 워터마크 (정중앙 고정)
    annotations=[
        dict(
            text="CONFIDENTIAL",
            x=0.5, y=0.5,      # 캔버스 중앙
            xref="paper", yref="paper", # Paper 좌표계 사용
            showarrow=False,
            font=dict(size=60, color="rgba(255,0,0,0.1)") # 투명도 조절
        ),
        # 2. Data 좌표계를 이용한 특정 포인트 강조
        dict(
            text="Highest Point",
            x=3, y=30,          # 데이터 값 기준
            xref="x", yref="y", # Data 좌표계 사용
            arrowhead=2,
            ax=-50, ay=-30      # 화살표 꼬리 위치 (픽셀 단위)
        )
    ],
    title="좌표계 혼합 사용 예제"
)

fig.show()