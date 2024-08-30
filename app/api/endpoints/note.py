from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.notes import notes_crud
from app.models import Note, User
from app.schemas.notes import NoteBase, NoteCreate
from app.services.spell_checker import check_spelling

router = APIRouter()


@router.get(
    "/",
    response_model=list[NoteBase],
)
async def get_notes_list(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> list[Note]:
    notes = await notes_crud.get_notes_list_by_user(
        user=user,
        session=session
    )
    return notes


@router.post(
    "/",
    response_model=NoteCreate,
)
async def create_note(
        note: NoteCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    spellchecking = check_spelling(note.content)
    if spellchecking:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=spellchecking)
    return await notes_crud.create(note, session=session, user=user)
