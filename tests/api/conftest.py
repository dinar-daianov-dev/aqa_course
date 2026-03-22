import pytest
from src.clients.booker_client import BookerClient

@pytest.fixture(scope="session")
def booker_client():
    """Создает клиента и вызывает authenticate()."""
    client = BookerClient("https://restful-booker.herokuapp.com")
    client.authenticate()
    return client