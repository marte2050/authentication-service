from abc import ABC, abstractmethod


class ICriptografy(ABC):
    """Class for handling password hashing and verification."""

    @abstractmethod
    def __init__(self) -> None:
        """Initializes the Criptografy class with a password hashing context."""

    @abstractmethod
    def hash_password(self, password: str) -> str:
        """Hashes a password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """

    @abstractmethod
    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        """Verifies a password against a hashed password.

        Args:
            plain_password (str): The plain password to verify.
            hash_password (str): The hashed password to verify against.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
