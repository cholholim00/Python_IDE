import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ==========================================
# 1. 데이터 생성 (Data Generation)
# ==========================================
# 1분 단위 24시간 시간축
time_index = pd.date_range(start="2024-02-01 00:00", periods=1440, freq="T")

np.random.seed(42) # 결과 재현을 위한 시드 고정

df = pd.DataFrame({
    "time": time_index,
    "temp": np.random.normal(300, 10, 1440),   # 센서 A: 온도
    "pressure": np.random.normal(50, 5, 1440), # 센서 B: 압력
    "vibration": np.random.rand(1440) * 10     # 센서 C: 진동 (기본 0~10)
})

# 이상치(Outlier) 강제 주입 (3곳)
outlier_indices = [200, 800, 1200]
df.loc[outlier_indices, "vibration"] = [55, 82, 60]  # 50을 넘는 값들

# ==========================================
# 2. 그래프 프레임워크 설계 (Subplots)
# ==========================================
# Row 1은 이중 축(Dual Axis)을 써야 하므로 specs에서 secondary_y=True 설정
fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True, # X축 공유 (줌 인/아웃 동기화 핵심)
    vertical_spacing=0.1,
    subplot_titles=("센서 A 및 B (온도/압력)", "센서 C (진동 분석)"),
    specs=[[{"secondary_y": True}],  # 1행: 이중 축 사용
           [{"secondary_y": False}]] # 2행: 단일 축
)

# ==========================================
# 3. 데이터 매핑 (Tracing)
# ==========================================

# [Row 1] 센서 A (온도) - 왼쪽 Y축
fig.add_trace(
    go.Scatter(x=df["time"], y=df["temp"], name="온도(°C)",
               line=dict(color="#00CC96", width=1.5)),
    row=1, col=1, secondary_y=False
)

# [Row 1] 센서 B (압력) - 오른쪽 Y축
fig.add_trace(
    go.Scatter(x=df["time"], y=df["pressure"], name="압력(bar)",
               line=dict(color="#EF553B", width=1.5, dash="dot")), # 점선 처리
    row=1, col=1, secondary_y=True
)

# [Row 2] 센서 C (진동) - WebGL 사용 (Scattergl)
fig.add_trace(
    go.Scattergl(x=df["time"], y=df["vibration"], name="진동(Hz)",
                 mode="markers", # 라인 없이 점만 찍기
                 marker=dict(size=4, color="#AB63FA", opacity=0.6)),
    row=2, col=1
)

# ==========================================
# 4. 핵심 로직: 이상치 자동 감지 및 주석 달기
# ==========================================
# 진동 값이 50 넘는 데이터만 필터링
outliers = df[df["vibration"] > 50]

for _, row in outliers.iterrows():
    fig.add_annotation(
        x=row["time"],
        y=row["vibration"],
        text="⚠️ WARNING(경고)",
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        font=dict(color="red", size=12, weight="bold"),
        row=2, col=1 # 2번째 서브플롯에 달아야 함
    )
    
    # 시각적 강조를 위해 빨간 원(Circle) 추가
    fig.add_trace(
        go.Scatter(x=[row["time"]], y=[row["vibration"]],
                   mode="markers", marker=dict(color="red", size=12, symbol="circle-open", line=dict(width=2)),
                   showlegend=False, name="Alert"),
        row=2, col=1
    )

# ==========================================
# 5. 하드코어 레이아웃 스타일링
# ==========================================
fig.update_layout(
    title_text="<b>🏭 반도체 공정 센서 모니터링 시스템</b>",
    title_x=0.5,
    template="plotly_dark", # 다크 모드
    height=800,
    showlegend=True,
    margin=dict(t=100, b=50, l=60, r=60),
    
    # 하단 Range Slider 설정 (Row 2의 X축에 적용되지만 shared_xaxes로 인해 전체 적용됨)
    xaxis2=dict(
        rangeslider=dict(visible=True),
        type="date"
    )
)

# Y축 라벨 정리
fig.update_yaxes(title_text="Temp (°C)", row=1, col=1, secondary_y=False)
fig.update_yaxes(title_text="Pressure (bar)", row=1, col=1, secondary_y=True)
fig.update_yaxes(title_text="Vibration (Hz)", row=2, col=1)

fig.show()