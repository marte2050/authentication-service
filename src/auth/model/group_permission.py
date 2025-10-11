from sqlalchemy import Column, ForeignKey, Integer, Table

from database import table_registry

group_permission = Table(
    "group_permissions",
    table_registry.metadata,
    Column("group_id", Integer, ForeignKey("group.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permission.id"), primary_key=True),
)
