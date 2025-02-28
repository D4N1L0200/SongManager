import os
import streamlit as st
import pandas as pd
from view import View
import time


class MySongsUI:
    @staticmethod
    def main():
        st.header("My songs")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "See my songs",
                "See my own songs",
                "Add song",
                "Add global song",
                "Update song",
            ]
        )
        with tab1:
            MySongsUI.see_my_songs()
        with tab2:
            MySongsUI.see_my_own_songs()
        with tab3:
            MySongsUI.add_song()
        with tab4:
            MySongsUI.add_global_songs()
        with tab5:
            MySongsUI.update_song()

    @staticmethod
    def see_my_songs():
        # O usuário pode ver as músicas globais por essa playlist, tipo "músicas curtidas", as músicas que são associadas diretamente à ele são só aquelas que fazem parte de sua library, ou seja, suas músicas próprias. Para escutar uma música global como se fosse sua, é preciso adicioná-la à essa "músicas curtidas", que na verdade não é músicas curtidas, mas sim uma playlist com as músicas globais e as próprias. É preciso arrumar um nome melhor para ela.
        # st.subheader("Your Liked Songs")

        id_liked_songs = View.get_liked_songs_id_by_user(st.session_state["user_id"])

        if id_liked_songs:
            songs = View.get_songs_by_playlist(id_liked_songs)
            if songs:
                df = pd.DataFrame(
                    [
                        {
                            "title": song.title,
                            "artist": song.artist,
                            "genre": song.genre,
                        }
                        for song in songs
                    ]
                )
                st.dataframe(df)

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
            else:
                st.write("You don't have any liked songs yet")

    @staticmethod
    def see_my_own_songs():
        # library
        # pode deletar músicas aqui também
        # st.subheader("Your own Songs")

        own_songs = View.get_user_owned_songs(st.session_state["user_id"])

        if own_songs:
            df = pd.DataFrame(
                [
                    {"title": song.title, "artist": song.artist, "genre": song.genre}
                    for song in own_songs
                ]
            )
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
        # st.subheader("Add a Song to Your Library")

        title = st.text_input("Insert the song's title:")
        artist = st.text_input("Insert the song's artist:")
        genre = st.text_input("Insert the song's genre:")
        file = st.file_uploader("Insert a MP3 or a WAV file:", type=["mp3", "wav"])
        if st.button("Add song"):
            if title and artist and genre and file:
                View.songs_insert(
                    (st.session_state["user_id"]),
                    title,
                    artist,
                    genre,
                    file.name,
                    0,
                    file,
                )
                st.success("Song inserted with sucess")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Please fill all the fields")

    @staticmethod
    def add_global_songs():
        # aqui você adiciona as músicas globais à Liked Songs para poder adicionar qualquer das liked songs em alguma playlist
        # st.subheader("Add Global Songs to Your Liked Songs Playlist")

        liked_songs_id = View.get_liked_songs_id_by_user(st.session_state["user_id"])

        liked_songs_songs = View.get_songs_by_playlist(liked_songs_id)

        global_songs = View.get_all_global_songs()

        if global_songs:
            liked_songs_ids = [song.id for song in liked_songs_songs]

            songs_to_show = [
                song for song in global_songs if song.id not in liked_songs_ids
            ]

            if not songs_to_show:
                st.write("You already liked all the global songs")
                return

            df = pd.DataFrame(
                [
                    {"title": song.title, "artist": song.artist, "genre": song.genre}
                    for song in songs_to_show
                ]
            )
            st.dataframe(df)

            for song in songs_to_show:
                song_title = song.title
                song_file_path = song.file

                st.write(f"{song_title} - {song.artist}")
                if os.path.isfile(song_file_path):
                    if song_file_path.endswith(".mp3"):
                        st.audio(song_file_path, format="audio/mp3")
                    elif song_file_path.endswith(".wav"):
                        st.audio(song_file_path, format="audio/wav")

                    if st.button("Add song", key=f"add_song_{song.id}"):
                        View.playlistitems_insert(liked_songs_id, song.id, 0)
                        st.success("Song inserted with success")
                        time.sleep(2)
                        st.rerun()
                else:
                    st.write(f"Cannot play {song_title}, file not found.")
        else:
            st.write("There are no global songs yet")

    @staticmethod
    def update_song():
        pass

    # @staticmethod
    # def delete():
    #     pass
