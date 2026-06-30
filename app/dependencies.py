from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.oauth2 import (
    get_current_user,
    admin_required,
    member_required
)


# Database Dependency
def get_database() -> Session:
    return Depends(get_db)


# Logged-in User Dependency
def get_logged_in_user():
    return Depends(get_current_user)


# Admin Only Dependency
def get_admin():
    return Depends(admin_required)


# Member Only Dependency
def get_member():
    return Depends(member_required)