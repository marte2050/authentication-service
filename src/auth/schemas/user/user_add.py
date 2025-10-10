from pydantic import BaseModel, EmailStr, Field


class UserAddSchemaResponse(BaseModel):
    username: str
    email: EmailStr

class UserAddSchemaRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="The username of the user")
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100, description="The password of the user")