import pytest
from cool_editor import create_app
from cool_editor.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
