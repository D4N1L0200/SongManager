from dao import DAO
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
        self._id: int = 0
        self._id_user: int = 0
        self._name: str = ""
        self._description: str = ""
        self._creation_date: datetime = datetime.now()

        self.set_id(id)
        self.set_id_user(id_user)
        self.set_name(name)
        self.set_description(description)
        self.set_creation_date(creation_date)

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

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("'name' must be a string")

        if not name:
            raise ValueError("'name' can't be empty")

        self._name = name

    def set_description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("'description' must be a string")

        if not description:
            raise ValueError("'description' can't be empty")

        self._description = description

    def set_creation_date(self, creation_date: datetime) -> None:
        if not isinstance(creation_date, datetime):
            raise TypeError("'creation_date' must be a datetime")

        if creation_date > datetime.now():
            raise ValueError("'creation_date' can't be in the future")

        self._creation_date = creation_date

    def get_id(self) -> int:
        return self._id

    def get_id_user(self) -> int:
        return self._id_user

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_creation_date(self) -> datetime:
        return self._creation_date

    def __str__(self):
        return f"ID: {self.get_id()}; ID User: {self.get_id_user()}; name: {self.get_name()}; description: {self.get_description()}; creation date: {self.get_creation_date()}"


class PlaylistDAO(DAO["Playlist"]):
    @classmethod
    def save(cls) -> None:
        pass

    @classmethod
    def load(cls) -> None:
        pass
