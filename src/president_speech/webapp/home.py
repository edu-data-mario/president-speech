import streamlit as st
from president_speech.db.parquet_interpreter import read_parquet

markdown = '''
### president-speech ON-LINE
```
┌─┐┬─┐┌─┐┌─┐┬┌┬┐┌─┐┌┐┌┌┬┐
├─┘├┬┘├┤ └─┐│ ││├┤ │││ │ 
┴  ┴└─└─┘└─┘┴─┴┘└─┘┘└┘ ┴ 
┌─┐┌─┐┌─┐┌─┐┌─┐┬ ┬       
└─┐├─┘├┤ ├┤ │  ├─┤       
└─┘┴  └─┘└─┘└─┘┴ ┴       
┌─┐┌┐┌┬  ┬┌┐┌┌─┐         
│ │││││  ││││├┤          
└─┘┘└┘┴─┘┴┘└┘└─┘
```
```bash
pip install president-speech==0.7.5
```
'''

st.markdown(markdown)

# bar chart
df = read_parquet(use_columns=["president"])
grouped = df.groupby("president")
result_df = grouped.size().reset_index(name="speeches")
st.bar_chart(
    result_df,
    x='president',
    y='speeches',
    height=200,
)

# line chart
df = read_parquet(use_columns=["date"])
df = df.dropna(how="any")

# 날짜 형식 변환
df["year"] = df["date"].str[:4]

# 날짜 형식에 맞지 않는 데이터 제외
df = df[df["year"].str[:4] != ""]

# 연도별 집계
speeches_by_year_df = df["year"].value_counts().reset_index(name="speeches").sort_values("year")

# 출력
st.line_chart(
    speeches_by_year_df,
    x='year',
    y='speeches',
)
