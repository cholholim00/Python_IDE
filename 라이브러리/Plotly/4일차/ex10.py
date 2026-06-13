# 캔들스틱 + 이동평균선(MA) 오버레이
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 1. 가상 금융 데이터 생성 (OHLC)
dates = pd.date_range(start="2024-01-01", periods=100, freq="D")
np.random.seed(42)
close_prices = np.cumsum(np.random.randn(100)) + 100
open_prices = close_prices + np.random.randn(100) * 0.5
high_prices = np.maximum(open_prices, close_prices) + np.random.rand(100)
low_prices = np.minimum(open_prices, close_prices) - np.random.rand(100)

df = pd.DataFrame({
    'Date': dates, 'Open': open_prices, 'High': high_prices, 
    'Low': low_prices, 'Close': close_prices
})

# 2. 기술적 지표 계산 (Pandas Rolling)
# 5일 이동평균선, 20일 이동평균선
df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()

# 3. 시각화 (Candlestick + Line)
fig = go.Figure()

# 메인 캔들스틱
fig.add_trace(go.Candlestick(
    x=df['Date'],
    open=df['Open'], high=df['High'],
    low=df['Low'], close=df['Close'],
    name="OHLC",
    increasing_line_color='red', decreasing_line_color='blue' # 한국식 (상승:빨강)
))

# 이동평균선 겹쳐 그리기
fig.add_trace(go.Scatter(x=df['Date'], y=df['MA5'], line=dict(color='orange', width=1), name="MA 5"))
fig.add_trace(go.Scatter(x=df['Date'], y=df['MA20'], line=dict(color='purple', width=1), name="MA 20"))

fig.update_layout(title="Technical Analysis Chart", xaxis_rangeslider_visible=False)
fig.show()