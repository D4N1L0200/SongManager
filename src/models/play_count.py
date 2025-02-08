from dao import DAO


class PlayCount:
    def __init__(self, id: int, id_user: int, id_song: int, count: int) -> None:
        self._id: int = 0
        self._id_user: int = 0
        self._id_song: int = 0
        self._count: int = 0

        self.set_id(id)
        self.set_id_user(id_user)
        self.set_id_song(id_song)
        self.set_count(count)

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")
        if id <= 0:
            raise ValueError("'id' can't be less than zero or equal to zero")

        self._id = id

    def set_id_user(self, id_user: int) -> None:
        if not isinstance(id_user, int):
            raise TypeError("'id_user' must be an integer")
        if id_user <= 0:
            raise ValueError("'id_user' can't be less than zero or equal to zero")

        self._id_user = id_user

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

    def get_id_user(self) -> int:
        return self._id_user

    def get_id_song(self) -> int:
        return self._id_song

    def get_count(self) -> int:
        return self._count

    def __str__(self):
        return f"ID: {self.get_id()}; User ID: {self.get_id_user()}; Song ID: {self.get_id_song()}; Count: {self.get_count()}"


class PlayCountDAO(DAO["PlayCount"]):
    @classmethod
    def save(cls) -> None:
        pass

    @classmethod
    def load(cls) -> None:
        pass
