from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.issue import IssueCreate
from app.services.issue_service import (
    issue_book,
    return_book,
    get_member_books
)

router = APIRouter(
    tags=["Book Issue"]
)


@router.post("/issues")
def issue(
    issue_data: IssueCreate,
    db: Session = Depends(get_db)
):
    return issue_book(issue_data, db)


@router.put("/returns/{issue_id}")
def return_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    return return_book(issue_id, db)


@router.get("/members/{member_id}/books")
def member_books(
    member_id: int,
    db: Session = Depends(get_db)
):
    return get_member_books(member_id, db)