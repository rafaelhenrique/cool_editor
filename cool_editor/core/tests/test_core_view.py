import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestCoreView:

    def test_get_status_code(self):
        response = self.client.get(url_for('core.index'))
        assert response.status_code == 200
