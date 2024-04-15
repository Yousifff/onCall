import streamlit as st



def create_tabel():
    #st.title("Tabel")
    st.table(st.session_state['database'])