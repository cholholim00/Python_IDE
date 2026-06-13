import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ==========================================
# 1. 데이터 생성 및 전처리 (Data Processing)
# ==========================================
# 1년치(365일) 데이터 생성
dates = pd.date_range(start="2023-01-01", periods=365, freq="D")
np.random.seed(42)

# 주가 흐름 (Random Walk)
close = np.cumsum(np.random.randn(365)) + 100
# 시가, 고가, 저가 생성 (변동성 부여)
open_p = close + np.random.randn(365) * 0.5
high = np.maximum(open_p, close) + np.random.rand(365)
low = np.minimum(open_p, close) - np.random.rand(365)
# 거래량 (0 ~ 1000)
volume = np.random.randint(100, 1000, 365)

df = pd.DataFrame({
    'Date': dates, 'Open': open_p, 'High': high, 'Low': low, 'Close': close, 'Volume': volume
})

# --- [Quant Logic] 지표 계산 ---
# 1. 이동평균선 (20일)
df['MA20'] = df['Close'].rolling(window=20).mean()

# 2. 볼린저 밴드 (표준편차 2배)
df['Std'] = df['Close'].rolling(window=20).std()
df['Upper'] = df['MA20'] + (df['Std'] * 2)
df['Lower'] = df['MA20'] - (df['Std'] * 2)

# 3. 거래량 색상 로직 (상승장: 빨강, 하락장: 파랑) - Numpy vectorization
# 한국식 표기: 종가 >= 시가 이면 빨강(상승)
vol_colors = np.where(df['Close'] >= df['Open'], '#EF553B', '#636EFA') 


# ==========================================
# 2. 레이아웃 아키텍처 (2 Rows)
# ==========================================
fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True, # X축 공유 (줌 동기화)
    vertical_spacing=0.03, # 두 차트 사이 간격을 좁혀서 하나처럼 보이게 함
    row_heights=[0.7, 0.3] # 7:3 비율
)

# ==========================================
# 3. 시각화 (Visualization)
# ==========================================

# --- [Row 1] 캔들스틱 & 볼린저 밴드 ---

# (1) 볼린저 밴드 하한선 (선만 그리기, 색은 흐리게)
fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['Lower'],
        line=dict(color='rgba(255, 255, 255, 0.3)', width=1), # 아주 흐린 선
        name="Lower Band", showlegend=False
    ),
    row=1, col=1
)

# (2) 볼린저 밴드 상한선 + 채우기 (핵심!)
fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['Upper'],
        line=dict(color='rgba(255, 255, 255, 0.3)', width=1),
        fill='tonexty', # 바로 직전 trace(하한선)까지 영역 채우기
        fillcolor='rgba(0, 255, 255, 0.1)', # 반투명 청록색 채우기
        name="Bollinger Band", showlegend=True
    ),
    row=1, col=1
)

# (3) 중심선 (MA20)
fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['MA20'],
        line=dict(color='yellow', width=1.5, dash='dash'), # 노란 점선
        name="MA 20"
    ),
    row=1, col=1
)

# (4) 메인 캔들스틱 (가장 위에 그려지도록 마지막에 추가하거나 레이어 조정)
fig.add_trace(
    go.Candlestick(
        x=df['Date'],
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'],
        increasing_line_color='#EF553B', # 빨강
        decreasing_line_color='#636EFA', # 파랑
        name="Price"
    ),
    row=1, col=1
)

# --- [Row 2] 거래량 (Volume) ---
fig.add_trace(
    go.Bar(
        x=df['Date'], y=df['Volume'],
        marker_color=vol_colors, # 미리 계산한 색상 배열 적용
        name="Volume"
    ),
    row=2, col=1
)


# ==========================================
# 4. 스타일링 (Final Polish)
# ==========================================
fig.update_layout(
    title="<b>Pro Trader's Technical Chart</b> (Bollinger + Vol)",
    template="plotly_dark", # 다크 테마
    xaxis_rangeslider_visible=False, # 하단 슬라이더 제거 (공간 확보)
    height=800,
    margin=dict(t=80, b=50, l=60, r=40),
    legend=dict(x=0, y=1, orientation="h", bgcolor="rgba(0,0,0,0)") # 범례를 차트 안으로 넣기
)

# Y축 포맷팅 (콤마 표시 등)
fig.update_yaxes(title="Price", tickformat=",", row=1, col=1)
fig.update_yaxes(title="Vol", row=2, col=1)

# 캔들스틱의 Range Slider를 끄려면 update_xaxes가 아니라 layout 레벨에서 처리하거나
# 각 x축 설정에서 rangeslider=dict(visible=False)를 해야 함
fig.update_xaxes(rangeslider=dict(visible=False), row=1, col=1)
fig.update_xaxes(rangeslider=dict(visible=False), row=2, col=1)

fig.show()