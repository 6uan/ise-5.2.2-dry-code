import streamlit as st
from utils import init_session_state, render_sidebar, render_footer


init_session_state()

st.set_page_config(page_title="About")

st.markdown("# About")

st.sidebar.header("About")
render_sidebar()

st.markdown(
    """
    Fake Company LLC Inc. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

st.image("./assets/fake_company.png")

render_footer()