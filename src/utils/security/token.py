from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import ExpiredSignatureError, InvalidTokenError, decode, encode

from settings import Settings


class Token:
    def __init__(self) -> None:
        self.SECRET_KEY = Settings().SECRET_KEY
        self.ALGORITHM = Settings().ALGORITHM_TOKEN
        self.ACCESS_TOKEN_EXPIRE_MINUTES = Settings().ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, data: dict) -> dict:
        to_encode = data.copy()
        expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        to_encode.update({"exp": expire})
        return encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

    def decode_access_token(self, token: str) -> dict:
        try:
            return decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        except ExpiredSignatureError as error:
            msg = "Token has expired"
            raise ValueError(msg) from error
        except InvalidTokenError as error:
            msg = "Invalid token"
            raise ValueError(msg) from error
