import streamlit as st
from streamlit_chat import message

st.title("president speech bot")

msg = st.text_input('LIVING FOR TODAY')
message(msg, is_user=True)
message("본인은 ...") 