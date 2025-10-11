from pydantic import BaseModel, Field


class GroupAddSchemaResponse(BaseModel):
    name: str
    description: str


class GroupAddSchemaRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
