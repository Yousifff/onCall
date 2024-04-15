# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
DEBUG = os.getenv("PRODUCTION", False)

API_URL = "http://localhost:8000" if DEBUG else "https://oncall-api.fly.dev"


import streamlit as st

from frontend.pages.admin import create_form
from frontend.pages.index import create_tabel
from st_pages import Page,show_pages

if 'database' not in st.session_state:
    st.session_state['database'] = {}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_tabel()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
