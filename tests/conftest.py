import os

import pytest
from fastapi.testclient import TestClient
import app
from config.config import TestConfig, Settings


def pytest_generate_tests():
    os.environ["ENV"] = "test"


@pytest.fixture(scope="module")
def test_client():
    app.app.dependency_overrides[Settings] = TestConfig
    with TestClient(app.app) as client:
        yield client
