from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base import User
from app.crud.base import CRUDBase
from app.models.note import Note
from app.schemas.notes import NoteCreate, NoteUpdate


class CRUDNotes(CRUDBase[Note, NoteCreate, NoteUpdate]):
    @staticmethod
    async def get_notes_list_by_user(user: User, session: AsyncSession):
        """
        Получить список заметок пользователя.
        """
        notes = await session.execute(
            select(Note).where(Note.author_id == user.id)
        )
        return notes.scalars().all()


notes_crud = CRUDNotes(Note)
