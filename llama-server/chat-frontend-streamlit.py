import streamlit as st
import requests as r

URL = 'http://127.0.0.1:6800'

health = r.get (f"{URL}/health").content.decode ('ascii')

st.write (health)

if (health != "OK"):
    r.get (f"{URL}/generate")

health = r.get (f"{URL}/health").content.decode ('ascii')



if (health == "OK"):
    prompt = st.text_input ("Prompt", "Are you up?")
    if (st.button ("Send")):
        st.write (r.post (f"{URL}/chat", data=prompt).content.decode ('ascii'))

    max_seq_len = st.write ("Max Sequence length", 8192)
    max_gen_len = st.write ("Max Generated length", None)
    temperature = st.write ("Temperature", 0.6)