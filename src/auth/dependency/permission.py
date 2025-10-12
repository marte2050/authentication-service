from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from auth.dependency.user import inject_user_service
from auth.model import User
from auth.repository import GroupRepository, PermissionRepository
from auth.service import PermissionService
from auth.service.contracts import IPermissionService, IUserService
from database import create_session
from utils.security import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def inject_verify_permission(permissions: str) -> User:
    def dependency(
        token: Annotated[str, Depends(oauth2_scheme)],
        user_service: Annotated[IUserService, Depends(inject_user_service)],
    ) -> User:
        try:
            token_manager = Token()
            token_valid = token_manager.decode_access_token(token)
        except ValueError as error:
            raise HTTPException(status_code=401, detail=str(error)) from error

        email = token_valid.get("sub")
        return user_service.verify_permission(email, permissions)

    return dependency


def inject_permission_service(session: Annotated[Session, Depends(create_session)]) -> IPermissionService:
    return PermissionService(
        session=session,
        permission_repository=PermissionRepository,
        group_repository=GroupRepository,
    )
