from pydantic import BaseModel


class SpellingError(BaseModel):
    word: str
    suggestions: list[str]


class SpellingCheckFailedResponse(BaseModel):
    message: str
    errors: list[SpellingError]
