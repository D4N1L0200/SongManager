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
        self._id: int = 0
        self._id_library: int = 0
        self._title: str = ""
        self._artist: str = ""
        self._genre: str = ""
        self._file: str = ""
        self._count: int = 0

        self.set_id(id)
        self.set_id_library(id_library)
        self.set_title(title)
        self.set_artist(artist)
        self.set_genre(genre)
        self.set_file(file)
        self.set_count(count)

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")
        if id < 0:
            raise ValueError("'id' can't be less than zero")

        self._id = id

    def set_id_library(self, id_library: int) -> None:
        if not isinstance(id_library, int):
            raise TypeError("'id_library' must be an integer")
        if id_library <= 0:
            raise ValueError("'id_library' can't be less than zero or equal to zero")

        self._id_library = id_library

    def set_title(self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError("'title' must be a string")

        if not title:
            raise ValueError("'title' can't be empty")

        self._title = title

    def set_artist(self, artist: str) -> None:
        if not isinstance(artist, str):
            raise TypeError("'artist' must be a string")

        if not artist:
            raise ValueError("'artist' can't be empty")

        self._artist = artist

    def set_genre(self, genre: str) -> None:
        if not isinstance(genre, str):
            raise TypeError("'genre' must be a string")

        if not genre:
            raise ValueError("'genre' can't be empty")

        self._genre = genre

    def set_file(self, file: str) -> None:
        if not isinstance(file, str):
            raise TypeError("'file' must be a string")

        if not file:
            raise ValueError("'file' can't be empty")

        # TODO: Temporarily removed
        # if not os.path.isfile(file):
        #     raise ValueError("'file' is not a valid file")

        self._file = file

    def set_count(self, count: int) -> None:
        if not isinstance(count, int):
            raise TypeError("'count' must be an integer")

        if count < 0:
            raise ValueError("'count' can't be less than zero")

        self._count = count

    def get_id(self) -> int:
        return self._id

    def get_id_library(self) -> int:
        return self._id_library

    def get_title(self) -> str:
        return self._title

    def get_artist(self) -> str:
        return self._artist

    def get_genre(self) -> str:
        return self._genre

    def get_file(self) -> str:
        return self._file

    def get_count(self) -> int:
        return self._count

    def __str__(self):
        return f"ID: {self.get_id()}; Library ID: {self.get_id_library()}; Title: {self.get_title()}; Artist: {self.get_artist()}; Genre: {self.get_genre()}; File: {self.get_file()}; Count: {self.get_count()}"


class SongDAO(DAO["Song"]):
    file_name = "songs"

    @classmethod
    def to_dict(cls, obj: Song) -> dict:
        return {
            "id": obj.get_id(),
            "id_library": obj.get_id_library(),
            "title": obj.get_title(),
            "artist": obj.get_artist(),
            "genre": obj.get_genre(),
            "file": obj.get_file(),
            "count": obj.get_count(),
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
