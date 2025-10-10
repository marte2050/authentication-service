from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import create_session
from utils.security.criptografy import Criptografy
from auth.service.contracts import IUserService
from auth.service.user import UserService
from auth.repository import UserRepository, GroupRepository
from auth.schemas import (
    UserAddSchemaResponse, 
    UserAddSchemaRequest,
    UserUpdateSchemaResponse,
    UserUpdateSchemaRequest,
    UserListSchemaResponse
)


auth_router = APIRouter()

def inject_user_service(session: Session = Depends(create_session)) -> IUserService:
    return UserService(
        session=session,
        user_repository=UserRepository,
        group_repository=GroupRepository,
        criptografy=Criptografy
    )

@auth_router.post(
    "/user/",
    tags=["auth"],
    summary="Create a new user",
    response_model=UserAddSchemaResponse,
)
async def add_user(
    data: UserAddSchemaRequest,
    user_service: IUserService = Depends(inject_user_service)
):
    data_json = data.model_dump()
    record = user_service.create_user(data_json)
    return record


@auth_router.delete(
    "/user/{user_id}",
    tags=["auth"],
    summary="Delete a user by ID",
)
async def delete_user(
    user_id: int,
    user_service: IUserService = Depends(inject_user_service)
):
    user_service.delete_user(user_id)
    return {"detail": "User deleted successfully"}

@auth_router.put(
    "/user/{user_id}",
    tags=["auth"],
    summary="Update a user by ID",
    response_model=UserUpdateSchemaResponse,
)
async def update_user(
    user_id: int,
    data: UserUpdateSchemaRequest,
    user_service: IUserService = Depends(inject_user_service)
):
    data_json = data.model_dump()
    record = user_service.update_user(user_id, data_json)
    return record

@auth_router.get(
    "/user/{user_id}",
    tags=["auth"],
    summary="Get a user by ID",
    response_model=UserListSchemaResponse,
)
async def get_user(
    user_id: int,
    user_service: IUserService = Depends(inject_user_service)
):
    record = user_service.get_user_by_id(user_id)
    return record

@auth_router.post(
    "/user/{user_id}/group/{group_id}",
    tags=["auth"],
    summary="Add a user to a group",
)
async def add_user_to_group(
    user_id: int,
    group_id: int,
    user_service: IUserService = Depends(inject_user_service)
):
    user_service.add_group_to_user(user_id, group_id)
    return {"detail": "User added to group successfully"}