import streamlit as st
from view import View
from datetime import datetime
import time

class RegisterAccountUI:
    def main():
        st.header("Register account on the system")
        RegisterAccountUI.insert()

    def insert():
        name = st.text_input("Insert your name")
        password = st.text_input("Insert a password", type="password")
        if st.button("Inserir"):
            View.users_insert(name, password, datetime.now(), False)
            st.success("Account registered")
            time.sleep(2)
            st.rerun()