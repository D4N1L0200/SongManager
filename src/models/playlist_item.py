from dao import DAO


class PlaylistItem:
    def __init__(self, id: int, id_playlist: int, id_song: int, count: int) -> None:
        self._id: int = 0
        self._id_playlist: int = 0
        self._id_song: int = 0
        self._count: int = 0

        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_song(id_song)
        self.set_count(count)

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")
        if id <= 0:
            raise ValueError("'id' can't be less than zero or equal to zero")

        self._id = id

    def set_id_playlist(self, id_playlist: int) -> None:
        if not isinstance(id_playlist, int):
            raise TypeError("'id_playlist' must be an integer")
        if id_playlist <= 0:
            raise ValueError("'id_playlist' can't be less than zero or equal to zero")

        self._id_playlist = id_playlist

    def set_id_song(self, id_song: int) -> None:
        if not isinstance(id_song, int):
            raise TypeError("'id_song' must be an integer")
        if id_song <= 0:
            raise ValueError("'id_song' can't be less than zero or equal to zero")

        self._id_song = id_song

    def set_count(self, count: int) -> None:
        if not isinstance(count, int):
            raise TypeError("'count' must be an integer")
        if count <= 0:
            raise ValueError("'count' can't be less than zero or equal to zero")

        self._count = count

    def get_id(self) -> int:
        return self._id

    def get_id_playlist(self) -> int:
        return self._id_playlist

    def get_id_song(self) -> int:
        return self._id_song

    def get_count(self) -> int:
        return self._count

    def __str__(self):
        return f"ID: {self.get_id()}; Playlist ID: {self.get_id_playlist()}; Song ID: {self.get_id_song()}; Count: {self.get_count()}"


class PlaylistItemDAO(DAO["PlaylistItem"]):
    @classmethod
    def save(cls) -> None:
        pass

    @classmethod
    def load(cls) -> None:
        pass
