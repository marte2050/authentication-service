from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from settings import Settings


class Token:
    def __init__(self):
        self.SECRET_KEY = Settings().SECRET_KEY
        self.ALGORITHM = Settings().ALGORITHM_TOKEN
        self.ACCESS_TOKEN_EXPIRE_MINUTES = Settings().ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, data: dict) -> dict:
        to_encode = data.copy()
        expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({'exp': expire})
        encoded_jwt = encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    def decode_access_token(self, token: str) -> dict:
        try:
            decoded_jwt = decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return decoded_jwt
        except ExpiredSignatureError:
            raise ValueError("Token has expired")
        except InvalidTokenError:
            raise ValueError("Invalid token")

