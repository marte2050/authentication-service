from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.security import Token
from auth.service.contracts import IUserService
from auth.dependency.user import inject_user_service


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def inject_verify_permission(permissions: str = None):
    def dependency(
            token: str = Depends(oauth2_scheme), 
            user_service: IUserService = Depends(inject_user_service),
        ):
        try:
            token_manager = Token()
            token_valid = token_manager.decode_access_token(token)
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
        email = token_valid.get("sub")
        return user_service.verify_permission(email, permissions)
    return dependency