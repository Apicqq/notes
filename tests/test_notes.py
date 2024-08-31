import pytest

NOTES_URL = "/notes"


def test_notes_list(notes_list, user_client):
    response = user_client.get(NOTES_URL)
    assert response.status_code == 200, (
        "GET-запрос зарегистрированного пользователя к эндпоинту "
        f" {NOTES_URL} должен вернуть ответ со статус-кодом 200."
    )
    response_data = response.json()
    assert len(response_data) == 2, (
        "В ответе на GET-запрос зарегистрированного пользователя к эндпоинту "
        f"`{NOTES_URL}` должны быть только заметки пользователя, "
        "сделавшего запрос."
    )
    assert isinstance(response_data, list), (
        "В ответ на GET-запрос зарегистрированного пользователя к эндпоинту "
        f"`{NOTES_URL}` должен возвращаться список заметок "
        "пользователя (объект типа `list`)."
    )


def test_notes_list_by_different_user(another_user_client, notes_list):
    response = another_user_client.get(NOTES_URL)
    assert response.status_code == 200, (
        "GET-запрос зарегистрированного пользователя к эндпоинту "
        f" {NOTES_URL} должен вернуть ответ со статус-кодом 200."
    )
    response_data = response.json()
    assert len(response_data) == 0, (
        "В ответе на GET-запрос зарегистрированного пользователя к эндпоинту "
        f"`{NOTES_URL}` должны быть только заметки пользователя, "
        "сделавшего запрос."
    )


@pytest.mark.parametrize(
    "json_data",
    [
        {"title": "Заголовок заметки", "content": "Содержание заметки"},
    ],
)
def test_notes_create_valid_data(user_client, json_data):
    response = user_client.post("/notes", json=json_data)
    assert response.status_code == 200, (
        "Корректный POST-запрос зарегистрированного пользователя к эндпоинту "
        f"`{NOTES_URL}` должен возвращать ответ со статус-кодом 200."
    )


@pytest.mark.parametrize(
    "json_data",
    [
        {"title": "Заголовок заметки", "content": "Текст с ашибками"},
    ],
)
def test_notes_spellchecking_validation(user_client, json_data):
    response = user_client.post("/notes", json=json_data)
    assert response.status_code == 400, (
        "POST-запрос зарегистрированного пользователя к эндпоинту "
        f"`{NOTES_URL}`, содержащий ошибки правописания, "
        f"должен возвращать ответ со статус-кодом 400."
    )


@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        (
            {
                "title": "Очень длинная заметка" * 100,
                "content": "Содержание заметки",
            },
            422,
        ),
        (
            {
                "title": "Заголовок заметки",
                "content": "Очень длинная заметка" * 100,
            },
            422,
        ),
    ],
)
def test_notes_length_validation(user_client, data, expected_status_code):
    response = user_client.post("/notes", json=data)
    assert response.status_code == expected_status_code, (
        "Некорректный POST-запрос зарегистрированного пользователя"
        " к эндпоинту `{NOTES_URL}` должен возвращать ответ со статус-кодом "
        f"{expected_status_code}"
    )
