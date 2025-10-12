from pwdlib import PasswordHash

from utils.security.contracts import ICriptografy


class Criptografy(ICriptografy):
    def __init__(self) -> None:
        self.pwd_context = PasswordHash.recommended()

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hash_password)
