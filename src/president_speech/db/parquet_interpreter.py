import os
import pandas as pd
import termplotlib as tpl
from tabulate import tabulate
import dask.dataframe as dd

parquet_tmp_dir = os.path.join(os.path.dirname(__file__), "parquet_tmp")
parquet_path = os.path.join(os.path.dirname(__file__), "parquet", "president_speech_ko.parquet")


def get_parquet_tmp_dir() -> str:
    """Here's the full path of the built-in parquet"""
    return parquet_tmp_dir


def get_parquet_full_path() -> str:
    """Here's the full path of the built-in parquet"""
    return parquet_path


def set_parquet_full_path(full_path: str) -> str:
    parquet_path = full_path
    return parquet_path


def print_parquet_full_path():
    print(get_parquet_full_path())


def read_parquet(use_columns=['division_number', 'president', 'title', 'date', 'location', 'kind', 'speech_text']) -> pd.DataFrame:
    """
    Read the parquet file of the president's speech history
    - For efficient memory use, you can specify columns to read.
    :param use_columns: ['division_number', 'president', 'title', 'date', 'location', 'kind', 'speech_text']
    :return: pd.DataFrame
    """
    # df = pd.read_parquet(parquet_path, columns=use_columns)
    ddf = dd.read_parquet(parquet_path, columns=use_columns, memory_limit=100)
    # df = ddf.compute()
    return ddf


def president_word_frequency(word: str) -> pd.DataFrame:
    """return -> [president, count_word]"""
    df = read_parquet(use_columns=['speech_text', 'president'])
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


def search_by(column_name: str, word: str, use_columns=["date", "title", "president", "division_number"]) -> pd.DataFrame:
    """Search if words are included - contains"""
    df = read_parquet(use_columns)

    df = df[df[column_name].str.contains(word)]
    # df = df.set_index(["division_number"])
    pa_go_kr = "https://www.pa.go.kr/research/contents/speech/index.jsp?spMode=view&catid=c_pa02062&artid="
    df["url"] = df["division_number"].apply(lambda x: f"{pa_go_kr}{x}")
    df = df.sort_values("date")
    return df.compute()

    







