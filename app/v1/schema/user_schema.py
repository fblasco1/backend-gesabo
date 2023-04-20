from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@gesabo.com"
    )
    usuario: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="SoyPepito"
    )


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )
    tipo: str = Field(
        ...,
        example="Admin"
    )


class UserRegister(UserBase):
    contrasenia: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )