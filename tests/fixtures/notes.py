import pytest


@pytest.fixture
def note(mixer):
    return mixer.blend(
        "app.models.note.Note",
        author_id=1
    )


@pytest.fixture
def notes_list(mixer):
    return mixer.cycle(2).blend(
        "app.models.note.Note",
        author_id=1,
        title="Заголовок заметки",
        content="Содержание заметки",
    )
