import os
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
        # pegar todas as playlists, para cada playlist pegar todos os seus items e pegar as musicas desses items
        # st.subheader("See your playlists")
        playlists = View.get_owned_playlists_minus_liked(st.session_state["user_id"])
        
        if playlists:
            df = pd.DataFrame([{"id": playlist.id, "name": playlist.name, "description": playlist.description} for playlist in playlists])
            st.dataframe(df)

            playlist_to_see = st.selectbox("Select a playlist to see", [playlist for playlist in playlists])
            playlist_id = playlist_to_see.id
            if st.button("See playlist"):
                if not playlist_id:
                    st.error("Please fill all the fields")
                    return
                if playlist_id not in df["id"].values:
                    st.error("Invalid playlist ID")
                    return

                songs = View.get_songs_by_playlist(playlist_id)
                st.subheader(f"Playlist: {playlist_to_see.name}")
                if songs:
                    for song in songs:
                        song_title = song.title
                        song_file_path = song.file

                        st.write(f"{song_title} - {song.artist}")
                        if os.path.isfile(song_file_path):
                            if song_file_path.endswith(".mp3"):
                                st.audio(song_file_path, format="audio/mp3")
                            elif song_file_path.endswith(".wav"):
                                st.audio(song_file_path, format="audio/wav")
                        else:
                            st.write(f"Cannot play {song_title}, file not found.")
        
    @staticmethod
    def add_music_to_playlist():
        # criar um playlistitem relacionado com uma playlist
        # st.subheader("Add some of your liked songs to a playlist")

        id_liked_songs = View.get_liked_songs_id_by_user(st.session_state["user_id"])

        if id_liked_songs:
            songs = View.get_songs_by_playlist(id_liked_songs)
            if songs:
                df = pd.DataFrame([{"title": song.title, "artist": song.artist, "genre": song.genre} for song in songs])
                st.dataframe(df)

                song_to_add = st.selectbox("Select a song to add", [song for song in songs])

                playlist_to_add = st.selectbox("Select a playlist to add", [playlist for playlist in View.get_owned_playlists_minus_liked(st.session_state["user_id"])])

                if st.button("Add song to playlist"):
                    if not song_to_add or not playlist_to_add:
                        st.error("Please fill all the fields")
                        return
                    View.playlistitems_insert(playlist_to_add.id, song_to_add.id, 0)
                    st.success("Song added to playlist with sucess")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def create_playlist():
        # st.subheader("Create a playlist")

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
        # st.subheader("Update your playlists")

        playlists = View.get_owned_playlists_minus_liked(st.session_state["user_id"])

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
        # st.subheader("Delete a playlist")
        playlists = View.get_owned_playlists_minus_liked(st.session_state["user_id"])

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