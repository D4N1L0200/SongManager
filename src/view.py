from models.user import User, UserDAO
from models.library import Library, LibraryDAO
from models.play_count import PlayCount, PlayCountDAO
from models.playlist_item import PlaylistItem, PlaylistItemDAO
from models.playlist_item import PlaylistItem, PlaylistItemDAO
from models.playlist import Playlist, PlaylistDAO
from models.song import Song, SongDAO
from models.user import User, UserDAO

from datetime import datetime, timedelta


class View:
    @staticmethod
    def load_all():
        UserDAO.load()
        LibraryDAO.load()
        PlayCountDAO.load()
        PlaylistItemDAO.load()
        PlaylistDAO.load()
        SongDAO.load()

    @staticmethod
    def user_admin():
        for c in View.users_get():
            if c.name == "admin":
                return
        View.users_insert("admin", "admin", datetime.now(), True)
        # View.libraries_insert(True, "global")

    @staticmethod
    def users_clear():
        UserDAO.clear()

    @staticmethod
    def users_insert(name: str, password: str, creation_date: datetime, is_admin: bool):
        u = User(0, name, password, creation_date, is_admin)
        UserDAO.insert(u)
        View.libraries_insert(is_admin, name)

    @staticmethod
    def users_get():
        return UserDAO.get()

    @staticmethod
    def users_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return UserDAO.get_by_id(id)

    @staticmethod
    def is_name_taken(name: str):
        return UserDAO.is_name_taken(name)

    @staticmethod
    def users_update(id: int, name: str, password: str):
        if id < 0:
            raise ValueError("Invalid ID")
        if not UserDAO.get_by_id(id):
            raise ValueError("The given id doesn't match an user")
        if len(name) < 2:
            raise ValueError("Invalid name")

        o = UserDAO.get_by_id(id)
        creation_date = o.creation_date

        u = User(id, name, password, creation_date, False)
        UserDAO.update(id, u)

    @staticmethod
    def users_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        UserDAO.delete(id)

    @staticmethod
    def user_authenticate(email: str, password: str):
        for c in View.users_get():
            if c.name == email and c.password == password:
                return {"id": c.id, "name": c.name}

        return None

    @staticmethod
    def playlists_clear():
        PlaylistDAO.clear()

    @staticmethod
    def playlists_insert(
        id: int, id_user: int, name: str, description: str, creation_date: datetime
    ):
        p = Playlist(id, id_user, name, description, creation_date)
        PlaylistDAO.insert(p)

    @staticmethod
    def playlists_get():
        return PlaylistDAO.get()

    @staticmethod
    def playlists_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return PlaylistDAO.get_by_id(id)

    @staticmethod
    def get_owned_playlists(id_user: int):
        return PlaylistDAO.get_owned_playlists(id_user)

    @staticmethod
    def playlists_update(
        id: int, id_user: int, name: str, description: str, creation_date: datetime
    ):
        if id < 0:
            raise ValueError("Invalid ID")
        if len(name) < 2:
            raise ValueError("Invalid name")
        if len(name) < 2:
            raise ValueError("Invalid description")

        p = Playlist(id, id_user, name, description, creation_date)
        PlaylistDAO.update(id, p)

    @staticmethod
    def playlists_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        PlaylistDAO.delete(id)

    @staticmethod
    def songs_clear():
        SongDAO.clear()

    @staticmethod
    def songs_insert(
        id_library: int, title: str, artist: str, genre: str, file_name: str, count: int, file
    ):
        if file is None:
            raise ValueError("Invalid file")

        s = Song(0, id_library, title, artist, genre, file_name, count)
        SongDAO.insert(s)
        SongDAO.insert_audio_file(s, file)

    @staticmethod
    def songs_get():
        return SongDAO.get()

    @staticmethod
    def songs_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return SongDAO.get_by_id(id)

    @staticmethod
    def get_all_global_songs():
        return SongDAO.get_all_global_songs()
    @staticmethod
    def get_user_owned_songs(id_user: int):
        if id_user < 0:
            raise ValueError("ID can't be less than zero")
        return SongDAO.get_user_owned_songs(id_user)
    @staticmethod
    def songs_update(
        id: int,
        id_library: int,
        title: str,
        artist: str,
        genre: str,
        file: str,
        count: int,
    ):
        if id < 0:
            raise ValueError("Invalid ID")
        if len(title) < 2:
            raise ValueError("Invalid title")
        if len(artist) < 2:
            raise ValueError("Invalid artist")
        if len(genre) < 2:
            raise ValueError("Invalid genre")
        if len(file) < 2:
            raise ValueError("Invalid file")

        s = Song(id, id_library, title, artist, genre, file, count)
        SongDAO.update(id, s)

    @staticmethod
    def songs_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        SongDAO.delete(id)

    @staticmethod
    def libraries_clear():
        LibraryDAO.clear()

    @staticmethod
    def libraries_insert(is_global: bool, folder: str):
        l = Library(0, is_global, folder)
        LibraryDAO.insert(l)

    @staticmethod
    def libraries_get():
        return LibraryDAO.get()

    @staticmethod
    def libraries_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return LibraryDAO.get_by_id(id)

    @staticmethod
    def libraries_update(id: int, is_global: bool, folder: str):
        if id < 0:
            raise ValueError("Invalid ID")

        l = Library(id, is_global, folder)
        LibraryDAO.update(id, l)

    @staticmethod
    def libraries_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        LibraryDAO.delete(id)

    @staticmethod
    def playcounts_clear():
        PlayCountDAO.clear()

    @staticmethod
    def playcounts_insert(id_user: int, id_song: int, count: int):
        pc = PlayCount(0, id_user, id_song, count)
        PlayCountDAO.insert(pc)

    @staticmethod
    def playcounts_get():
        return PlayCountDAO.get()

    @staticmethod
    def playcounts_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return PlayCountDAO.get_by_id(id)

    @staticmethod
    def playcounts_update(id: int, id_user: int, id_song: int, count: int):
        if id < 0:
            raise ValueError("Invalid ID")

        pc = PlayCount(id, id_user, id_song, count)
        PlayCountDAO.update(id, pc)

    @staticmethod
    def playcounts_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        PlayCountDAO.delete(id)

    @staticmethod
    def playlistitems_clear():
        PlaylistItemDAO.clear()

    @staticmethod
    def playlistitems_insert(id_playlist: int, id_song: int, count: int):
        if id_playlist < 0:
            raise ValueError("ID can't be less than zero")
        if id_song < 0:
            raise ValueError("ID can't be less than zero")

        pi = PlaylistItem(0, id_playlist, id_song, count)
        PlaylistItemDAO.insert(pi)

    @staticmethod
    def playlistitems_get():
        return PlaylistItemDAO.get()

    @staticmethod
    def playlistitems_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return PlaylistItemDAO.get_by_id(id)

    @staticmethod
    def playlistitems_update(id: int, id_playlist: int, id_song: int, count: int):
        if id < 0:
            raise ValueError("Invalid ID")
        if id_playlist < 0:
            raise ValueError("Invalid ID")
        if id_song < 0:
            raise ValueError("Invalid ID")

        pi = PlaylistItem(id, id_playlist, id_song, count)
        PlaylistItemDAO.update(id, pi)

    @staticmethod
    def playlistitems_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        PlaylistItemDAO.delete(id)
