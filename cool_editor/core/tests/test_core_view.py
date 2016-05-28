import pytest
from flask import url_for
from mock import patch

from cool_editor.core.tests.test_utils import count_words


@pytest.mark.usefixtures('client_class')
class TestCoreView:

    @patch('cool_editor.redis_store')
    def test_get_status_code(self, mock_redis_store):
        mock_redis_store.hset.return_value = True
        response = self.client.get(url_for('core.index'))
        assert response.status_code == 302

    @patch('cool_editor.redis_store')
    @patch('cool_editor.core.views.id_generator')
    def test_return_correct_url_hash(self, mock_id_generator,
                                     mock_redis_store):
        mock_id_generator.return_value = "Rafael1234"
        mock_redis_store.hset.return_value = True
        response = self.client.get(url_for('core.index'))
        expected_url = url_for('core.editor', hashkey="Rafael1234")
        assert expected_url in response.location

    # pseudo acceptance test
    @patch('cool_editor.redis_store')
    @patch('cool_editor.core.views.id_generator')
    def test_html(self, mock_id_generator, mock_redis_store):
        mock_id_generator.return_value = "Rafael1234"
        mock_redis_store.hset.return_value = True
        url = url_for('core.editor', hashkey="Rafael1234")
        response = self.client.get(url)
        tags = (
            ('<title>', 1),
            ('<label for="code-editor">', 1),
            ('<button id="show".*</button>', 1),
            ('<textarea id="code-editor".*</textarea>', 1),
            ('<script src="/static/js/jquery.min.js"></script>', 1),
            ('<script src="/static/js/bootstrap.min.js"></script>', 1),
            ('<script src="/core/js/code-editor.js"></script>', 1),
            ('<link href="/static/css/bootstrap.min.css".*>', 1),
            ('<link href="/static/css/bootstrap-theme.min.css".*>', 1),
            ('<meta name="csrf-token"', 1),
        )
        content = response.data.decode('utf-8')
        for text, count in tags:
            assert count_words(text, content) == count
