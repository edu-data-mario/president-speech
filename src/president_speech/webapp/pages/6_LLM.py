import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="P.S.O",
    page_icon="speech_balloon",
    layout="wide",
)

st.title("president speech BOT")

st.session_state.setdefault(
    'past', [
        '본인은 ...',
        ]
)
st.session_state.setdefault(
    'generated', [
        {'type': 'normal', 'data': '두환이니?'}
     ]
)

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append({'type': 'normal', 'data': user_input},)

   
with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
    
chat_placeholder = st.empty()

 
with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True)

        message(
            st.session_state['generated'][i]['data']
        )