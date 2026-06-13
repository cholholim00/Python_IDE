# 코드 구조 이해를 돕기 위한 예시입니다.
# app.py 구조 예시
import streamlit as st
import plotly.express as px

st.title("My First Plotly App")

# 1. Streamlit 위젯으로 입력 받기
continent = st.sidebar.selectbox("대륙 선택", ["Asia", "Europe", "Americas"])

# 2. 입력값에 따라 데이터 필터링
df = px.data.gapminder().query(f"continent == '{continent}'")

# 3. 그래프 그리기
fig = px.line(df, x="year", y="life_exp", color="country")

# 4. 웹에 띄우기 (반응형 옵션 필수)
st.plotly_chart(fig, use_container_width=True)