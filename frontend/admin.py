import streamlit as st
import datetime

def create_form():

    with st.form("Schdule_Form"):
        today = datetime.date.today()
        jan_1 = datetime.date(today.year,1,1)
        dec_31 = datetime.date(today.year,12,31)
        name = st.text_input("Name",placeholder='Name')
        schdule_date = st.date_input("date",(jan_1,dec_31))
        submit = st.form_submit_button("Save")
        if submit:
            st.session_state['database'][name] = schdule_date




