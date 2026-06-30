from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


def create_book(book: BookCreate, db: Session):

    existing = db.query(Book).filter(
        Book.isbn == book.isbn
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="ISBN already exists"
        )

    new_book = Book(**book.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def get_books(
        db: Session,
        search: str = None,
        category: str = None,
        page: int = 1,
        limit: int = 10
):

    query = db.query(Book).filter(
        Book.is_deleted == False
    )

    if search:
        query = query.filter(
            or_(
                Book.title.ilike(f"%{search}%"),
                Book.author.ilike(f"%{search}%")
            )
        )

    if category:
        query = query.filter(
            Book.category == category
        )

    return query.offset(
        (page - 1) * limit
    ).limit(limit).all()


def get_book(book_id: int, db: Session):

    book = db.query(Book).filter(
        Book.id == book_id,
        Book.is_deleted == False
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    return book


def update_book(
        book_id: int,
        data: BookUpdate,
        db: Session
):

    book = get_book(book_id, db)

    for key, value in data.model_dump().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)

    return book


def delete_book(book_id: int, db: Session):

    book = get_book(book_id, db)

    book.is_deleted = True

    db.commit()

    return {
        "message": "Book Deleted Successfully"
    }