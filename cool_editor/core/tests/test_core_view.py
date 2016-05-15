import pytest
from flask import url_for
from mock import patch


@pytest.mark.usefixtures('client_class')
class TestCoreView:

    @patch('cool_editor.redis_store')
    def test_get_status_code(self, mock_redis_store):
        mock_redis_store.hset.return_value = True
        response = self.client.get(url_for('core.index'))
        assert response.status_code == 200
