
# app.py
import streamlit as st
from st_pages import Page, show_pages, add_page_title

# ページの設定
show_pages(
    [
        Page("app.py", "Home", "🏠"),
#        Page("pages/page1.py", "Page 1", ":xxxx:")
    ]
)

# タイトルの追加
add_page_title()

# メインページの内容
def main():
    st.write("これはメインページです。")
    st.write("左のサイドバーから他のページに移動できます。")

if __name__ == "__main__":
    main()

