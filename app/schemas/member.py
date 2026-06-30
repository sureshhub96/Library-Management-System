from pydantic import BaseModel, EmailStr, ConfigDict, Field


class MemberCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(
        pattern=r"^[6-9]\d{9}$",
        description="10-digit Indian mobile number"
    )


class MemberResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)