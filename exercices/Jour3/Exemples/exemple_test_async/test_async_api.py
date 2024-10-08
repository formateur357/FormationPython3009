import pytest
from unittest.mock import AsyncMock, patch

from async_api import fetch_data

@pytest.mark.asyncio
@patch('async_api.aiohttp.ClientSession')
async def test_fetch_data_success(mock_session):
    # Configure le mock pour renvoyer une reponse avec statut 200
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json.return_valiue = {'key': 'value'}

    mock_get = AsyncMock()
    mock_get.__aenter__.return_value = mock_response
    mock_session.return_value.__aenter__.return_value.get.return_value = mock_get

    data = await fetch_data('hhtp://exemple.com')
    assert data == {'key': 'value'}


@pytest.mark.asyncio
@patch("async_api.aiohttp.ClientSession")
async def test_fetch_data_failure(mock_session):
    # Configurer le mock pour renvoyer une réponse avec statut 404
    mock_response = AsyncMock()
    mock_response.status = 404

    mock_get = AsyncMock()
    mock_get.__aenter__.return_value = mock_response
    mock_session.return_value.__aenter__.return_value.get.return_value = mock_get

    data = await fetch_data("http://example.com")
    assert data is None
