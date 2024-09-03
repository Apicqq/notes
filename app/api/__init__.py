from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import User

UserDependency = Annotated[User, Depends(current_user)]
SessionDependency = Annotated[AsyncSession, Depends(get_async_session)]
