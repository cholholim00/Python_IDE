import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ==========================================
# 1. 데이터 생성 (Data Generation)
# ==========================================
dates = pd.date_range(start="2023-01-01", periods=200, freq="D")
np.random.seed(42)

close = np.cumsum(np.random.randn(200)) + 100
open_p = close + np.random.randn(200) * 0.5
high = np.maximum(open_p, close) + np.random.rand(200)
low = np.minimum(open_p, close) - np.random.rand(200)
volume = np.random.randint(100, 1000, 200)

df = pd.DataFrame({'Date': dates, 'Open': open_p, 'High': high, 'Low': low, 'Close': close, 'Volume': volume})

# 지표 계산
df['MA20'] = df['Close'].rolling(window=20).mean()
df['Std'] = df['Close'].rolling(window=20).std()
df['Upper'] = df['MA20'] + (df['Std'] * 2)
df['Lower'] = df['MA20'] - (df['Std'] * 2)
vol_colors = np.where(df['Close'] >= df['Open'], '#EF553B', '#636EFA')

# ==========================================
# 2. 레이아웃 및 Trace 배치 (순서 중요!)
# ==========================================
fig = make_subplots(
    rows=2, cols=1, shared_xaxes=True, 
    vertical_spacing=0.03, row_heights=[0.7, 0.3]
)

# [Trace 0] Lower Band
fig.add_trace(go.Scatter(x=df['Date'], y=df['Lower'], line=dict(color='gray', width=1), name="Lower"), row=1, col=1)

# [Trace 1] Upper Band
fig.add_trace(go.Scatter(x=df['Date'], y=df['Upper'], line=dict(color='gray', width=1), fill='tonexty', fillcolor='rgba(0,255,255,0.1)', name="Upper"), row=1, col=1)

# [Trace 2] MA20
fig.add_trace(go.Scatter(x=df['Date'], y=df['MA20'], line=dict(color='yellow', width=1, dash='dash'), name="MA20"), row=1, col=1)

# [Trace 3] Candlestick (기본값: Visible)
fig.add_trace(go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="Candle"), row=1, col=1)

# [Trace 4] Line Chart (기본값: Hidden) -> 캔들 대신 보여줄 라인 차트
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', line=dict(color='white', width=2), name="Line", visible=False), row=1, col=1)

# [Trace 5] Volume
fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], marker_color=vol_colors, name="Volume"), row=2, col=1)


# ==========================================
# 3. 인터랙티브 컨트롤 구현 (Updatemenus)
# ==========================================
fig.update_layout(
    updatemenus=[
        # (1) 차트 타입 변경 드롭다운 (Dropdown)
        dict(
            type="dropdown",
            direction="down",
            active=0, 
            x=0.1, y=1.15, # 위치: 좌측 상단
            buttons=list([
                dict(label="🕯️ Candlestick",
                     method="update", # method="update"는 data와 layout 둘 다 건드림
                     args=[{"visible": [True, True, True, True, False, True]}, # Trace 3(Candle) 켜고, 4(Line) 끔
                           {"title": "Candlestick View"}]),
                dict(label="📈 Line Chart",
                     method="update",
                     args=[{"visible": [True, True, True, False, True, True]}, # Trace 3(Candle) 끄고, 4(Line) 켬
                           {"title": "Line Chart View"}]),
            ]),
        ),
        # (2) 레이어 ON/OFF 버튼 그룹 (Buttons)
        dict(
            type="buttons",
            direction="left",
            x=0.5, y=1.15, # 위치: 중앙 상단
            buttons=list([
                # 볼린저 밴드 토글 (Trace 0, 1, 2 제어)
                dict(label="Bollinger ON",
                     method="restyle", # restyle: 데이터 속성만 변경
                     args=[{"visible": True}, [0, 1, 2]]), # [0, 1, 2]번 Trace만 True로
                dict(label="OFF",
                     method="restyle",
                     args=[{"visible": False}, [0, 1, 2]]),
                
                # 거래량 토글 (Trace 5 제어)
                dict(label="Volume ON",
                     method="restyle",
                     args=[{"visible": True}, [5]]),
                dict(label="OFF",
                     method="restyle",
                     args=[{"visible": False}, [5]]),
            ]),
        )
    ]
)

# ==========================================
# 4. 기간 선택기 (Range Selector)
# ==========================================
fig.update_xaxes(
    rangeslider_visible=False,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1M", step="month", stepmode="backward"),
            dict(count=3, label="3M", step="month", stepmode="backward"),
            dict(step="all", label="All")
        ]),
        bgcolor="rgba(50,50,50,0.8)", # 버튼 배경색
        font=dict(color="white")
    ),
    row=1, col=1
)

# 최종 스타일링
fig.update_layout(
    title="<b>Interactive Trading Suite</b>",
    template="plotly_dark",
    height=800,
    margin=dict(t=100, l=50, r=50),
    legend=dict(orientation="h", y=1, x=0.6)
)
fig.update_yaxes(title="Price", row=1, col=1)
fig.update_yaxes(title="Vol", row=2, col=1)

fig.show()