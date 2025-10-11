from pydantic import BaseModel


class UserListSchemaResponse(BaseModel):
    username: str
    email: str
