import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Enter the system")
        name = st.text_input("Insert your username")
        password = st.text_input("Insert the password", type="password")
        if st.button("Enter"):
            c = View.user_authenticate(name, password)
            if c == None: st.write("Invalid username or password")
            else:
                st.session_state["user_id"] = c["id"]
                st.session_state["user_name"] = c["name"]
                st.rerun()