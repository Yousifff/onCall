import streamlit as st
import datetime
import requests

def create_form():

    with st.form("Schedule_Form"):
        today = datetime.date.today()
        jan_1 = datetime.date(today.year, 1, 1)
        dec_31 = datetime.date(today.year, 12, 31)
        
        name = st.text_input("Name", placeholder='Name')
        start_date = st.date_input("Start Date", jan_1, jan_1, dec_31)
        end_date = st.date_input("End Date", dec_31, jan_1, dec_31)

        user_url = "http://127.0.0.1:8000/user"
        weekly_url = "http://127.0.0.1:8000/weekly"  # Corrected endpoint URL

        submit = st.form_submit_button("Save")

        if submit:
            start = start_date.strftime("%Y-%m-%d")
            end = end_date.strftime("%Y-%m-%d")

            user_data = {'name': name,'start_date': start, 'end_date': end}
            #weekly_data = {'start_date': start, 'end_date': end}

            # Send user data
            user_response = requests.post(user_url, json=user_data)
            if user_response.status_code == 200:
                st.success("User data saved successfully!")
            else:
                st.error("Failed to save user data.")

            # Send weekly data to the corrected endpoint URL
            #weekly_response = requests.post(weekly_url, json=weekly_data)
            #if weekly_response.status_code == 200:
            #    st.success("Weekly data saved successfully!")
            #else:
            #    st.error("Failed to save weekly data.")



if __name__ == '__main__':
    create_form()

    

