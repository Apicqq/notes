from contextlib import asynccontextmanager, AbstractAsyncContextManager
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from app.api.routers import main_router
from app.core.constants import ErrConstants as Err
from app.core.exceptions import SpellingCheckException
from app.core.init_db import create_first_superuser


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager:
    await create_first_superuser()
    yield


app = FastAPI(
    docs_url="/swagger",
    lifespan=lifespan,
)
add_pagination(app)
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
