from sqlalchemy.orm import Session

from app.models.user import User


def get_users(db: Session):
    return db.query(User).all()


def get_user(user_id: int, db: Session):
    return db.query(User).filter(
        User.id == user_id
    ).first()