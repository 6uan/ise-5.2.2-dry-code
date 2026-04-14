import streamlit as st
from utils import init_session_state, render_sidebar, render_footer


init_session_state()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit!")

render_sidebar()

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

render_footer()