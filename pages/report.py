import streamlit as st
from utils import init_session_state, render_sidebar, render_footer


init_session_state()

st.set_page_config(page_title="Report")

st.markdown("# Report")

st.sidebar.header("Report")
render_sidebar()

st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
"""
)

render_footer()