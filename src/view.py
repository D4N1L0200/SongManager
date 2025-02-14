from ast import Try
from models.user import User, UserDAO
from models.library import Library, LibraryDAO
from models.play_count import PlayCount, PlayCountDAO
from models.playlist_item import PlaylistItem, PlaylistItemDAO
from models.playlist_item import PlaylistItem, PlaylistItemDAO
from models.playlist import Playlist, PlaylistDAO
from models.song import Song, SongDAO
from models.user import User, UserDAO

from datetime import datetime, timedelta

class View():
    #clear insert get getid update delete
    @staticmethod
    def users_clear():
        UserDAO.clear()
    @staticmethod
    def users_insert():
        pass
    @staticmethod
    def users_get():
        return UserDAO.get()
    @staticmethod
    def users_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return UserDAO.get_by_id(id)
    @staticmethod
    def users_update(id: int, name: str, password: str, creation_date: datetime):
        if id < 0:
            raise ValueError("Not a valid ID")
        if not UserDAO.get_by_id(id):
            raise ValueError("The given id doesn't match an user")
        if len(name) < 2:
            raise ValueError("Not a valid name")
        
        u = User(id, name, password, creation_date, False)
        UserDAO.update(u)
    @staticmethod
    def users_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        UserDAO.delete(id)
    
    @staticmethod
    def playlists_clear():
        PlaylistDAO.clear()
    @staticmethod
    def playlists_insert():
        pass
    @staticmethod
    def playlists_get():
        return PlaylistDAO.get()
    @staticmethod
    def playlists_get_by_id(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        return PlaylistDAO.get_by_id(id)
    @staticmethod
    def playlists_update(id: int, id_user: int,name: str, description: str, creation_date: datetime):
        if id < 0:
            raise ValueError("Not a valid ID")
        if len(name) < 2:
            raise ValueError("Not a valid name")
        if len(name) < 2:
            raise ValueError("Not a valid description")
        
        p = Playlist(id, id_user, name, description, creation_date)
        PlaylistDAO.update(p)
    @staticmethod
    def playlists_delete(id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")

        PlaylistDAO.delete(id)
