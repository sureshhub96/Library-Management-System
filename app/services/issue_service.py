from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.issue import Issue
from app.models.book import Book
from app.models.member import Member
from app.schemas.issue import IssueCreate


def issue_book(data: IssueCreate, db: Session):

    member = db.query(Member).filter(
        Member.id == data.member_id
    ).first()

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    book = db.query(Book).filter(
        Book.id == data.book_id,
        Book.is_deleted == False
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    if book.available_copies <= 0:
        raise HTTPException(
            status_code=400,
            detail="Book Not Available"
        )

    duplicate = db.query(Issue).filter(
        Issue.member_id == data.member_id,
        Issue.book_id == data.book_id,
        Issue.is_returned == False
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=400,
            detail="Book already issued to this member"
        )

    issue = Issue(
        member_id=data.member_id,
        book_id=data.book_id,
        issue_date=date.today(),
        is_returned=False
    )

    book.available_copies -= 1

    db.add(issue)

    db.commit()

    db.refresh(issue)

    return issue


def return_book(issue_id: int, db: Session):

    issue = db.query(Issue).filter(
        Issue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue Not Found"
        )

    if issue.is_returned:
        raise HTTPException(
            status_code=400,
            detail="Book Already Returned"
        )

    issue.is_returned = True
    issue.return_date = date.today()

    book = db.query(Book).filter(
        Book.id == issue.book_id
    ).first()

    book.available_copies += 1

    db.commit()

    return {
        "message": "Book Returned Successfully"
    }


def get_member_books(member_id: int, db: Session):

    return db.query(Issue).filter(
        Issue.member_id == member_id,
        Issue.is_returned == False
    ).all()