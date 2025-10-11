from pydantic import BaseModel, Field


class PermissionAddSchemaResponse(BaseModel):
    name: str
    description: str


class PermissionAddSchemaRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
