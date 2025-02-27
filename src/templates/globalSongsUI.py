import streamlit as st
import pandas as pd
from view import View
import time

class GlobalSongsUI:
    @staticmethod
    def main():
        st.header("Manage Global Songs")
        tab1, tab2, tab3, tab4 = st.tabs(["See all global songs", "Add global song", "Update global song", "Delete global song"])
        with tab1: GlobalSongsUI.see_all_global_songs()
        with tab2: GlobalSongsUI.add_global_songs()
        with tab3: GlobalSongsUI.update_global_songs()
        with tab4: GlobalSongsUI.delete_global_songs()

    @staticmethod
    def see_all_global_songs():
        global_songs = View.get_all_global_songs()
        
        if global_songs:
            df = pd.DataFrame([{"title": song.title, "artist": song.artist, "genre": song.genre} for song in global_songs])
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
        pass

    @staticmethod
    def update_global_songs():
        pass

    @staticmethod
    def delete_global_songs():
        pass