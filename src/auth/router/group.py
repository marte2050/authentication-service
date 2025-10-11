from fastapi import APIRouter, Depends

from auth.dependency import inject_group_service, inject_verify_permission
from auth.schemas.group import (
    GroupAddSchemaRequest,
    GroupAddSchemaResponse,
    GroupListSchemaResponse,
    GroupUpdateSchemaRequest,
    GroupUpdateSchemaResponse,
)
from auth.service.contracts import IGroupService

auth_group_router = APIRouter()


@auth_group_router.post(
    "/groups/",
    tags=["auth"],
    summary="Create a new group",
    response_model=GroupAddSchemaResponse,
)
def create_group(
    group_data: GroupAddSchemaRequest,
    group_service: IGroupService = Depends(inject_group_service),
    user=Depends(inject_verify_permission("create:group")),
):
    data = group_data.model_dump()
    return group_service.create_group(data)


@auth_group_router.delete(
    "/groups/{group_id}",
    tags=["auth"],
    summary="Delete a group by ID",
)
def delete_group(
    group_id: int,
    group_service: IGroupService = Depends(inject_group_service),
    user=Depends(inject_verify_permission("delete:group")),
):
    return group_service.delete_group(group_id)


@auth_group_router.put(
    "/groups/{group_id}",
    tags=["auth"],
    summary="Update a group by ID",
    response_model=GroupUpdateSchemaResponse,
)
def update_group(
    group_id: int,
    group_data: GroupUpdateSchemaRequest,
    group_service: IGroupService = Depends(inject_group_service),
    user=Depends(inject_verify_permission("update:group")),
):
    data = group_data.model_dump()
    return group_service.update_group(group_id, data)


@auth_group_router.get(
    "/groups/{group_id}",
    tags=["auth"],
    summary="Get a group by ID",
    response_model=GroupListSchemaResponse,
)
def get_group(
    group_id: int,
    group_service: IGroupService = Depends(inject_group_service),
    user=Depends(inject_verify_permission("update:group")),
):
    return group_service.get_group_by_id(group_id)


@auth_group_router.post(
    "/group/{group_id}/user/{user_id}",
    tags=["auth"],
    summary="Add a user to a group",
)
def add_user_to_group(
    group_id: int,
    user_id: int,
    group_service: IGroupService = Depends(inject_group_service),
    user=Depends(inject_verify_permission("add_user_to_group:group")),
):
    return group_service.add_user_to_group(group_id, user_id)


@auth_group_router.post(
    "/group/{group_id}/permission/{permission_id}",
    tags=["auth"],
    summary="Add a permission to a group",
)
def add_permission_to_group(
    group_id: int,
    permission_id: int,
    group_service: IGroupService = Depends(inject_group_service),
):
    return group_service.add_permission_to_group(group_id, permission_id)
