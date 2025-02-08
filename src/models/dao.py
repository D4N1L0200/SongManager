from abc import ABC, abstractmethod


from typing import Generic, TypeVar

T = TypeVar("T")


class DAO(Generic[T]):
    objects: list[T] = []

    @classmethod
    def insert(cls, obj: T) -> None:
        cls.objects.append(obj)

    @classmethod
    def get(cls) -> list[T]:
        return cls.objects

    @classmethod
    def get_by_id(cls, id: int) -> T:
        if id < 0 or id >= len(cls.objects):
            raise IndexError("Index out of range")

        return cls.objects[id]

    @classmethod
    def update(cls, id: int, obj: T) -> None:
        if id < 0 or id >= len(cls.objects):
            raise IndexError("Index out of range")

        cls.objects[id] = obj

    @classmethod
    def delete(cls, id: int) -> None:
        if id < 0 or id >= len(cls.objects):
            raise IndexError("Index out of range")

        del cls.objects[id]

    @classmethod
    @abstractmethod
    def save(cls) -> None:
        pass

    @classmethod
    @abstractmethod
    def load(cls) -> None:
        pass
