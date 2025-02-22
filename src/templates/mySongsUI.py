import os
import streamlit as st
import pandas as pd
from view import View
import time

class MySongsUI:
    @staticmethod
    def main():
        st.header("My songs")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["See my songs", "See my own songs", "Add song", "Add global song", "Update song"])
        with tab1: MySongsUI.see_my_songs()
        with tab2: MySongsUI.see_my_own_songs()
        with tab3: MySongsUI.add_song()
        with tab4: MySongsUI.add_global_songs()
        with tab5: MySongsUI.update_song()
    @staticmethod
    def see_my_songs():
        #O usuário pode ver as músicas globais por essa playlist, tipo "músicas curtidas", as músicas que são associadas diretamente à ele são só aquelas que fazem parte de sua library, ou seja, suas músicas próprias. Para escutar uma música global como se fosse sua, é preciso adicioná-la à essa "músicas curtidas", que na verdade não é músicas curtidas, mas sim uma playlist com as músicas globais e as próprias. É preciso arrumar um nome melhor para ela.
        pass
    @staticmethod
    def see_my_own_songs():
        #library
        #pode deletar músicas aqui também
        own_songs = View.get_user_owned_songs(st.session_state["user_id"])

        if own_songs:
            df = pd.DataFrame([{"title": song.title, "artist": song.artist, "genre": song.genre} for song in own_songs])
            st.dataframe(df)

            for song in own_songs:
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
            st.write("You don't have any songs yet")

    @staticmethod
    def add_song():
        title = st.text_input("Insert the song's title:")
        artist = st.text_input("Insert the song's artist:")
        genre = st.text_input("Insert the song's genre:")
        file = st.file_uploader("Insert a MP3 or a WAV file:", type = ["mp3", "wav"])
        if st.button("Add song"):
            if title and artist and genre and file:
                st.write(st.session_state["user_id"])
                View.songs_insert((st.session_state["user_id"]), title, artist, genre, file.name, 0, file)
                st.success("Song inserted with sucess")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Please fill in all the fields")
    @staticmethod
    def add_global_songs():
        pass
    @staticmethod
    def update_song():
        pass

    # @staticmethod
    # def delete():
    #     pass