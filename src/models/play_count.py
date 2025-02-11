from dao import DAO


class PlayCount:
    def __init__(self, id: int, id_user: int, id_song: int, count: int) -> None:
        self.__id: int = 0
        self.__id_user: int = 0
        self.__id_song: int = 0
        self.__count: int = 0

        self.id = id
        self.id_user = id_user
        self.id_song = id_song
        self.count = count

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")
        if id <= 0:
            raise ValueError("'id' can't be less than zero or equal to zero")

        self.__id = id

    @property
    def id_user(self) -> int:
        return self.__id_user

    @id_user.setter
    def id_user(self, id_user: int) -> None:
        if not isinstance(id_user, int):
            raise TypeError("'id_user' must be an integer")
        if id_user <= 0:
            raise ValueError("'id_user' can't be less than zero or equal to zero")

        self.__id_user = id_user

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
        return f"ID: {self.id}; User ID: {self.id_user}; Song ID: {self.id_song}; Count: {self.count}"


class PlayCountDAO(DAO["PlayCount"]):
    file_name = "play_count"

    @classmethod
    def to_dict(cls, obj: PlayCount) -> dict:
        return {
            "id": obj.id,
            "id_user": obj.id_user,
            "id_song": obj.id_song,
            "count": obj.count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> PlayCount:
        return PlayCount(
            data["id"],
            data["id_user"],
            data["id_song"],
            data["count"],
        )

