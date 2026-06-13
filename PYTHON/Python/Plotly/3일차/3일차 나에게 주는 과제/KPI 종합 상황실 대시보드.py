import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ==========================================
# 1. 가상 데이터 생성 (Dummy Data)
# ==========================================
# (1) 메인 시계열 데이터
dates = pd.date_range(start="2023-01-01", periods=100, freq="W")
np.random.seed(42)
sales_trend = np.cumsum(np.random.randn(100) * 10 + 5) + 1000 # 우상향 트렌드

# (2) KPI 데이터
current_sales = sales_trend[-1]
prev_sales = sales_trend[-2]
profit_margin = 24.5 # %

# (3) 제품별 데이터
products = ["Electronics", "Fashion", "Home", "Beauty", "Sports"]
sales_share = [4500, 3200, 1500, 1200, 800] # Pie Chart용
top_products_df = pd.DataFrame({
    "Rank": [1, 2, 3, 4, 5],
    "Product": ["스마트폰 17", "러닝화", "OLED TV", "스마트 워치", "겨울 코트"],
    "Revenue ($)": ["$1.2M", "$850K", "$620K", "$450K", "$300K"],
    "Growth": ["+12%", "+5%", "-2%", "+15%", "+8%"]
})

# ==========================================
# 2. 레이아웃 아키텍처 설계 (The Blueprint)
# ==========================================
# 3행 2열 구조
# Row 1: Indicator (KPI)
# Row 2: XY Plot (Main Trend) - 2칸 병합
# Row 3: Domain (Pie) + Table
specs = [
    [{"type": "indicator"}, {"type": "indicator"}],    # Row 1
    [{"colspan": 2, "type": "xy"}, None],              # Row 2 (Merge)
    [{"type": "domain"}, {"type": "table"}]            # Row 3
]

fig = make_subplots(
    rows=3, cols=2,
    specs=specs,
    vertical_spacing=0.15,
    horizontal_spacing=0.1,
    subplot_titles=("총 수익", "영업이익률", "주간 판매 추세 (글로벌)", 
                    "카테고리별 매출", "인기 상품 5가지 목록"),
    row_heights=[0.2, 0.4, 0.4] # 행 높이 비율 조정 (중간 차트를 가장 크게)
)

# ==========================================
# 3. 데이터 시각화 구현 (Visualization)
# ==========================================

# --- [Row 1, Col 1] 총 매출 KPI (Indicator) ---
fig.add_trace(
    go.Indicator(
        mode="number+delta",
        value=current_sales,
        number={'prefix': "$", 'suffix': "K"},
        delta={'reference': prev_sales, 'relative': True, 'position': "top", 'valueformat': ".1%"},
        title={"text": "이번 주 판매"}
    ),
    row=1, col=1
)

# --- [Row 1, Col 2] 영업 이익률 (Gauge) ---
fig.add_trace(
    go.Indicator(
        mode="gauge+number",
        value=profit_margin,
        number={'suffix': "%"},
        gauge={
            'axis': {'range': [0, 50]}, # 최대 50% 가정
            'bar': {'color': "#EF553B"}, # 붉은색 게이지 바
            'bgcolor': "rgba(50,50,50,1)", # 어두운 배경
            'steps': [
                {'range': [0, 10], 'color': "gray"},
                {'range': [10, 30], 'color': "lightgray"}
            ],
            'threshold': {
                'line': {'color': "green", 'width': 4},
                'thickness': 0.75,
                'value': 30 # 목표치
            }
        },
        title={"text": "Operating Profit Margin"}
    ),
    row=1, col=2
)

# --- [Row 2] 메인 시계열 차트 (Line) ---
fig.add_trace(
    go.Scatter(
        x=dates, y=sales_trend,
        mode="lines", fill='tozeroy', # 영역 채우기
        name="Weekly Sales",
        line=dict(color="#00CC96", width=2)
    ),
    row=2, col=1
)

# --- [Row 3, Col 1] 제품 비중 (Pie) ---
fig.add_trace(
    go.Pie(
        labels=products, values=sales_share,
        hole=0.4, # 도넛 차트 스타일
        marker=dict(colors=pd.Series(sales_share).apply(lambda x: "#636EFA")), # 단일 색조
        textinfo='label+percent',
        showlegend=False
    ),
    row=3, col=1
)

# --- [Row 3, Col 2] 상세 테이블 (Table) ---
fig.add_trace(
    go.Table(
        header=dict(
            values=list(top_products_df.columns),
            fill_color="black",
            font=dict(color="white", size=12),
            align="center"
        ),
        cells=dict(
            values=[top_products_df[k].tolist() for k in top_products_df.columns],
            fill_color="white",
            font=dict(color="black", size=11),
            align="center",
            height=30
        )
    ),
    row=3, col=2
)

# ==========================================
# 4. 스타일링 및 슬라이더 설정 (Final Polish)
# ==========================================
fig.update_layout(
    template="plotly_dark", # 다크 모드 적용
    height=1300, # 전체 높이 충분히 확보
    title_text="<b>🚀 글로벌 영업 지휘 센터</b>",
    title_x=0.5,
    title_font_size=24,
    showlegend=False, # KPI 대시보드에서는 범례가 지저분할 수 있음
    margin=dict(t=100, b=100, l=80, r=80), # 여백 조정
)

# Row 2 (메인 차트)에만 Range Slider 적용
fig.update_xaxes(
    rangeslider=dict(visible=True, thickness=0.05), # 두께를 5%로 얇게 설정
    row=2, col=1
)

fig.show()