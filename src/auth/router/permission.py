from typing import Annotated

from fastapi import APIRouter, Depends

from auth.dependency import inject_permission_service, inject_verify_permission
from auth.model import Permission, User
from auth.schemas.permission import PermissionAddSchemaRequest, PermissionAddSchemaResponse
from auth.service.contracts import IPermissionService

auth_permission_router = APIRouter()


@auth_permission_router.post(
    "/permissions/",
    tags=["auth"],
    summary="Create a new permission",
    response_model=PermissionAddSchemaResponse,
)
def create_permission(
    data_permission: PermissionAddSchemaRequest,
    permission_service: Annotated[IPermissionService, Depends(inject_permission_service)],
    user: Annotated[User, Depends(inject_verify_permission("create:permission"))],
) -> Permission:
    data = data_permission.model_dump()
    return permission_service.create_permission(data)


@auth_permission_router.delete(
    "/permissions/{permission_id}",
    tags=["auth"],
    summary="Delete a permission by ID",
)
def delete_permission(
    permission_id: int,
    permission_service: Annotated[IPermissionService, Depends(inject_permission_service)],
    user: Annotated[User, Depends(inject_verify_permission("delete:permission"))],
) -> dict:
    return permission_service.delete_permission(permission_id)


@auth_permission_router.get(
    "/permissions/{permission_id}",
    tags=["auth"],
    summary="Get a permission by ID",
    response_model=PermissionAddSchemaResponse,
)
def get_permission_by_id(
    permission_id: int,
    permission_service: Annotated[IPermissionService, Depends(inject_permission_service)],
    user: Annotated[User, Depends(inject_verify_permission("view:permission"))],
) -> Permission:
    return permission_service.get_permission_by_id(permission_id)


@auth_permission_router.put(
    "/permissions/{permission_id}",
    tags=["auth"],
    summary="Update a permission by ID",
    response_model=PermissionAddSchemaResponse,
)
def update_permission(
    permission_id: int,
    data_permission: PermissionAddSchemaRequest,
    permission_service: Annotated[IPermissionService, Depends(inject_permission_service)],
    user: Annotated[User, Depends(inject_verify_permission("update:permission"))],
) -> Permission:
    data = data_permission.model_dump()
    return permission_service.update_permission(permission_id, data)
