import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi


df = pd.DataFrame()

# 검색어 입력받기
search_word = st.text_input("Calculates the number of word references by president.")


# 검색어를 포함하는 행을 추출
if search_word:
    df = pi.president_word_frequency(search_word)
# 결과 출력
if df.empty:
    st.write("No search results found.")
else:
    # bar chart
    st.bar_chart(
        df,
        x='president',
        y='count_word',
        height=200,
    )
    st.dataframe(
        df,
        hide_index=True,
        # column_config={
        #     "url": st.column_config.LinkColumn("see the original text"),
        #     "division_number": st.column_config.TextColumn("id"),
        # }
    )


