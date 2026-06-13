# 저장의 기술
import plotly.express as px

# 데이터 로드
df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, x="gdpPercap", y="life_exp", color="continent", 
                 title="Global Development 2007")

# 1. [Bad] 그냥 저장 (약 3MB)
fig.write_html("heavy_chart.html")

# 2. [Good] CDN 사용 저장 (약 50KB - 전송용 추천)
fig.write_html("light_chart.html", include_plotlyjs='cdn')

# 3. [Static] 고해상도 PNG 저장 (Scale 3 = 3배 확대, 깨짐 방지)
# fig.write_image("chart_hq.png", scale=3) 

print("저장 완료. 파일 크기를 비교해 보세요.")