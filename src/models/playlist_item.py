from models.dao import DAO


class PlaylistItem:
    def __init__(self, id: int, id_playlist: int, id_song: int, count: int) -> None:
        self.id = id
        self.id_playlist = id_playlist
        self.id_song = id_song
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
    def id_playlist(self) -> int:
        return self.__id_playlist

    @id_playlist.setter
    def id_playlist(self, id_playlist: int) -> None:
        if not isinstance(id_playlist, int):
            raise TypeError("'id_playlist' must be an integer")
        if id_playlist <= 0:
            raise ValueError("'id_playlist' can't be less than zero or equal to zero")

        self.__id_playlist = id_playlist

    @property
    def id_song(self) -> int:
        return self.__id_song

    @id_song.setter
    def id_song(self, id_song: int) -> None:
        if not isinstance(id_song, int):
            raise TypeError("'id_song' must be an integer")
        if id_song <= 0:
            raise ValueError("'id_song' can't be less than zero or equal to zero")

        self.__id_song = id_song

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int) -> None:
        if not isinstance(count, int):
            raise TypeError("'count' must be an integer")
        if count <= 0:
            raise ValueError("'count' can't be less than zero or equal to zero")

        self.__count = count

    def __str__(self):
        return f"ID: {self.id}; Playlist ID: {self.id_playlist}; Song ID: {self.id_song}; Count: {self.count}"


class PlaylistItemDAO(DAO["PlaylistItem"]):
    file_name = "playlist_item"

    @classmethod
    def to_dict(cls, obj: PlaylistItem) -> dict:
        return {
            "id": obj.id,
            "id_playlist": obj.id_playlist,
            "id_song": obj.id_song,
            "count": obj.count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> PlaylistItem:
        return PlaylistItem(
            data["id"],
            data["id_playlist"],
            data["id_song"],
            data["count"],
        )
