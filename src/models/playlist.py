from models.dao import DAO
from datetime import datetime


class Playlist:
    def __init__(
        self,
        id: int,
        id_user: int,
        name: str,
        description: str,
        creation_date: datetime,
    ) -> None:
        self.id = id
        self.id_user = id_user
        self.name = name
        self.description = description
        self.creation_date = creation_date

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("'name' must be a string")

        if not name:
            raise ValueError("'name' can't be empty")

        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("'description' must be a string")

        if not description:
            raise ValueError("'description' can't be empty")

        self.__description = description

    @property
    def creation_date(self) -> datetime:
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, creation_date: datetime) -> None:
        if not isinstance(creation_date, datetime):
            raise TypeError("'creation_date' must be a datetime")

        if creation_date > datetime.now():
            raise ValueError("'creation_date' can't be in the future")

        self.__creation_date = creation_date

    def __str__(self):
        return f"ID: {self.id}; ID User: {self.id_user}; Name: {self.name}; Description: {self.description}; Creation Date: {self.creation_date}"


class PlaylistDAO(DAO["Playlist"]):
    file_name = "playlist"

    @classmethod
    def to_dict(cls, obj: Playlist) -> dict:
        return {
            "id": obj.id,
            "id_user": obj.id_user,
            "name": obj.name,
            "description": obj.description,
            "creation_date": obj.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @classmethod
    def from_dict(cls, data: dict) -> Playlist:
        return Playlist(
            data["id"],
            data["id_user"],
            data["name"],
            data["description"],
            datetime.strptime(data["creation_date"], "%Y-%m-%d %H:%M:%S"),
        )
