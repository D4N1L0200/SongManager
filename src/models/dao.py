import os
import json
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Protocol


class HasId(Protocol):
    id: int


T = TypeVar("T", bound=HasId)


class DAO(ABC, Generic[T]):
    objects: list[T] = []
    file_name: str

    @classmethod
    def clear(cls) -> None:
        cls.objects = []
        cls.save()

    @classmethod
    def insert(cls, obj: T) -> None:
        if obj.id == 0:
            ids: list[int] = [0]

            for o in cls.objects:
                ids.append(o.id)

            obj.id = max(ids) + 1

        cls.objects.append(obj)

        cls.save()

    @classmethod
    def get(cls) -> list[T]:
        return cls.objects

    @classmethod
    def get_by_id(cls, id: int) -> T:
        if id not in [o.id for o in cls.objects]:
            raise IndexError("ID not found")

        idx: int = [o.id for o in cls.objects].index(id)

        return cls.objects[idx]

    @classmethod
    def update(cls, id: int, obj: T) -> None:
        if id not in [o.id for o in cls.objects]:
            raise IndexError("ID not found")

        idx: int = [o.id for o in cls.objects].index(id)
        cls.objects[idx] = obj

        cls.save()

    @classmethod
    def delete(cls, id: int) -> None:
        if id not in [o.id for o in cls.objects]:
            raise IndexError("ID not found")

        idx: int = [o.id for o in cls.objects].index(id)
        del cls.objects[idx]

        cls.save()

    @classmethod
    def save(cls) -> None:
        data: list[dict] = []

        for obj in cls.objects:
            data.append(cls.to_dict(obj))

        with open(f"src/data/{cls.file_name}.json", "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls) -> None:
        data_dir = "src/data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        if not os.path.isfile(f"{data_dir}/{cls.file_name}.json"):
            with open(f"{data_dir}/{cls.file_name}.json", "w") as f:
                json.dump([], f)

        with open(f"{data_dir}/{cls.file_name}.json", "r") as f:
            data = json.load(f)

        cls.clear()

        for obj in data:
            cls.insert(cls.from_dict(obj))

    @classmethod
    @abstractmethod
    def to_dict(cls, obj: T) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> T:
        pass
