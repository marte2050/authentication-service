from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utils.security import Token
from auth.service.contracts import IUserService
from auth.dependency.user import inject_user_service
from database import create_session
from auth.service.contracts import IPermissionService
from auth.service import PermissionService
from auth.repository import GroupRepository, PermissionRepository


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

def inject_permission_service(session: Session = Depends(create_session)) -> IPermissionService:
    return PermissionService(
        session=session,
        permission_repository=PermissionRepository,
        group_repository=GroupRepository
    )