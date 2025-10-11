from pydantic import BaseModel


class GroupListSchemaResponse(BaseModel):
    name: str
    description: str
