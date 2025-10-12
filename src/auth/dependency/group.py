from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from auth.repository import GroupRepository, PermissionRepository
from auth.service import GroupService
from auth.service.contracts import IGroupService
from database import create_session


def inject_group_service(session: Annotated[Session, Depends(create_session)]) -> IGroupService:
    return GroupService(
        session=session,
        group_repository=GroupRepository,
        permission_repository=PermissionRepository,
    )
