from datetime import date
from pydantic import BaseModel, ConfigDict


class IssueCreate(BaseModel):
    member_id: int
    book_id: int


class ReturnBook(BaseModel):
    return_date: date


class IssueResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    issue_date: date
    return_date: date | None = None
    is_returned: bool

    model_config = ConfigDict(from_attributes=True)