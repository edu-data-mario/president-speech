import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi

st.set_page_config(
    page_title="P.S.O",
    page_icon="clipboard",
    layout="wide",
)

df = pd.DataFrame()

# 검색어 입력받기
search_word = st.text_input("I'll find the presidential speech associated with the word you type.")

# 검색어를 포함하는 행을 추출
if search_word:
    df = pi.partition_search_by("speech_text", search_word, use_columns=["date", "title", "president", "division_number", "speech_text"])

# 결과 출력
if df.empty:
    st.write("No search results found.")
else:
    # bar chart
    grouped = df.groupby("president")
    result_df = grouped.size().reset_index(name="speeches")
    st.bar_chart(
        result_df,
        x='president',
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


