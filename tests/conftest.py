from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def activities_snapshot():
    original_state = deepcopy(activities)

    yield

    activities.clear()
    activities.update(original_state)
