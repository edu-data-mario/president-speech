from president_speech.db.search import title, speech
from president_speech.db.parquet_interpreter import plot_president_word_frequency, table_president_word_frequency
import argparse


def search():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--title", action="store_true", help="Search speech title like")
    group.add_argument("-s", "--speech", action="store_true", help="Search speech title speech")
    parser.add_argument("keyword", type=str, help="Search word")

    args = parser.parse_args()

    if args.title:
        title(args.keyword)

    elif args.speech:
        speech(args.keyword)
    else:
        print("An undefined functional call has occurred.")


def word_count():
    parser = argparse.ArgumentParser(description="Word frequency output from previous presidential speeches")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--table", action="store_true", help="Table Format Output")
    group.add_argument("-p", "--plot", action="store_true", help="Format Output")
    parser.add_argument("word", type=str, help="Search word")

    args = parser.parse_args()

    if args.table:
        table_president_word_frequency(args.word)

    elif args.plot:
        plot_president_word_frequency(args.word)
    else:
        print("An undefined functional call has occurred.")
