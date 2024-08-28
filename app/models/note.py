from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import *


class Note(Base):
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(255))
    author: Mapped["User"] = relationship(back_populates="notes")
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
