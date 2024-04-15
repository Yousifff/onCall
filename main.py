# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

from frontend.admin import create_form
from frontend.index import create_tabel
from st_pages import Page,show_pages

if 'database' not in st.session_state:
    st.session_state['database'] = {}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_form()
    create_tabel()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
