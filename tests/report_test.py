import pytest

from streamlit.testing.v1 import AppTest

from test_const import addr_md, links_md


@pytest.mark.timeout(10)  # Extra timeout because bar charts are slow
def test_app_page_markdown():
    at = AppTest.from_file("pages/report.py").run()

    assert at.markdown[0].body == "# Report"
    assert at.markdown[1].body.startswith("Here is a page with a report on it.")
    assert at.markdown[2].body.strip() == ("Look at those numbers. Amazing.")
    assert at.markdown[3].body.strip() == addr_md.strip()
    assert at.markdown[4].body.strip() == links_md.strip()


def test_app_page_login():
    at = AppTest.from_file("pages/report.py").run()

    at.session_state.logged_in = False

    at.button("login").click().run()

    assert at.session_state.logged_in == True

    at.button("logout").click().run()

    assert at.session_state.logged_in == False
