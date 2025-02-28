import os
import streamlit as st
import pandas as pd
from view import View
import time


class GlobalSongsUI:
    @staticmethod
    def main():
        st.header("Manage Global Songs")
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "See all global songs",
                "Add global song",
                "Update global song",
                "Delete global song",
            ]
        )
        with tab1:
            GlobalSongsUI.see_all_global_songs()
        with tab2:
            GlobalSongsUI.add_global_songs()
        with tab3:
            GlobalSongsUI.update_global_songs()
        with tab4:
            GlobalSongsUI.delete_global_songs()

    @staticmethod
    def see_all_global_songs():
        global_songs = View.get_all_global_songs()

        if global_songs:
            df = pd.DataFrame(
                [
                    {"title": song.title, "artist": song.artist, "genre": song.genre}
                    for song in global_songs
                ]
            )
            st.dataframe(df)

            for song in global_songs:
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
        else:
            st.write("There are no global songs yet")

    @staticmethod
    def add_global_songs():
        title = st.text_input("Insert the song's title:")
        artist = st.text_input("Insert the song's artist:")
        genre = st.text_input("Insert the song's genre:")
        file = st.file_uploader(
            "Insert a MP3 or a WAV file:",
            type=["mp3", "wav"],
            key="add_song_file_uploader",
        )
        if st.button("Add song"):
            if title and artist and genre and file:
                View.songs_insert(1, title, artist, genre, file.name, 0, file)
                st.success("Song inserted with success")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Please fill all the fields")

    @staticmethod
    def update_global_songs():
        global_songs = View.get_all_global_songs()

        if global_songs:
            df = pd.DataFrame(
                [
                    {"title": song.title, "artist": song.artist, "genre": song.genre}
                    for song in global_songs
                ]
            )
            st.dataframe(df)

            song_to_update = st.selectbox(
                "Select a song to update", [song for song in global_songs]
            )
            if song_to_update:
                title = st.text_input(
                    "Insert the song's new title:", value=song_to_update.title
                )
                artist = st.text_input(
                    "Insert the song's new artist:", value=song_to_update.artist
                )
                genre = st.text_input(
                    "Insert the song's new genre:", value=song_to_update.genre
                )
                file = st.file_uploader(
                    "Insert a MP3 or a WAV file:",
                    type=["mp3", "wav"],
                    key=f"update_song_{song_to_update.title}_file_uploader",
                )
                if st.button("Update song"):
                    if (
                        title != song_to_update.title
                        or artist != song_to_update.artist
                        or genre != song_to_update.genre
                        or file is not None
                    ):
                        file_name = file.name if file else song_to_update.file

                        View.songs_update(
                            song_to_update.id,
                            song_to_update.id_library,
                            title,
                            artist,
                            genre,
                            file_name,
                            song_to_update.count,
                        )
                        st.success("Song updated with success")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error(
                            "Make sure to change at least one field with a valid new value"
                        )

    @staticmethod
    def delete_global_songs():
        global_songs = View.get_all_global_songs()

        if global_songs:
            df = pd.DataFrame(
                [
                    {"title": song.title, "artist": song.artist, "genre": song.genre}
                    for song in global_songs
                ]
            )
            st.dataframe(df)

            song_to_delete = st.selectbox(
                "Select a song to delete", [song for song in global_songs]
            )
            if song_to_delete:
                if st.button("Delete song"):
                    View.songs_delete(song_to_delete.id)
                    st.success("Song deleted with sucess")
                    time.sleep(2)
                    st.rerun()
