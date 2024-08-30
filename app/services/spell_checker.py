from http import HTTPStatus
from typing import Union

import requests

from app.core.config import settings


def check_spelling(text: str, lang: str = "ru") -> Union[list, bool]:
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
            else:
                return True
        raise ConnectionError
    except (ConnectionError, TimeoutError) as e:
        print(f"Error in check_note_spelling({text}). {e}")
