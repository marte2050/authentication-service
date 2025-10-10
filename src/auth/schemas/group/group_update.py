
from typing import Optional
from pydantic import BaseModel, Field


class GroupUpdateSchemaResponse(BaseModel):
    name: str
    description: str

class GroupUpdateSchemaRequest(BaseModel):
    name: Optional[str] = Field(
        default=None, 
        min_length=3, 
        max_length=50
    )
    description: Optional[str] = Field(
        default=None, 
        min_length=3, 
        max_length=50
    )