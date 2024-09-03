from fastapi import APIRouter, status
from fastapi_pagination import LimitOffsetPage, Page

from app.api import UserDependency, SessionDependency
from app.core.constants import ErrConstants as Err
from app.crud.notes import notes_crud
from app.models import Note
from app.schemas.notes import NoteCreate, NoteGet
from app.schemas.spelling import SpellingCheckFailedResponse

router = APIRouter()


@router.get(
    "/",
    response_model=Page[NoteGet],
)
@router.get(
    "/limit-offset",
    response_model=LimitOffsetPage[NoteGet],
)
async def get_notes_list(
    session: SessionDependency,
    user: UserDependency,
) -> list[Note]:
    """
    Вывести список заметок пользователя.
    """
    notes = await notes_crud.get_notes_list_by_user(user=user, session=session)
    return notes


@router.post(
    "/",
    response_model=NoteCreate,
    responses={
        status.HTTP_400_BAD_REQUEST: dict(
            description=Err.SPELLCHECK_FAILED_SHORT,
            model=SpellingCheckFailedResponse,
        )
    },
)
async def create_note(
    note: NoteCreate,
    session: SessionDependency,
    user: UserDependency,
) -> Note:
    """
    Создать новую заметку.
    - **title**: Заголовок заметки — не более 100 символов.
    - **content**: Содержание заметки — не более 255 символов.
    """
    return await notes_crud.create(note, session=session, user=user)
