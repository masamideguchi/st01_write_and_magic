import streamlit as st
from utils import show_code


def ex1():
    '''
    # THis is the document title

    This is some _markdown_:
    '''

    import pandas as pd
    df = pd.DataFrame({'col1': [1, 2, 3]})
    df

    x = 10
    'x', x


    import matplotlib.pyplot as plt
    import numpy as np

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    fig



ex1()

st.divider()
show_code(ex1)
