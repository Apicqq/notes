from pydantic import BaseModel, Field, field_validator

from app.core.exceptions import SpellingCheckException
from app.services.spell_checker import check_spelling


class NoteBase(BaseModel):
    """
    Базовая схема для заметки.
    """

    title: str = Field(None, title="Заголовок заметки", max_length=100)
    content: str = Field(
        None,
        title="Содержание заметки",
        max_length=255,
    )


class NoteCreate(NoteBase):
    """
    Схема для создания заметок. Включает в себя валидацию правописания.
    """

    @field_validator("content")
    @classmethod
    def spellcheck_note_content(cls, value: str) -> str:
        spellcheck = check_spelling(value)
        if spellcheck:
            raise SpellingCheckException(spellcheck)
        return value


class NoteGet(NoteBase):
    id: int


class NoteUpdate(NoteBase):
    pass
