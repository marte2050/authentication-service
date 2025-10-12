from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.repository import GroupRepository, UserRepository
from auth.service.contracts import IUserService
from auth.service.user import UserService
from database import create_session
from utils.security.criptografy import Criptografy

authentication_router = APIRouter()


def inject_user_service(session: Annotated[Session, Depends(create_session)]) -> IUserService:
    return UserService(
        session=session,
        user_repository=UserRepository,
        group_repository=GroupRepository,
        criptografy=Criptografy,
    )


@authentication_router.post(
    "/login",
    tags=["auth"],
    summary="Authenticate user and return a token",
)
async def login(
    user_service: Annotated[IUserService, Depends(inject_user_service)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> dict:
    return user_service.authenticate(form_data.username, form_data.password)
