from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.repository import GroupRepository, UserRepository
from auth.service.contracts import IUserService
from auth.service.user import UserService
from database import create_session
from utils.security.criptografy import Criptografy

authentication_router = APIRouter()


def inject_user_service(session: Session = Depends(create_session)) -> IUserService:
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
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: IUserService = Depends(inject_user_service),
):
    return user_service.authenticate(form_data.username, form_data.password)
