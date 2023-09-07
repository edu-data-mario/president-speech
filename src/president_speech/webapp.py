import streamlit as st
import pandas as pd
import president_speech.db.parquet_interpreter as pi

df = pi.read_parquet()

df
