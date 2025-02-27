import os
from models.dao import DAO

class Song:
    def __init__(
        self,
        id: int,
        id_library: int,
        title: str,
        artist: str,
        genre: str,
        file: str,
        count: int,
    ) -> None:
        self.id = id
        self.id_library = id_library
        self.title = title
        self.artist = artist
        self.genre = genre
        self.file = file
        self.count = count

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")
        if id < 0:
            raise ValueError("'id' can't be less than zero")

        self.__id = id

    @property
    def id_library(self) -> int:
        return self.__id_library

    @id_library.setter
    def id_library(self, id_library: int) -> None:
        if not isinstance(id_library, int):
            raise TypeError("'id_library' must be an integer")
        if id_library <= 0:
            raise ValueError("'id_library' can't be less than zero or equal to zero")

        self.__id_library = id_library

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError("'title' must be a string")

        if not title:
            raise ValueError("'title' can't be empty")

        self.__title = title

    @property
    def artist(self) -> str:
        return self.__artist

    @artist.setter
    def artist(self, artist: str) -> None:
        if not isinstance(artist, str):
            raise TypeError("'artist' must be a string")

        if not artist:
            raise ValueError("'artist' can't be empty")

        self.__artist = artist

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre: str) -> None:
        if not isinstance(genre, str):
            raise TypeError("'genre' must be a string")

        if not genre:
            raise ValueError("'genre' can't be empty")

        self.__genre = genre

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str) -> None:
        if not isinstance(file, str):
            raise TypeError("'file' must be a string")

        if not file:
            raise ValueError("'file' can't be empty")

        # TODO: Temporarily removed
        # if not os.path.isfile(file):
        #     raise ValueError("'file' is not a valid file")

        self.__file = file

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int) -> None:
        if not isinstance(count, int):
            raise TypeError("'count' must be an integer")

        if count < 0:
            raise ValueError("'count' can't be less than zero")

        self.__count = count

    def __str__(self):
        return f"ID: {self.id}; Library ID: {self.id_library}; Title: {self.title}; Artist: {self.artist}; Genre: {self.genre}; File: {self.file}; Count: {self.count}"


class SongDAO(DAO["Song"]):
    file_name = "songs"

    @classmethod
    def to_dict(cls, obj: Song) -> dict:
        return {
            "id": obj.id,
            "id_library": obj.id_library,
            "title": obj.title,
            "artist": obj.artist,
            "genre": obj.genre,
            "file": obj.file,
            "count": obj.count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Song:
        return Song(
            data["id"],
            data["id_library"],
            data["title"],
            data["artist"],
            data["genre"],
            data["file"],
            data["count"],
        )
    
    @classmethod
    def get_user_owned_songs(cls, id_user: int):
        return [song for song in cls.objects if song.id_library == id_user]
    
    @classmethod
    def get_all_global_songs(cls):
        return [song for song in cls.objects if song.id_library == 1]

    @classmethod
    def insert_audio_file(cls, obj: Song, audio_file) -> None:
        audio_dir = "src/data/songs"
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)

        audio_path = os.path.join(audio_dir, f"{obj.id}_{audio_file.name}")

        with open(audio_path, "wb") as f:
            f.write(audio_file.getbuffer())

        obj.file = audio_path
        SongDAO.update(obj.id, obj)

    