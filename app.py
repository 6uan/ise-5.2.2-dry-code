import streamlit as st

if st.session_state.get("logged_in") == None:
    st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit!")

if st.session_state.logged_in:
    st.sidebar.success("Logged in")
    st.sidebar.button("Log out", key="logout", on_click=logout)
else:
    st.sidebar.warning("Not logged in")
    st.sidebar.button("Log in", key="login", on_click=login)

st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

with st.expander("Company Info"):
    st.write(
        """
        Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
    """
    )

with st.expander("Links"):
    st.markdown(
        """
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
    """
    )
