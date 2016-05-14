import pytest
from cool_editor import create_app
from cool_editor.config import test_config


@pytest.fixture
def app():
    app = create_app(test_config)
    return app
