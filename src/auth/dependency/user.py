from fastapi import Depends
from auth.service.user import UserService
from auth.repository import UserRepository, GroupRepository
from database import create_session
from utils.security.criptografy import Criptografy
from auth.service.contracts import IUserService
from sqlalchemy.orm import Session


def inject_user_service(session: Session = Depends(create_session)) -> IUserService:
    return UserService(
        session=session,
        user_repository=UserRepository,
        group_repository=GroupRepository,
        criptografy=Criptografy
    )