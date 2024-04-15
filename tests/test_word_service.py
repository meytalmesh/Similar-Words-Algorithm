import pytest
from services.word_service import app


@pytest.fixture(name='testapp')
def _test_app():
    return app


@pytest.mark.asyncio
async def test_similar_endpoint_returns_right_values(testapp):
    client = testapp.test_client()
    response = await client.get('/api/v1/similar?word=cat')
    assert response.status_code == 200
    assert await response.json == {'similar': ['act']}


@pytest.mark.asyncio
async def test_similar_endpoint_post_not_implemented(testapp):
    client = testapp.test_client()
    response = await client.post('/api/v1/similar?word=cat')
    assert response.status_code == 405
    assert await response.data == (b'<!doctype html>\n<html lang=en>\n<title>405 Method Not Allowed</title>\n<h1'
                                   b'>Method Not Allowed</h1>\n<p>The method is not allowed for the requested '
                                   b'URL.</p>\n')


@pytest.mark.asyncio
async def test_similar_endpoint_returns_right_values(testapp):
    client = testapp.test_client()
    response = await client.get('/api/v1/similar?word=moshiko')
    assert response.status_code == 404
    assert await response.json == {'error': 'Word not found in the dictionary'}