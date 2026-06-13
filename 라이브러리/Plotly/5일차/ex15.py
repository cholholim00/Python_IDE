# 기간 선택기 장착
import plotly.express as px

df = px.data.stocks() # 2년치 주가 데이터

fig = px.line(df, x='date', y='GOOG', title="Google Stock Price")

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"), # 최근 1달
            dict(count=6, label="6m", step="month", stepmode="backward"), # 최근 6달
            dict(count=1, label="YTD", step="year", stepmode="todate"),   # 올해 1월 1일부터(Year To Date)
            dict(count=1, label="1y", step="year", stepmode="backward"),  # 최근 1년
            dict(step="all") # 전체 보기
        ])
    )
)

fig.show()