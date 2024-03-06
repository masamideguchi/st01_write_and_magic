import streamlit as st
from utils import show_code

def ex1():
    # イタリック、ボールド、イタリックボールド
    st.markdown("*Streamlit* is **really** ***cool***.")

    # 文字色の指定
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')

    # 絵文字の指定
    st.markdown("Here's a bouquet &mdash;  \
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    # 行末に2個の空白で改行
    # 2個以上の改行文字で改行
    multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
    '''

    st.markdown(multi)

ex1()
st.divider()
show_code(ex1)
