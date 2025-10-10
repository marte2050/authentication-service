from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import create_session
from auth.service.contracts import IPermissionService
from auth.service import PermissionService
from auth.repository import GroupRepository, PermissionRepository
from auth.schemas.permission import PermissionAddSchemaRequest, PermissionAddSchemaResponse

auth_permission_router = APIRouter()

def inject_permission_service(session: Session = Depends(create_session)) -> IPermissionService:
    return PermissionService(
        session=session,
        permission_repository=PermissionRepository,
        group_repository=GroupRepository
    )

@auth_permission_router.post(
    "/permissions/", 
    tags=["auth"], 
    summary="Create a new permission",
    response_model=PermissionAddSchemaResponse
)
def create_permission(
    data_permission: PermissionAddSchemaRequest,
    permission_service: IPermissionService = Depends(inject_permission_service),
):
    data = data_permission.model_dump()
    return permission_service.create_permission(data)

@auth_permission_router.delete(
    "/permissions/{permission_id}", 
    tags=["auth"], 
    summary="Delete a permission by ID"
)
def delete_permission(
    permission_id: int,
    permission_service: IPermissionService = Depends(inject_permission_service),
):
    return permission_service.delete_permission(permission_id)

@auth_permission_router.get(
    "/permissions/{permission_id}", 
    tags=["auth"], 
    summary="Get a permission by ID",
    response_model=PermissionAddSchemaResponse
)
def get_permission_by_id(
    permission_id: int,
    permission_service: IPermissionService = Depends(inject_permission_service),
):
    return permission_service.get_permission_by_id(permission_id)

@auth_permission_router.put(
    "/permissions/{permission_id}", 
    tags=["auth"], 
    summary="Update a permission by ID",
    response_model=PermissionAddSchemaResponse
)
def update_permission(
    permission_id: int,
    data_permission: PermissionAddSchemaRequest,
    permission_service: IPermissionService = Depends(inject_permission_service),
):
    data = data_permission.model_dump()
    return permission_service.update_permission(permission_id, data)
