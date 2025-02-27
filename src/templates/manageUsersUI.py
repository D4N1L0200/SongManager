import streamlit as st
import pandas as pd
from view import View
import time

class ManageUsersUI:
    @staticmethod
    def main():
        st.header("Manage Users")
        tab1, tab2, tab3 = st.tabs(["See users","Update user", "Delete user"])
        with tab1: ManageUsersUI.see_users()
        with tab2: ManageUsersUI.update_user()
        with tab3: ManageUsersUI.delete_user()
    @staticmethod
    def see_users():
        users = View.users_get()
        df = pd.DataFrame([{"id": user.id, "name": user.name, "admin": user.is_admin} for user in users])
        st.dataframe(df)
    @staticmethod
    def update_user():
        users = View.users_get()
        df = pd.DataFrame([{"id": user.id, "name": user.name, "admin": user.is_admin} for user in users])
        st.dataframe(df)
        user_id = st.number_input("Enter the ID of the user to update", min_value=2)
        new_name = st.text_input("Enter the new name")
        new_password = st.text_input("Enter the new password", type="password")
        if st.button("Update user"):
            if not user_id or not new_name or not new_password:
                st.error("Please fill in all the fields")
                return
            if user_id not in df["id"].values:
                st.error("Invalid user ID")
                return
            if len(new_name) < 2:
                st.error("Invalid name")
                return
            
            View.users_update(user_id, new_name, new_password)
            st.success("User updated successfully")
            time.sleep(2)
            st.rerun()
    @staticmethod
    def delete_user():
        users = View.users_get()
        df = pd.DataFrame([{"id": user.id, "name": user.name, "admin": user.is_admin} for user in users])
        st.dataframe(df)
        user_id = st.number_input("Enter the ID of the user to delete", min_value=2)
        if st.button("Delete user"):
            if not user_id:
                st.error("Please fill in all the fields")
                return
            if user_id not in df["id"].values:
                st.error("Invalid user ID")
                return
            View.users_delete(user_id)
            st.success("User deleted successfully")
            time.sleep(2)
            st.rerun()