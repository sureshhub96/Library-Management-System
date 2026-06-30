from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    isbn: str
    total_copies: int
    available_copies: int


class BookUpdate(BaseModel):
    title: str
    author: str
    category: str
    isbn: str
    total_copies: int
    available_copies: int


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    category: str
    isbn: str
    total_copies: int
    available_copies: int
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)