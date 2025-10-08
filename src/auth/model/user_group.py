from database import table_registry
from sqlalchemy import Column, ForeignKey, Integer, Table


user_group = Table(
    "user_groups",
    table_registry.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("group.id"), primary_key=True)
)