# 전 세계 지진 발생 위치 시각화
import plotly.express as px
import pandas as pd

# 가상 지진 데이터 생성 (위경도 난수)
# 태평양 불의 고리 주변 대략적 좌표
df = pd.DataFrame({
    'Latitude': [-33, 35, 19, 45, -41, 14, 36],
    'Longitude': [-71, 139, -99, 140, 174, 121, -120],
    'Magnitude': [8.5, 9.0, 7.1, 8.2, 7.8, 6.5, 6.0],
    'Location': ['Chile', 'Japan', 'Mexico', 'Hokkaido', 'New Zealand', 'Philippines', 'California']
})

# Scatter Mapbox
fig = px.scatter_mapbox(
    df,
    lat="Latitude", lon="Longitude",
    size="Magnitude",     # 지진 강도에 따라 원 크기 조절
    color="Magnitude",    # 색상도 강도에 따라 (경고색)
    hover_name="Location",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=30,          # 원의 최대 크기 제한
    zoom=1,               # 초기 줌 레벨 (1: 전세계, 10: 도시)
    mapbox_style="carto-darkmatter" # [무료] 다크모드 지도 스타일
)

fig.update_layout(title="Global Earthquake Magnitude Map")
fig.show()