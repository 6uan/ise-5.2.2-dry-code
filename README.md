# [ISE] In-Class Activity 5.2.2 - DRY Code

In this activity, you'll be looking at a multipage Streamlit app with a _bunch_ of redundant code. Your task is to abstract out as much of that redundant code as you can so that the app still works, but changing things (e.g. the company address, or the login method) doesn't have to happen on every page.

## Installation

Create a copy of this repository with the "Use this template" button in the upper right on Github.

Clone your copy to your local workspace. Then:

```bash
cd ise-5.2.2-dry-code # cd into directory
python -m venv venv # initialize venv
source venv/bin/activate # activate venv
pip install -r requirements.txt # install libraries
```

## Running

Run the app with

```bash
streamlit run app.py
```

## Tests

Want to make sure you haven't broken anything? Run the tests with

```bash
pytest tests/
```