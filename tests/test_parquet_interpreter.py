import president_speech.db.parquet_interpreter as pi
import pandas as pd


def test_print_parquet_full_path():
    assert pi.get_parquet_full_path().endswith(".parquet")


def test_president_word_frequency():
    df = pi.president_word_frequency(word='반공')
    assert isinstance(df, pd.DataFrame)


def test_plot_president_word_frequency():
    pi.plot_president_word_frequency(word='미신')


def test_table_president_word_frequency():
    pi.table_president_word_frequency(word='5.18')
