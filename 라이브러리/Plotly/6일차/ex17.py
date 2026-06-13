# 캐나다 몬트리올 선거구별 득표율
import plotly.express as px

# 1. GeoJSON 로드 (Plotly 내장 데이터)
election = px.data.election()
geojson = px.data.election_geojson()

# 2. 데이터 확인
# election DataFrame의 'district' 컬럼과 geojson의 'feature.id'가 매칭됨.
print(election.head(3))

# 3. Choropleth Mapbox 그리기
fig = px.choropleth_mapbox(
    election,
    geojson=geojson,
    locations="district",    # DataFrame에서 매칭할 컬럼명
    featureidkey="properties.district", # GeoJSON에서 매칭할 키 (경로)
    color="Bergeron",        # 색상으로 표현할 수치 (득표수)
    color_continuous_scale="Viridis",
    range_color=(0, 6500),
    mapbox_style="carto-positron", # [무료] 밝은 지도 스타일
    zoom=9,
    center={"lat": 45.5517, "lon": -73.7073}, # 몬트리올 중심 좌표
    opacity=0.5,             # 투명도 (지도가 비쳐 보이게)
    labels={'Bergeron':'Votes'}
)

fig.update_layout(title="Montreal Election Result (Choropleth)")
fig.show()