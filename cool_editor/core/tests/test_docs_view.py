import pytest
from flask import url_for
from mock import patch


@pytest.mark.usefixtures('client_class')
class TestDocsView:

    @patch('cool_editor.redis_store')
    def test_get_found_doc(self, mock_redis_store):
        mock_redis_store.hgetall.return_value = {'status': 'created'}
        response = self.client.get(url_for('core.docs', hashkey='Rafael123'))
        assert response.status_code == 200

    @patch('cool_editor.redis_store')
    def test_get_not_found_doc(self, mock_redis_store):
        mock_redis_store.hgetall.return_value = {}
        response = self.client.get(url_for('core.docs', hashkey='Rafael123'))
        assert response.status_code == 404

    @patch('cool_editor.redis_store')
    def test_get_doc_content(self, mock_redis_store):
        mock_redis_store.hgetall.return_value = {'status': 'created'}
        response = self.client.get(url_for('core.docs', hashkey='Rafael123'))
        assert response.json == {'status': 'created'}

    @patch('cool_editor.redis_store')
    def test_put_doc(self, mock_redis_store):
        mock_redis_store.hset.return_value = True
        payload = {'key': 0, 'value': 'print("hello world")'}
        url = url_for('core.docs', hashkey='Rafael123')
        response = self.client.put(url, data=payload)
        assert response.status_code == 200

    @patch('cool_editor.redis_store')
    def test_put_doc_content(self, mock_redis_store):
        mock_redis_store.hset.return_value = True
        payload = {'key': 0, 'value': 'print("hello world")'}
        url = url_for('core.docs', hashkey='Rafael123')
        response = self.client.put(url, data=payload)
        assert response.json == {'Rafael123': {'0': 'print("hello world")'}}

    def test_put_bad_request(self):
        payload = {'value': 'print("hello world")'}
        url = url_for('core.docs', hashkey='Rafael123')
        response = self.client.put(url, data=payload)
        assert response.status_code == 400
