from http import HTTPStatus

import requests

from app.core.config import settings


def check_spelling(text: str, lang: str = "ru, en") -> list[dict[str, str]] | bool:
    errors = list()
    try:
        payload = dict(
            text=text,
            lang=lang
        )
        request = requests.post(
            settings.ya_spellcheck_address,
            data=payload
        )
        if request.status_code == HTTPStatus.OK:
            if request.json():
                for error in request.json():
                    errors.append(
                        dict(
                            word=error["word"],
                            suggestions=error["s"]
                        )
                    )
                return errors
        raise ConnectionError
    except (ConnectionError, TimeoutError) as e:
        return False
