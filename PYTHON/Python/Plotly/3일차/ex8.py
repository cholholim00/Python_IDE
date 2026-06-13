# 경영진 현황판 (Indicator + Table)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "indicator"}, {"type": "table"}]], # 계기판 vs 표
    column_widths=[0.3, 0.7]
)

# 1. Indicator (계기판)
fig.add_trace(
    go.Indicator(
        mode="number+delta",
        value=450,
        delta={"reference": 400, "relative": True, "valueformat": ".1%"},
        title={"text": "오늘의 매출 달성률"},
        domain={"x": [0, 1], "y": [0, 1]} # 자체 도메인 설정
    ),
    row=1, col=1
)

# 2. Table (표)
fig.add_trace(
    go.Table(
        header=dict(values=["Product", "Price", "Stock"], fill_color="paleturquoise"),
        cells=dict(values=[["A", "B", "C"], [100, 200, 150], [50, 30, 0]])
    ),
    row=1, col=2
)

fig.update_layout(height=300)
fig.show()