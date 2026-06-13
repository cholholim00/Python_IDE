# Corporate Identity 테마 제작 및 등록
import plotly.io as pio
import plotly.graph_objects as go

# 1. 나만의 테마 정의 (딕셔너리 구조)
my_corporate_theme = go.layout.Template(
    layout=dict(
        font=dict(family="Verdana", color="#333333"),
        title=dict(font=dict(size=24, color="#1f77b4", family="Arial Black")),
        plot_bgcolor="white", # 그래프 영역 배경
        paper_bgcolor="#f8f9fa", # 전체 캔버스 배경
        xaxis=dict(
            showgrid=True, gridwidth=1, gridcolor="#e5e5e5",
            showline=True, linewidth=2, linecolor="#333333"
        ),
        yaxis=dict(
            showgrid=True, gridwidth=1, gridcolor="#e5e5e5",
            showline=False
        ),
        colorway=["#003f5c", "#7a5195", "#ef5675", "#ffa600"] # 회사 전용 컬러 팔레트
    )
)

# 2. 테마 등록 (이제 'my_style'이라는 이름으로 언제든 호출 가능)
pio.templates["my_style"] = my_corporate_theme
pio.templates.default = "my_style" # 기본값으로 설정

# 3. 테스트 (설정 안 해도 자동으로 테마 적용됨)
fig = go.Figure(data=[
    go.Bar(name='Prod A', x=['Q1', 'Q2', 'Q3'], y=[10, 20, 15]),
    go.Bar(name='Prod B', x=['Q1', 'Q2', 'Q3'], y=[5, 15, 25])
])
fig.update_layout(title="Corporate Theme 자동 적용 테스트")
fig.show()