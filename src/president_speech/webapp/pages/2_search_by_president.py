import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi

st.set_page_config(
    page_title="P.S.O",
    page_icon="seat",
    layout="wide",
)

df = pd.DataFrame()

# 검색어 입력받기
search_word = st.text_input("Please enter the President's name.")


# 검색어를 포함하는 행을 추출
if search_word:
    df = pi.search_by("president", search_word)
# 결과 출력
if df.empty:
    st.write("No search results found.")
else:
    # line chart
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
        height=200,
    )

    # table
    st.dataframe(
        df,
        hide_index=True,
        column_config={
            "url": st.column_config.LinkColumn("see the original text"),
            "division_number": st.column_config.TextColumn("id"),
        }
    )


