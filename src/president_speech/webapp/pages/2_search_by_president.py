import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi


df = pd.DataFrame()


def get_df(word: str, columns: list) -> pd.DataFrame:
    df_1 = pi.read_parquet(use_columns=columns)
    df_r = df_1[df_1["president"].str.contains(word)]
    return df_r


# 검색어 입력받기
search_word = st.text_input("Please enter the President's name.")


# 검색어를 포함하는 행을 추출
if search_word:
    # DataFrame 생성
    df = get_df(search_word, ["date", "title", "president"])
    df = df[df["president"].str.contains(search_word)]

# 결과 출력
if df.empty:
    st.write("No search results found.")
else:
    st.table(df)
