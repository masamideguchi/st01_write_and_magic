import streamlit as st
from utils import show_code


def ex1():
    md = st.text_area('Type in your markdown string (without outer quotes)',
                      "Happy Streamlit-ing! :balloon: :balloon: :balloon: :balloon: :balloon:")

    st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

    st.markdown(md)

ex1()
st.divider()
show_code(ex1)