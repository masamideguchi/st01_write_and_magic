import streamlit as st
import pandas as pd
from utils import show_code


def ex1():

    st.write('Hello, *World* :sunglasses:')


def ex2():
    st.write(1234)
    data_frame = pd.DataFrame({
        '1カラム目': [1, 2, 3, 4],
        '2カラム目': [50, 30, 20, 40],
    })
    st.write(data_frame)


def ex3():
    st.write('1 + 1 = ', 2)

    data_frame = pd.DataFrame({
        '1カラム目': [1, 2, 3, 4],
        '2カラム目': [50, 30, 20, 40],
    })
    st.write('Below is a DataFrame:', data_frame, 'Abobe is a DataFrame')
    st.divider()


def ex4():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import altair as alt

    df = pd.DataFrame(
        np.random.randn(200,3),
        columns=['a', 'b', 'c']
    )

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c',tooltip=['a', 'b', 'c']
    )
    st.write(c)


st.write('引数が文字列の場合は、Markdown形式のテキストを出力')
ex1()
show_code(ex1)
st.divider()
st.write('数値、データフレームなども出力可能')
ex2()
show_code(ex2)
st.divider()
st.write('文字列とデータフレームなどの複数の引数を渡すことも可能')
ex3()
show_code(ex3)
st.divider()
st.write('XXXX')
ex4()
show_code(ex4)

