import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# ==========================================
# 1. 데이터 생성 (Data Generation)
# ==========================================
# 2000년 ~ 2024년 Daily 데이터
dates = pd.date_range(start="2000-01-01", end="2024-01-01", freq="D")
n = len(dates)

np.random.seed(42) # 결과 재현을 위한 시드 고정

# Random Walk with Drift (우상향 트렌드)
start_price = 1000
# 일일 변동폭(정규분포) + 약간의 상승 추세(0.02)
steps = np.random.normal(loc=0.02, scale=1.0, size=n)
price_path = start_price + np.cumsum(steps)

df = pd.DataFrame({
    "date": dates,
    "price": price_path
})

# ==========================================
# 2. 커스텀 테마 설정 (Branding Template)
# ==========================================
# 깔끔한 흰색 배경의 보고서용 테마 정의
report_template = go.layout.Template(
    layout=dict(
        font=dict(family="Arial, sans-serif", color="#2c3e50"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(
            showgrid=True, gridcolor="#ecf0f1", gridwidth=1,
            showline=True, linecolor="#bdc3c7", linewidth=2
        ),
        yaxis=dict(
            showgrid=True, gridcolor="#ecf0f1", gridwidth=1,
            showline=False, side="right" # Y축을 오른쪽에 배치하여 시선 이동 자연스럽게
        ),
        title=dict(font=dict(size=22, color="#2c3e50", family="Arial Black"))
    )
)
pio.templates["report_style"] = report_template
pio.templates.default = "report_style"


# ==========================================
# 3. 기본 차트 그리기
# ==========================================
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["date"], y=df["price"],
    mode="lines",
    name="KOSPI (Simulated)",
    line=dict(color="#34495e", width=1.5)
))


# ==========================================
# 4. 핵심 로직 A: 위기 구간 자동 하이라이팅 (Loop & vrect)
# ==========================================
# 경제 위기 리스트 정의 (이 리스트만 관리하면 됨)
crises = [
    {"name": "닷컴 버블 붕괴", "start": "2000-03-10", "end": "2001-10-31"},
    {"name": "글로벌 금융위기", "start": "2008-01-01", "end": "2009-06-30"},
    {"name": "COVID-19 팬데믹 쇼크", "start": "2020-02-20", "end": "2020-05-20"}
]

# 반복문을 돌며 vrect 영역 표시
for crisis in crises:
    fig.add_vrect(
        x0=crisis["start"], x1=crisis["end"],
        fillcolor="gray", opacity=0.15,
        layer="below", line_width=0,
        annotation_text=crisis["name"], # 상단에 이름 표시
        annotation_position="top left",
        annotation_font=dict(size=10, color="gray")
    )


# ==========================================
# 5. 핵심 로직 B: 최고점/최저점 자동 마킹 (Programmatic Annotation)
# ==========================================
# 최고점 찾기
max_price = df["price"].max()
max_date = df.loc[df["price"].idxmax(), "date"]

# 최저점 찾기
min_price = df["price"].min()
min_date = df.loc[df["price"].idxmax(), "date"]

# 최고점 주석
fig.add_annotation(
    x=max_date, y=max_price,
    text=f"역대 최고점<br>({max_price:.0f}pt)",
    showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2,
    arrowcolor="#e74c3c", bgcolor="rgba(255,255,255,0.8)",
    ax=-20, ay=-40 # 화살표 위치 조정 (위에서 아래로)
)

# 최저점 주석
fig.add_annotation(
    x=min_date, y=min_price,
    text=f"시작점 부근 최저<br>({min_price:.0f}pt)",
    showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2,
    arrowcolor="#27ae60", bgcolor="rgba(255,255,255,0.8)",
    ax=30, ay=40 # 화살표 위치 조정 (아래에서 위로)
)


# ==========================================
# 6. 핵심 로직 C: 브랜딩 서명 (Paper Coordinates)
# ==========================================
fig.add_annotation(
    text="Analysis by **Plotly Master** | Source: Simulated Data",
    x=1, y=-0.1, # 캔버스 오른쪽 하단 바깥쪽
    xref="paper", yref="paper", # Paper 좌표계 필수
    showarrow=False,
    xanchor="right", yanchor="bottom",
    font=dict(size=11, color="gray")
)


# ==========================================
# 7. 최종 레이아웃 다듬기
# ==========================================
fig.update_layout(
    title_text="<b>[장기 추세 리포트] KOSPI와 주요 경제 위기 구간 분석</b>",
    xaxis_title="연도",
    yaxis_title="지수 (포인트)",
    height=700,
    margin=dict(b=100, r=80) # 하단 서명을 위한 여백 확보
)

fig.show()