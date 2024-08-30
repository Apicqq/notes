import pytest
from fastapi.testclient import TestClient

from app.models.user import User
from tests.conftest import app, get_async_session, current_user, \
    get_async_testing_session

user = User(
    id=1,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)

second_user = User(
    id=2,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)

@pytest.fixture
def user_client():
    app.dependency_overrides = {get_async_session: get_async_testing_session,
                                current_user: lambda: user}
    with TestClient(app) as client:
        yield client

@pytest.fixture
def another_user_client():
    app.dependency_overrides = {get_async_session: get_async_testing_session,
                                current_user: lambda: second_user}
    with TestClient(app) as client:
        yield client