import streamlit as st
from st_pages import add_page_title

add_page_title()

def page1():
    st.write("これはページ1です。")
    st.write("ここにページ1の内容を追加します。")

if __name__ == "__main__":
    page1()