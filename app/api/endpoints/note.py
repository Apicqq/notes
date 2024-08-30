from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import ErrConstants as Err
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.notes import notes_crud
from app.models import Note, User
from app.schemas.notes import NoteCreate, NoteGet

router = APIRouter()


@router.get(
    "/",
    response_model=list[NoteGet],
)
async def get_notes_list(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> list[Note]:
    """
    Вывести список заметок пользователя.
    """
    notes = await notes_crud.get_notes_list_by_user(
        user=user,
        session=session
    )
    return notes


@router.post(
    "/",
    response_model=NoteCreate,
    responses={
        400: {"description": "Spelling check failed",
              "content": {
                  "application/json": {
                      "example": {
                          "message": Err.SPELLCHECK_FAILED,
                          "errors": [{"word1": "word", "suggestions":
                              ["suggestion1", "suggestion2"]}]
                      }
                  }
              }
              }
    }
)
async def create_note(
        note: NoteCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> Note:
    """
    Создать новую заметку.
    - **title**: Заголовок заметки — не более 100 символов.
    - **content**: Содержание заметки — не более 255 символов.
    """
    return await notes_crud.create(note, session=session, user=user)
