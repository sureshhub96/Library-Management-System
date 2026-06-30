from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.book import BookCreate, BookUpdate
from app.services.book_service import (
    create_book,
    get_books,
    get_book,
    update_book,
    delete_book
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post("/")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return create_book(book, db)


@router.get("/")
def list_books(
    search: str = None,
    category: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_books(
        db,
        search,
        category,
        page,
        limit
    )


@router.get("/{book_id}")
def get_single_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return get_book(book_id, db)


@router.put("/{book_id}")
def edit_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db)
):
    return update_book(book_id, book, db)


@router.delete("/{book_id}")
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return delete_book(book_id, db)