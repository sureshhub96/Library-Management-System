from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.member import Member
from app.schemas.member import MemberCreate


def create_member(member: MemberCreate, db: Session):

    existing = db.query(Member).filter(
        Member.email == member.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_member = Member(**member.model_dump())

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return new_member


def get_members(db: Session):
    return db.query(Member).all()


def get_member(member_id: int, db: Session):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    return member