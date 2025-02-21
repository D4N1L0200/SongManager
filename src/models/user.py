from datetime import datetime
from models.dao import DAO, HasId


class User(HasId):
    def __init__(
        self,
        id: int,
        name: str,
        password: str,
        creation_date: datetime,
        is_admin: bool,
    ) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.creation_date = creation_date
        self.is_admin = is_admin

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
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("'password' must be a string")

        if not password:
            raise ValueError("'password' can't be empty")

        self.__password = password

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

    @property
    def is_admin(self) -> bool:
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin: bool) -> None:
        if not isinstance(is_admin, bool):
            raise TypeError("'is_admin' must be a boolean")

        self.__is_admin = is_admin

    def __str__(self):
        return f"ID: {self.id}; Name: {self.name}; Password: {self.password}; Creation date: {self.creation_date}; Is admin: {self.is_admin}"


class UserDAO(DAO["User"]):
    file_name = "users"

    @classmethod
    def to_dict(cls, obj: User) -> dict:
        return {
            "id": obj.id,
            "name": obj.name,
            "password": obj.password,
            "creation_date": obj.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            "is_admin": obj.is_admin,
        }

    @classmethod
    def from_dict(cls, data: dict) -> User:
        return User(
            data["id"],
            data["name"],
            data["password"],
            datetime.strptime(data["creation_date"], "%Y-%m-%d %H:%M:%S"),
            data["is_admin"],
        )
