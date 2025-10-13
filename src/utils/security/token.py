import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import ExpiredSignatureError, InvalidTokenError, decode, encode

from settings import Settings


class Token:
    def __init__(self) -> None:
        secret_key, algorithm, access_token_expire_minutes = self.is_production_or_staging().values()
        self.SECRET_KEY = secret_key
        self.ALGORITHM = algorithm
        self.ACCESS_TOKEN_EXPIRE_MINUTES = access_token_expire_minutes

    def is_production_or_staging(self) -> bool:
        production_or_staging = os.getenv("PRODUCTION_OR_STAGING", "development")

        if production_or_staging in ["production", "staging"]:
            return {
                "SECRET_KEY": os.getenv("SECRET_KEY"),
                "ALGORITHM": os.getenv("ALGORITHM_TOKEN"),
                "ACCESS_TOKEN_EXPIRE_MINUTES": int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")),
            }

        return {
            "SECRET_KEY": Settings().SECRET_KEY,
            "ALGORITHM": Settings().ALGORITHM_TOKEN,
            "ACCESS_TOKEN_EXPIRE_MINUTES": Settings().ACCESS_TOKEN_EXPIRE_MINUTES,
        }

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
