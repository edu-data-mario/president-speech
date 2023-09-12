import os
import pandas as pd
import termplotlib as tpl
from tabulate import tabulate
import dask.dataframe as dd
import unicodedata
import urllib.parse
import gc


parquet_tmp_dir = os.path.join(os.path.dirname(__file__), "parquet_tmp")
# parquet_path = os.path.join(os.path.dirname(__file__), "parquet", "president_speech_ko.parquet")
parquet_path = os.path.join(os.path.dirname(__file__), "parquet_tmp", "partition", "df")


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


def read_parquet(use_columns=['division_number', 'president', 'title', 'date', 'location', 'kind', 'speech_text'], partition_key=None) -> pd.DataFrame:
    """
    Read the parquet file of the president's speech history
    - For efficient memory use, you can specify columns to read.
    :param use_columns: ['division_number', 'president', 'title', 'date', 'location', 'kind', 'speech_text']
    :param partition_key:
    :return: pd.DataFrame
    """
    if partition_key:
        ddf = dd.read_parquet(f'{parquet_path}/president={encode_korean(partition_key)}', columns=use_columns, memory_limit=100)
    else:
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


def partition_search_by(column_name: str, word: str,
                        use_columns=["date", "title", "president", "division_number"],
                        presidents=['이승만', '윤보선', '박정희', '최규하', '전두환', '노태우', '김영삼', '김대중', '노무현', '이명박', '박근혜', '문재인']
                        ) -> pd.DataFrame:
    dfs = []
    for p in presidents:
        gc.collect()
        df = read_parquet(use_columns, partition_key=p)

        df = df[df[column_name].str.contains(word)]
        # df = df.set_index(["division_number"])
        pa_go_kr = "https://www.pa.go.kr/research/contents/speech/index.jsp?spMode=view&catid=c_pa02062&artid="
        df["url"] = df["division_number"].apply(lambda x: f"{pa_go_kr}{x}")
        df = df.sort_values("date")
        dfs.append(df.compute())

    return pd.concat(dfs)


def encode_korean(text):
  """한글을 URL 인코딩합니다."""

  # 유니코드로 변환
  unicode_text = unicodedata.normalize("NFC", text)

  # URL 인코딩
  encoded_text = urllib.parse.quote(unicode_text)
  return encoded_text








