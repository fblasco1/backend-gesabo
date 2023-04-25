from pydantic import Field, BaseModel

class Jurisdiccion(BaseModel):
    id: int = Field(...)
    provincia: str = Field(...)
    sede: str = Field(...)