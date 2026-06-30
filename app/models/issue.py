from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(Integer, ForeignKey("members.id"))

    book_id = Column(Integer, ForeignKey("books.id"))

    issue_date = Column(Date, nullable=False)

    return_date = Column(Date, nullable=True)

    is_returned = Column(Boolean, default=False)

    member = relationship("Member", back_populates="issues")

    book = relationship("Book")

    def __repr__(self):
        return f"<Issue Member:{self.member_id} Book:{self.book_id}>"