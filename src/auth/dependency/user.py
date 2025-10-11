from fastapi import Depends
from sqlalchemy.orm import Session

from auth.repository import GroupRepository, UserRepository
from auth.service.contracts import IUserService
from auth.service.user import UserService
from database import create_session
from utils.security.criptografy import Criptografy


def inject_user_service(session: Session = Depends(create_session)) -> IUserService:
    return UserService(
        session=session,
        user_repository=UserRepository,
        group_repository=GroupRepository,
        criptografy=Criptografy,
    )
