import streamlit as st
import requests


def create_tabel():
    #st.title("Tabel")
    url = 'http://127.0.0.1:8000'
    resp = requests.get(url)
    st.write(resp.json())


if __name__ == '__main__':
    create_tabel()
    