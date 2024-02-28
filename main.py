import streamlit as st


def run():
    st.set_page_config(
        page_title="st.write_and_magic",
        page_icon=":plane:",
    )

    st.write('# st.write and magicコマンド')

    st.sidebar.success("上記サブメニューを選択")

    st.markdown(
        """
        streamlitはあなたのアプリに情報を表示する2つの簡単な方法があり、通常はまずここから始めましょう。
        st.writeとmagicです。
        """
    )


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    run()

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
