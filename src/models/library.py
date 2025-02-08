import os
from dao import DAO


class Library:
    def __init__(self, id: int, is_global: bool, folder: str) -> None:
        self._id: int = 0
        self._is_global: bool = False
        self._folder: str = ""

        self.set_id(id)
        self.set_is_global(is_global)
        self.set_folder(folder)

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID can't be less than zero or equal to zero")

        self._id = id

    def set_is_global(self, is_global: bool) -> None:
        if not isinstance(is_global, bool):
            raise TypeError("Is global must be a boolean")

        self._is_global = is_global

    def set_folder(self, folder: str) -> None:
        if not isinstance(folder, str):
            raise TypeError("Folder must be a string")

        if not os.path.exists(folder):
            raise ValueError("Not a valid folder!")

        self._folder = folder

    def get_id(self) -> int:
        return self._id

    def get_is_global(self) -> bool:
        return self._is_global

    def get_folder(self) -> str:
        return self._folder

    def __str__(self):
        return f"ID: {self.get_id()}; Is Global: {self.get_is_global()}; Folder: {self.get_folder()}"


class LibraryDAO(DAO["Library"]):
    @classmethod
    def save(cls) -> None:
        pass

    @classmethod
    def load(cls) -> None:
        pass
