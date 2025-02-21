# import os
from models.dao import DAO


class Library:
    def __init__(self, id: int, is_global: bool, folder: str) -> None:
        self.id = id
        self.is_global = is_global
        self.folder = folder

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
    def is_global(self) -> bool:
        return self.__is_global

    @is_global.setter
    def is_global(self, is_global: bool) -> None:
        if not isinstance(is_global, bool):
            raise TypeError("'is_global' must be a boolean")

        self.__is_global = is_global

    @property
    def folder(self) -> str:
        return self.__folder

    @folder.setter
    def folder(self, folder: str) -> None:
        if not isinstance(folder, str):
            raise TypeError("'folder' must be a string")

        if not folder:
            raise ValueError("'folder' can't be empty")

        # TODO: Temporarily removed
        # if not os.path.exists(folder):
        #     raise ValueError("'folder' is not a valid folder!")

        self.__folder = folder

    def __str__(self):
        return f"ID: {self.id}; Is Global: {self.is_global}; Folder: {self.folder}"


class LibraryDAO(DAO["Library"]):
    file_name = "library"

    @classmethod
    def to_dict(cls, obj: Library) -> dict:
        return {
            "id": obj.id,
            "is_global": obj.is_global,
            "folder": obj.folder,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Library:
        return Library(
            data["id"],
            data["is_global"],
            data["folder"],
        )
