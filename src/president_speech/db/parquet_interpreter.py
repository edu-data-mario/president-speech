import os
import pandas as pd
import termplotlib as tpl
from tabulate import tabulate

PARQUET_PATH = os.path.join(os.path.dirname(__file__), "parquet", "president_speech_ko.parquet")


def print_parquet_full_path():
    print(PARQUET_PATH)


def read_parquet() -> pd.DataFrame:
    df = pd.read_parquet(PARQUET_PATH)
    return df


def president_word_frequency(word: str) -> pd.DataFrame:
    df = read_parquet()
    df['count_word'] = df['speech_text'].str.findall(word).str.len()
    df = df.groupby('president')['count_word'].sum().sort_values(ascending=False).to_frame().reset_index()
    return df


def plot_president_word_frequency(word: str):
    df = president_word_frequency(word)
    fig = tpl.figure()
    fig.barh(df['count_word'], df['president'], force_ascii=True)
    fig.show()


def table_president_word_frequency(word: str):
    df = president_word_frequency(word)
    print(tabulate(df, headers=['president', 'mention'], tablefmt='pipe'))








