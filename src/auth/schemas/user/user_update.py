from pydantic import BaseModel, EmailStr, Field


class UserUpdateSchemaResponse(BaseModel):
    username: str
    email: EmailStr


class UserUpdateSchemaRequest(BaseModel):
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="The username of the user",
    )
    email: EmailStr | None
