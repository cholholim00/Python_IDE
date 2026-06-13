# 비대칭 레이아웃 설계
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 레이아웃 구상:
# 1행: 전체를 차지하는 메인 그래프 (colspan=2)
# 2행: 왼쪽(Bar), 오른쪽(Pie) 반반 나누기

fig = make_subplots(
    rows=2, cols=2,
    # 각 컬럼의 너비 비율 설정 (예: 7:3 비율로 나누고 싶을 때 유용)
    column_widths=[0.7, 0.3], 
    
    # specs: 서브플롯의 성격을 정의하는 매트릭스
    specs=[
        [{"colspan": 2}, None], # (1,1)은 2칸 차지, (1,2)는 None으로 비워둠
        [{"type": "xy"}, {"type": "domain"}] # (2,1)은 XY좌표계, (2,2)는 Pie용 Domain
    ],
    subplot_titles=("Main Time Series (Full Width)", "Category Analysis", "Market Share")
)

# (1,1) 메인 그래프
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="Trend"), row=1, col=1)

# (2,1) 막대 그래프
fig.add_trace(go.Bar(x=["A", "B", "C"], y=[10, 20, 15], name="Category"), row=2, col=1)

# (2,2) 파이 차트 (Pie는 XY축이 아닌 Domain을 씀)
fig.add_trace(go.Pie(labels=["Yes", "No"], values=[60, 40], name="Share"), row=2, col=2)

fig.update_layout(title_text="Complex Grid Layout Example", height=600)
fig.show()