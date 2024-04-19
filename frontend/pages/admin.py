import streamlit as st
import datetime
import requests
def create_form():

    with st.form("Schdule_Form"):
        today = datetime.date.today()
        jan_1 = datetime.date(today.year,1,1)
        dec_31 = datetime.date(today.year,12,31)
        name = st.text_input("Name",placeholder='Name')
        schdule_date = st.date_input("date",(jan_1,dec_31))
        url = "http://127.0.0.1:8000/user"
        submit = st.form_submit_button("Save")
        if submit:
            st.write(name.strip())
            data = {'name': name}
            requests.post(url,json=data)




<<<<<<< Updated upstream
if __name__ == '__main__':
    create_form()
    
=======

if __name__ == '__main__':
    create_form()
    
>>>>>>> Stashed changes
