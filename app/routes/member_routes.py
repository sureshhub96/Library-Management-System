from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.member import MemberCreate
from app.services.member_service import (
    create_member,
    get_members,
    get_member
)

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


@router.post("/")
def add_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):
    return create_member(member, db)


@router.get("/")
def list_members(
    db: Session = Depends(get_db)
):
    return get_members(db)


@router.get("/{member_id}")
def member_details(
    member_id: int,
    db: Session = Depends(get_db)
):
    return get_member(member_id, db)