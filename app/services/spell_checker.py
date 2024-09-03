from http import HTTPStatus

import requests
from requests.exceptions import ConnectionError

from app.core.config import settings


def check_spelling(
    text: str, lang: str = "ru, en"
) -> list[dict[str, str]] | bool:
    """
    Проверка орфографии в тексте заметки.

    Для осуществления проверки отправляется запрос на эндпоинт Яндекса,
    после чего полученный ответ парсится в список ошибок и возвращается
    пользователю.
    :param text: Текст заметки.
    :param lang: Язык текста, по умолчанию русский и английский.
    """
    errors = list()
    try:
        payload = dict(text=text, lang=lang)
        request = requests.post(settings.ya_spellcheck_address, data=payload)
        if request.status_code == HTTPStatus.OK:
            if request.json():
                for error in request.json():
                    errors.append(
                        dict(word=error["word"], suggestions=error["s"])
                    )
                return errors
        raise ConnectionError
    except (ConnectionError, TimeoutError):
        return False  # в случае, если сервис яндекса недоступен, пропускаем
    # валидацию
