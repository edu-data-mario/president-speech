# president-speech
- Presidents of the Republic of Korea Speeches
- Parquet, provided in the form of sqlite db file
- Comes with simple cli

### SUMMARY OF PROVIDED DATA
- data per case can be checked in the following ways
- https://www.pa.go.kr/research/contents/speech/index.jsp?spMode=view&catid=c_pa02062&artid={division_number}
- some data show date values as empty columns or years only
  ![image](https://github.com/edu-data-mario/president-speech/assets/134017660/7efd02c4-0674-483f-bb27-458a04efe3d0)

    | president | size | min(date)  | max(date)  |
    |:----------|:-----|:-----------|:-----------|
    | 이승만       | 998  | 1948.07.24 | 1959.03.10 |
    | 윤보선       | 3    | 1960.08.13 | 1960.09.15 |
    | 박정희       | 1270 | 1963.12.17 | 1979.10.26 |
    | 최규하       | 58   | 1979.10.27 | 1980.08.16 |
    | 전두환       | 602  | 1980.06.05 | 1987.02.16 |
    | 노태우       | 601  | 1988.02.25 | 1992.10.05 |
    | 김영삼       | 728  | 1993.01.09 | 1998.01.23 |
    | 김대중       | 822  | 1998.02.25 | 2003.02.17 |
    | 노무현       | 780  | 2003.02.25 | 2008.01.28 |
    | 이명박       | 1027 | 2008.02.25 | 2013.02.07 |
    | 박근혜       | 493  | 2013.02.24 | 2016.10.26 |
    | 문재인       | 1389 | 2017.05.10 | 2022.03.30 |

    ```python
    >>> df.info()
    
    <class 'pandas.core.frame.DataFrame'>
    Index: 8771 entries, 5368 to 102591
    Data columns (total 7 columns):
     #   Column           Non-Null Count  Dtype 
    ---  ------           --------------  ----- 
     0   division_number  8771 non-null   int64 
     1   president        8771 non-null   object
     2   title            8771 non-null   object
     3   date             8771 non-null   object
     4   location         8771 non-null   object
     5   kind             8771 non-null   object
     6   speech_text      8771 non-null   object
    dtypes: int64(1), object(6)
    memory usage: 548.2+ KB
    ```
### Use
```bash
$ pip install president-speech
```
```python
>>> from president_speech.db.parquet_interpreter import read_parquet, get_parquet_full_path
>>> get_parquet_full_path()
'/Users/f16/code/edu/president-speech/.venv/lib/python3.8/site-packages/president_speech/db/parquet/president_speech_ko.parquet'
>>> read_parquet().head(3)
      division_number president                title        date location kind                                        speech_text
5368          1305368       박정희  제5대 대통령 취임식 대통령 취임사  1963.12.17       국내  취임사  \n\n\n단군성조가 천혜의 이 강토 위에 국기를 닦으신지 반만년, 연면히 이어온 ...
5369          1305369       박정희            국회 개회식 치사  1963.12.17       국내  기념사   존경하는 국회의장, 의원제위 그리고 내외귀빈 여러분! 오늘 이 뜻깊은 제3공화국의...
5370          1305370       박정희               신년 메시지  1964.01.01       국내  신년사   친애하는 국내외의 동포 여러분! 혁명의 고된 시련을 겪고 민정이양으로 매듭을 지은...
>>> 

```
### Use Cli
```bash
$ ps-wordcount -h     
usage: ps-word-count [-h] [-t | -p] word

Word frequency output from previous presidential speeches

positional arguments:
  word         Search word

optional arguments:
  -h, --help   show this help message and exit
  -t, --table  Table Format Output
  -p, --plot   Format Output

$ ps-word-count -p 독립
문재인  [954]  ****************************************
이승만  [430]  ******************
박정희  [361]  ****************
이명박  [176]  ********
김대중  [171]  ********
전두환  [169]  ********
노무현  [167]  *******
노태우  [131]  ******
김영삼  [114]  *****
박근혜  [ 71]  ***
최규하  [  4]  *
윤보선  [  0]
```

```bash
$ ps-word-count -t 독립
|    | president   |   mention |
|---:|:------------|----------:|
|  0 | 문재인      |       954 |
|  1 | 이승만      |       430 |
|  2 | 박정희      |       361 |
|  3 | 이명박      |       176 |
|  4 | 김대중      |       171 |
|  5 | 전두환      |       169 |
|  6 | 노무현      |       167 |
|  7 | 노태우      |       131 |
|  8 | 김영삼      |       114 |
|  9 | 박근혜      |        71 |
| 10 | 최규하      |         4 |
| 11 | 윤보선      |         0 |

```

### Ref
- [대통령기록관 연설기록](https://www.pa.go.kr/research/contents/speech/index.jsp)
- [대통령기록관_행정안전부 대통령기록관_대통령연설기록 연설문 API](https://www.data.go.kr/data/15084167/fileData.do#tab-layer-openapi)
- https://stackoverflow.com/questions/45470964/python-extracting-text-from-webpage-pdf
- https://pypdf.readthedocs.io/en/latest/user/extract-text.html
- https://setuptools.pypa.io/en/latest/userguide/datafiles.html
- https://frhyme.github.io/python-basic/py_no_break_space/
- [x] https://pypi.org/project/pandas-downcast/
- [x] https://realpython.com/python-project-documentation-with-mkdocs/
- https://publivate.tistory.com/245 modin, dask, vaex => pandas
- [x] https://www.fileformat.info/info/emoji/list.htm
- https://discuss.streamlit.io/t/version-1-26-0/50056
- [x] https://github.com/ai-yash/st-chat
- https://konlpy.org/ko/latest/index.html
- https://liveyourit.tistory.com/57
- https://dongdongfather.tistory.com/70
- https://docs.python.org/3/library/collections.html#collections.Counter

### Development environment setting
```bash
$ git clone ...
$ cd president-speech
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
```

```bash
$ pdm add -dG test pytest pytest-cov
$ pdm test
$ pdm ptest

$ pdm ctest
---------- coverage: platform darwin, python 3.9.18-final-0 ----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
src/president_speech/__init__.py                     0      0   100%
src/president_speech/db/__init__.py                  0      0   100%
src/president_speech/db/connection_manager.py       17      3    82%
src/president_speech/db/parquet_interpreter.py      25      1    96%
src/president_speech/db/search.py                   15      1    93%
tests/__init__.py                                    0      0   100%
tests/test_parquet_interpreter.py                   11      0   100%
tests/test_search.py                                 5      0   100%
--------------------------------------------------------------------
TOTAL                                               73      5    93%
```

### Deploy to fly.io with Docker Technology
```bash
$ docker build -t president-speech-webapp .
$ docker run -it --rm -p 7942:8051 president-speech-webapp

$ fly deploy
Visit your newly deployed app at https://president-speech.fly.dev/
```
![image](https://github.com/edu-data-mario/president-speech/assets/134017660/e108efcf-54ef-41c3-a9da-94d2ab5d1c21)

# Give it a try. And opinions are always welcome. Of course, it's PR.
- https://president-speech.fly.dev/