from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.auth.jwt_handler import verify_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Not Found"
        )

    return user


def admin_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.lower() != "admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin Access Required"
        )

    return current_user


def member_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.lower() != "member":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Member Access Required"
        )

    return current_user