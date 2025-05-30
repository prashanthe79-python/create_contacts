from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    country: str
    message: str | None = None

