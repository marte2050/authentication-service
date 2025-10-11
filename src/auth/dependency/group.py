from fastapi import Depends
from sqlalchemy.orm import Session
from database import create_session
from auth.service.contracts import IGroupService
from auth.service import GroupService
from auth.repository import PermissionRepository, GroupRepository


def inject_group_service(session: Session = Depends(create_session)) -> IGroupService:
    return GroupService(
        session=session,
        group_repository=GroupRepository,
        permission_repository=PermissionRepository
    )