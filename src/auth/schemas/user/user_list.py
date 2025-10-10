from typing import Optional
from pydantic import BaseModel, Field


class UserListSchemaResponse(BaseModel):
    username: str
    email: str