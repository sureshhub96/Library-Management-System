from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(15), nullable=False)

    is_active = Column(Boolean, default=True)

    issues = relationship("Issue", back_populates="member")

    def __repr__(self):
        return f"<Member {self.name}>"