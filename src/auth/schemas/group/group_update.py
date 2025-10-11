from pydantic import BaseModel, Field


class GroupUpdateSchemaResponse(BaseModel):
    name: str
    description: str


class GroupUpdateSchemaRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
    )
    description: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
    )
