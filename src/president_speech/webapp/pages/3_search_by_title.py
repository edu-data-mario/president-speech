import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi


df = pd.DataFrame()

# 검색어 입력받기
search_word = st.text_input("Please enter some or all of the speech titles.")


# 검색어를 포함하는 행을 추출
if search_word:
    df = pi.search_by("title", search_word)
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


