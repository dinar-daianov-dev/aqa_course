import pytest

from src.clients.chuck_norris_client import ChuckNorrisClient

@pytest.fixture(scope="session")
def chuck_norris_client():
    """Один клиент на все тесты - переиспользует соединение."""
    client = ChuckNorrisClient()
    yield client
    client.close()