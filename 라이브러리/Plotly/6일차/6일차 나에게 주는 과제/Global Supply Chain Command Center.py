import plotly.graph_objects as go
import pandas as pd

# ==========================================
# 1. 데이터 정의 (Hubs & Routes)
# ==========================================
# 주요 허브 데이터 (위경도 및 재고량)
hubs = {
    "New York": {"lat": 40.7128, "lon": -74.0060, "vol": 850, "code": "JFK"},
    "London":   {"lat": 51.5074, "lon": -0.1278,  "vol": 620, "code": "LHR"},
    "Tokyo":    {"lat": 35.6895, "lon": 139.6917, "vol": 940, "code": "NRT"},
    "Shanghai": {"lat": 31.2304, "lon": 121.4737, "vol": 780, "code": "PVG"},
    "Sydney":   {"lat": -33.8688,"lon": 151.2093, "vol": 450, "code": "SYD"}
}

# 경로 정의 (순서대로 연결)
# New York -> London -> Tokyo -> Sydney, 그리고 Shanghai -> New York (별도 라인)
route_paths = [
    ["New York", "London", "Tokyo", "Sydney"], # Main Route
    ["Shanghai", "New York"]                   # Supply Route
]

# 데이터프레임 변환 (마커용)
df_hubs = pd.DataFrame.from_dict(hubs, orient='index').reset_index()
df_hubs.rename(columns={'index': 'City'}, inplace=True)

fig = go.Figure()

# ==========================================
# 2. Layer 1: 물류 이동 경로 (Routes)
# ==========================================
# 경로가 여러 개이므로 반복문으로 각각 그립니다.
for path in route_paths:
    lats = [hubs[city]["lat"] for city in path]
    lons = [hubs[city]["lon"] for city in path]
    
    fig.add_trace(go.Scattermapbox(
        mode="lines",
        lon=lons, lat=lats,
        line=dict(width=2, color="#00ffff"), # Cyan 색상 (형광 느낌)
        opacity=0.6,
        hoverinfo="none", # 선에는 툴팁 안 뜨게
        name="Route"
    ))

# ==========================================
# 3. Layer 2: 허브 마커 (Hubs - Size by Volume)
# ==========================================
fig.add_trace(go.Scattermapbox(
    mode="markers",
    lon=df_hubs["lon"], lat=df_hubs["lat"],
    text=df_hubs["City"] + "<br>Vol: " + df_hubs["vol"].astype(str),
    marker=dict(
        size=df_hubs["vol"] / 25, # 크기 조절 (너무 크지 않게 나눔)
        color=df_hubs["vol"],     # 재고량에 따라 색상 변화
        colorscale="YlOrRd",      # Yellow -> Red (경고색 느낌)
        opacity=0.9,
        showscale=True,           # 우측 컬러바 표시
        sizemode='diameter'
    ),
    name="Inventory Hub"
))

# ==========================================
# 4. Layer 3: 텍스트 라벨 (Text Labels)
# ==========================================
# 마커 위에 글씨가 겹치지 않게 text trace를 따로 추가
fig.add_trace(go.Scattermapbox(
    mode="text",
    lon=df_hubs["lon"], lat=df_hubs["lat"],
    text=df_hubs["code"], # 공항 코드 표시 (JFK, LHR...)
    textposition="top center",
    textfont=dict(size=14, color="white", weight="bold"),
    hoverinfo="skip",
    name="Labels"
))

# ==========================================
# 5. 스타일링: 3D 관제센터 뷰 (Command Center View)
# ==========================================
fig.update_layout(
    title="<b>🌍 GLOBAL SUPPLY CHAIN COMMAND CENTER</b>",
    title_font_color="white",
    
    # 지도 스타일 설정
    mapbox=dict(
        style="carto-darkmatter", # [무료] 어두운 테마
        center=dict(lat=20, lon=10), # 대략적인 세계 중심
        zoom=1.2, # 전 세계가 보이도록
        pitch=40, # [핵심] 지도를 40도 기울임 (3D 효과)
        bearing=0 # 회전 없음
    ),
    
    # 전체 배경 및 여백
    paper_bgcolor="black",
    margin=dict(l=0, r=0, t=50, b=0),
    height=800,
    showlegend=False # 범례 숨김 (깔끔하게)
)

fig.show()