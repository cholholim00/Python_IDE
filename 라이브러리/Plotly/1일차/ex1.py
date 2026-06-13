# 딕셔너리 구조 직접 조작하기
import plotly.graph_objects as go
import plotly.io as pio

# 빈 캔버스 생성
fig = go.Figure()

# 1. Data 추가 (Trace)
# Express를 쓰지 않고 순수 객체로 정의
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    mode='markers+lines',
    name='Team A',
    marker=dict(size=15, color='rgba(255, 0, 0, 0.6)', line=dict(width=2, color='DarkSlateGrey'))
)

fig.add_trace(trace1)

# 2. Layout 심층 제어 (매직 언더바 사용)
fig.update_layout(
    title_text="<b>공부하기 Plotly 1일차</b>",
    title_font_size=24,
    title_x=0.5, # 제목 중앙 정렬
    
    # xaxis 딕셔너리 내부의 title 딕셔너리 내부의 text에 접근
    xaxis_title_text="Time Series", 
    xaxis_showgrid=True,
    xaxis_gridwidth=1,
    xaxis_gridcolor='LightPink',
    
    # 배경 제어
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    
    # 마진(여백) 정밀 제어 (픽셀 단위)
    margin=dict(l=50, r=50, t=80, b=50)
)

# JSON 구조 확인 (이 구조가 눈에 익어야 함)
print(fig.to_dict()['layout']['xaxis']) 

fig.show()
