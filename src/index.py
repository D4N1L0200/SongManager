from templates.loginUI import LoginUI
from templates.registerUI import RegisterAccountUI
from templates.globalSongsUI import GlobalSongsUI
from templates.manageUsersUI import ManageUsersUI
from templates.mySongsUI import MySongsUI
from templates.myPlaylistsUI import MyPlaylistsUI
from view import View

import streamlit as st


class IndexUI:
    @staticmethod
    def guest_menu():
        op = st.sidebar.selectbox("Menu", ["Login", "Register account"])
        if op == "Login":
            LoginUI.main()
        if op == "Register account":
            RegisterAccountUI.main()

    @staticmethod
    def admin_menu():
        op = st.sidebar.selectbox("Menu", ["Global Songs", "Manage Users"])
        if op == "Global Songs":
            GlobalSongsUI.main()
        if op == "Manage Users":
            ManageUsersUI.main()

    @staticmethod
    def user_menu():
        op = st.sidebar.selectbox("Menu", ["My Songs", "My Playlists"])
        if op == "My Songs":
            MySongsUI.main()
        if op == "My Playlists":
            MyPlaylistsUI.main()

    @staticmethod
    def quit():
        if st.sidebar.button("Quit"):
            del st.session_state["user_id"]
            del st.session_state["user_name"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "user_id" not in st.session_state:
            IndexUI.guest_menu()
        else:
            admin = st.session_state["user_name"] == "admin"

            st.sidebar.write("Welcome, " + st.session_state["user_name"] + "!")

            if admin:
                IndexUI.admin_menu()
            else:
                IndexUI.user_menu()

            IndexUI.quit()

    @staticmethod
    def main():
        View.load_all()
        View.user_admin()

        IndexUI.sidebar()


IndexUI.main()
