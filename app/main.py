from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.constants import ErrConstants as Err
from app.api.routers import main_router
from app.core.exceptions import SpellingCheckException

app = FastAPI(
    docs_url="/swagger",
)

app.include_router(main_router)


@app.exception_handler(SpellingCheckException)
async def spellcheck_exception_handler(
    request: Request, exc: SpellingCheckException
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content=dict(
            message=Err.SPELLCHECK_FAILED,
            errors=str(exc),
        ),
    )


@app.get("/")
async def root() -> dict:
    return {"message": "please refer to /redoc or /swagger for documentation"}
