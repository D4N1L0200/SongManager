import streamlit as st
import pandas as pd
from view import View
from datetime import datetime
import time

class MyPlaylistsUI:
    @staticmethod
    def main():
        st.header("My playlists")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["See my playlists", "Add a music to a playlist", "Create playlist", "Update playlist", "Delete playlist"])
        with tab1: MyPlaylistsUI.see_my_playlists()
        with tab2: MyPlaylistsUI.add_music_to_playlist()
        with tab3: MyPlaylistsUI.create_playlist()
        with tab4: MyPlaylistsUI.update_playlist()
        with tab5: MyPlaylistsUI.delete_playlist()
    @staticmethod
    def see_my_playlists():
        pass
    @staticmethod
    def add_music_to_playlist():
        pass
    @staticmethod
    def create_playlist():
        name = st.text_input("Insert the playlist's name")
        description = st.text_input("Insert the playlist's description")
        if st.button("Create playlist"):
            if not name or not description:
                st.error("Please fill all the fields")
                return
            View.playlists_insert(0, st.session_state["user_id"], name, description, datetime.now())
            st.success("Playlist inserted with sucess")
            time.sleep(2)
            st.rerun()
    @staticmethod
    def update_playlist():
        playlists = View.get_owned_playlists(st.session_state["user_id"])

        if playlists:
            df = pd.DataFrame([{"id": playlist.id, "name": playlist.name, "description": playlist.description} for playlist in playlists])
            st.dataframe(df)

            playlist_to_update = st.selectbox("Select a playlist to update", [playlist for playlist in playlists])
            if playlist_to_update:
                name = st.text_input("Insert the playlist's new name", value = playlist_to_update.name)
                description = st.text_input("Insert the playlist's new description", value = playlist_to_update.description)

                if st.button("Update playlist"):
                    if name != playlist_to_update.name or description != playlist_to_update.description:
                        View.playlists_update(playlist_to_update.id, playlist_to_update.id_user, name, description, playlist_to_update.creation_date)
                        st.success("Playlist updated with sucess")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error("Make sure to change at least one field with a valid new value")
    @staticmethod
    def delete_playlist():
        playlists = View.get_owned_playlists(st.session_state["user_id"])

        if playlists:
            df = pd.DataFrame([{"id": playlist.id, "name": playlist.name, "description": playlist.description} for playlist in playlists])
            st.dataframe(df)

            playlist_to_delete = st.selectbox("Select a playlist to delete", [playlist for playlist in playlists])
            playlist_id = playlist_to_delete.id
            if st.button("Delete playlist"):
                if not playlist_id:
                    st.error("Please fill all the fields")
                    return
                if playlist_id not in df["id"].values:
                    st.error("Invalid playlist ID")
                    return
                
                View.playlists_delete(playlist_id)
                st.success("Playlist deleted successfully")
                time.sleep(2)
                st.rerun()