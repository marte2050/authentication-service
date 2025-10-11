from fastapi import APIRouter, Depends

from auth.dependency import inject_user_service, inject_verify_permission
from auth.model import User
from auth.schemas import (
    UserAddSchemaRequest,
    UserAddSchemaResponse,
    UserListSchemaResponse,
    UserUpdateSchemaRequest,
    UserUpdateSchemaResponse,
)
from auth.service.contracts import IUserService

auth_router = APIRouter()


@auth_router.post(
    "/user/",
    tags=["auth"],
    summary="Create a new user",
    response_model=UserAddSchemaResponse,
)
async def add_user(
    data: UserAddSchemaRequest,
    user_service: IUserService = Depends(inject_user_service),
    user: User = Depends(inject_verify_permission("create:user")),
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
    user_service: IUserService = Depends(inject_user_service),
    user: User = Depends(inject_verify_permission("delete:user")),
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
    user_service: IUserService = Depends(inject_user_service),
    user: User = Depends(inject_verify_permission("update:user")),
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
    user_service: IUserService = Depends(inject_user_service),
    user: User = Depends(inject_verify_permission("view:user")),
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
    user_service: IUserService = Depends(inject_user_service),
    user: User = Depends(inject_verify_permission("add_user_to_group:user")),
):
    user_service.add_group_to_user(user_id, group_id)
    return {"detail": "User added to group successfully"}
