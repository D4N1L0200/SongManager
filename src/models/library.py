import os

class Library:
    def __init__(self, id, is_global, folder):
        self._id = id
        self._is_global = is_global
        self._folder = folder
    def get_id(self): return self._id
    def get_is_global(self): return self._is_global
    def get_folder(self): return self._folder
    def set_id(self, id: int):
        if id < 0:
            raise ValueError("ID can't be less than zero")
        self._id = id
    def set_is_global(self, is_global: bool):
        self._is_global = is_global
    def set_folder(self, folder: str):
        if not os.path.exists(folder):
            raise ValueError("Not an valid folder!")        
        self._folder = folder
    def __str__(self):
        return f"ID: {self.get_id()}; Is Global: {self.get_is_global()}; Folder: {self.get_folder()}"