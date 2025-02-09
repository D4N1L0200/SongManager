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
        self._id: int = 0
        self._name: str = ""
        self._password: str = ""
        self._creation_date: datetime = datetime.now()
        self._is_admin: bool = False

        self.set_id(id)
        self.set_name(name)
        self.set_password(password)
        self.set_creation_date(creation_date)
        self.set_is_admin(is_admin)

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("'id' must be an integer")

        if id < 0:
            raise ValueError("'id' can't be less than zero")

        self._id = id

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("'name' must be a string")

        if not name:
            raise ValueError("'name' can't be empty")

        self._name = name

    def set_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("'password' must be a string")

        if not password:
            raise ValueError("'password' can't be empty")

        self._password = password

    def set_creation_date(self, creation_date: datetime) -> None:
        if not isinstance(creation_date, datetime):
            raise TypeError("'creation_date' must be a datetime")

        if creation_date > datetime.now():
            raise ValueError("'creation_date' can't be in the future")

        self._creation_date = creation_date

    def set_is_admin(self, is_admin: bool) -> None:
        if not isinstance(is_admin, bool):
            raise TypeError("'is_admin' must be a boolean")

        self._is_admin = is_admin

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_password(self) -> str:
        return self._password

    def get_creation_date(self) -> datetime:
        return self._creation_date

    def get_is_admin(self) -> bool:
        return self._is_admin

    def __str__(self):
        return f"ID: {self.get_id()}; Name: {self.get_name()}; Password: {self.get_password()}; Creation date: {self.get_creation_date()}; Is admin: {self.get_is_admin()}"


class UserDAO(DAO["User"]):
    file_name = "users"

    @classmethod
    def to_dict(cls, obj: User) -> dict:
        return {
            "id": obj.get_id(),
            "name": obj.get_name(),
            "password": obj.get_password(),
            "creation_date": obj.get_creation_date().strftime("%Y-%m-%d %H:%M:%S"),
            "is_admin": obj.get_is_admin(),
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
