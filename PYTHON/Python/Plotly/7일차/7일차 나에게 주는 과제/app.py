import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# ==========================================
# 1. 페이지 설정 (Streamlit Config)
# ==========================================
st.set_page_config(layout="wide", page_title="Pro Quant Dashboard")

st.title("📈 Pro Quant: Real-time Technical Analysis")

# ==========================================
# 2. 사이드바 컨트롤 (User Inputs)
# ==========================================
st.sidebar.header("Chart Settings")

# 티커 입력 (기본값: Apple)
ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL").upper()

# 기간 선택
period = st.sidebar.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

# 지표 ON/OFF 스위치
show_ma = st.sidebar.checkbox("Show MA 20 (이동평균)", value=True)
show_bb = st.sidebar.checkbox("Show Bollinger Bands", value=True)
show_vol = st.sidebar.checkbox("Show Volume", value=True)


# ==========================================
# 3. 데이터 로딩 (Yahoo Finance API)
# ==========================================
@st.cache_data # 데이터 캐싱 (속도 최적화)
def load_data(symbol, p):
    data = yf.Ticker(symbol).history(period=p)
    return data

try:
    df = load_data(ticker, period)
    if df.empty:
        st.error("데이터를 찾을 수 없습니다. 티커를 확인하세요.")
        st.stop()
except Exception as e:
    st.error(f"API Error: {e}")
    st.stop()

# 기술적 지표 계산 (Pandas)
df['MA20'] = df['Close'].rolling(window=20).mean()
df['Std'] = df['Close'].rolling(window=20).std()
df['Upper'] = df['MA20'] + (df['Std'] * 2)
df['Lower'] = df['MA20'] - (df['Std'] * 2)

# 최근 데이터 표시 (KPI)
last_close = df['Close'].iloc[-1]
last_change = last_close - df['Close'].iloc[-2]
col1, col2, col3 = st.columns(3)
col1.metric("Current Price", f"${last_close:.2f}", f"{last_change:.2f}")
col2.metric("High (Period)", f"${df['High'].max():.2f}")
col3.metric("Low (Period)", f"${df['Low'].min():.2f}")


# ==========================================
# 4. 차트 그리기 (Plotly Hardcore Logic)
# ==========================================
# 레이아웃: 캔들(70%) + 거래량(30%)
fig = make_subplots(
    rows=2, cols=1, 
    shared_xaxes=True, 
    vertical_spacing=0.03, 
    row_heights=[0.7, 0.3]
)

# [Row 1] 캔들스틱
fig.add_trace(go.Candlestick(
    x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
    name="OHLC", increasing_line_color='#00CC96', decreasing_line_color='#FF4136'
), row=1, col=1)

# [Row 1] 이동평균선 (옵션)
if show_ma:
    fig.add_trace(go.Scatter(
        x=df.index, y=df['MA20'], 
        line=dict(color='yellow', width=1), name="MA 20"
    ), row=1, col=1)

# [Row 1] 볼린저 밴드 (옵션)
if show_bb:
    fig.add_trace(go.Scatter(
        x=df.index, y=df['Upper'], line=dict(color='gray', width=0.5), 
        name="Upper BB", showlegend=False
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=df.index, y=df['Lower'], line=dict(color='gray', width=0.5), 
        fill='tonexty', fillcolor='rgba(0, 200, 200, 0.1)', 
        name="Bollinger Band"
    ), row=1, col=1)

# [Row 2] 거래량 (옵션)
if show_vol:
    colors = ['#00CC96' if c >= o else '#FF4136' for c, o in zip(df['Close'], df['Open'])]
    fig.add_trace(go.Bar(
        x=df.index, y=df['Volume'], marker_color=colors, name="Volume"
    ), row=2, col=1)

# 스타일링
fig.update_layout(
    title=f"{ticker} Analysis Chart",
    template="plotly_dark", # 다크 테마
    xaxis_rangeslider_visible=False,
    height=700,
    margin=dict(l=50, r=50, t=50, b=50),
    legend=dict(orientation="h", y=1, x=0, bgcolor="rgba(0,0,0,0)")
)

# Y축 설정
fig.update_yaxes(title="Price ($)", row=1, col=1)
fig.update_yaxes(title="Volume", row=2, col=1)


# ==========================================
# 5. Streamlit에 렌더링
# ==========================================
st.plotly_chart(fig, use_container_width=True) # 화면 너비에 맞게 자동 조절