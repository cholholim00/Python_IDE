# 이동 경로와 밀도
import plotly.graph_objects as go

fig = go.Figure()

# 1. 이동 경로 (Lines) - 서울 -> 부산 -> 도쿄
lons = [126.97, 129.07, 139.69]
lats = [37.56, 35.17, 35.68]

fig.add_trace(go.Scattermapbox(
    mode="markers+lines", # 점과 선을 같이 그림
    lon=lons, lat=lats,
    marker={'size': 10, 'color': 'orange'},
    line={'width': 3, 'color': 'cyan'},
    name="Logistics Route"
))

# 2. 밀도 히트맵 (Density) - 서울 주변에 데이터가 많다고 가정
fig.add_trace(go.Densitymapbox(
    lat=[37.56, 37.50, 37.40, 35.17],
    lon=[126.97, 127.00, 126.90, 129.07],
    z=[10, 20, 5, 8], # 가중치 (밀도)
    radius=20,        # 히트맵 번짐 반경
    colorscale="Hot",
    name="Traffic Density"
))

fig.update_layout(
    mapbox=dict(
        style="carto-darkmatter",
        center=dict(lat=36.5, lon=132),
        zoom=4
    ),
    title="Route & Density Analysis"
)

fig.show()