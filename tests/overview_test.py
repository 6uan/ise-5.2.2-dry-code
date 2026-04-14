import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


def test_app_page_markdown():
    at = AppTest.from_file("pages/overview.py").run()

    assert at.markdown[0].body == "# Overview"
    assert at.markdown[1].body.startswith("Here is a page with a site overview.")
    assert at.markdown[2].body.strip() == addr_md.strip()
    assert at.markdown[3].body.strip() == links_md.strip()


def test_app_page_login():
    at = AppTest.from_file("pages/about.py").run()

    at.session_state.logged_in = False

    at.button("login").click().run()

    assert at.session_state.logged_in == True

    at.button("logout").click().run()

    assert at.session_state.logged_in == False
