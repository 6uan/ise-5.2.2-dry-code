import streamlit as st

COMPANY_ADDRESS = """
Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
"""

LINKS_MD = """
[Google](https://google.com)

[Gemini](https://gemini.google.com)

[Streamlit Docs](https://docs.streamlit.io/)
"""

COPYRIGHT = "This site is copyright Fake Company LLC Inc., 2024"


def init_session_state():
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


def render_sidebar():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)
    st.sidebar.write(COPYRIGHT)


def render_footer():
    with st.expander("Company Info"):
        st.write(COMPANY_ADDRESS)
    with st.expander("Links"):
        st.markdown(LINKS_MD)