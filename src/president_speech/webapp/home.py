import streamlit as st
from president_speech.db.parquet_interpreter import read_parquet

markdown = '''
### president-speech ON-LINE
```
┌─┐┬─┐┌─┐┌─┐┬┌┬┐┌─┐┌┐┌┌┬┐
├─┘├┬┘├┤ └─┐│ ││├┤ │││ │ 
┴  ┴└─└─┘└─┘┴─┴┘└─┘┘└┘ ┴ 
┌─┐┌─┐┌─┐┌─┐┌─┐┬ ┬       
└─┐├─┘├┤ ├┤ │  ├─┤       
└─┘┴  └─┘└─┘└─┘┴ ┴       
┌─┐┌┐┌┬  ┬┌┐┌┌─┐         
│ │││││  ││││├┤          
└─┘┘└┘┴─┘┴┘└┘└─┘
```
```bash
pip install president-speech==0.7.0
```
'''

st.markdown(markdown)

df = read_parquet(use_columns=["president"])
grouped = df.groupby("president")
result_df = grouped.size().reset_index(name="speeches")


st.bar_chart(
    result_df,
    x='president',
    y='speeches',
    height=200,
)
