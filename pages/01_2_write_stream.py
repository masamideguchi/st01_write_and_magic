import streamlit as st
from utils import show_code

def ex1():
    import time
    import numpy as np
    import pandas as pd
    import streamlit as st

    _LOREM_IPSUM = """
    ジェネレーター、 反復可能 または ストリーム のような
    シーケンスを アプリに ストリーミング します。

    st.write_stream は、 指定された シーケンスを 反復処理し、
    すべての チャンクを アプリに 書き込みます。
    文字列 チャンクは タイプライター効果を 使用して 書き込まれます。
    他の データ型は st.write を使用して 書き込まれます。

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """


    def stream_data():
        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(1)

        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )


        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(1)

    st.write("streamlit 1.31.0以上")
    if st.button("Stream data"):
        st.write_stream(stream_data)


ex1()

st.divider()
show_code(ex1)
