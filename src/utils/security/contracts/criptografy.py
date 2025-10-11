from abc import ABC, abstractmethod


class ICriptografy(ABC):
    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def hash_password(self, password: str) -> str: ...

    @abstractmethod
    def verify_password(self, plain_password: str, hash_password: str) -> bool: ...
