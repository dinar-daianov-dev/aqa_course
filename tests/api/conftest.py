import pytest
from src.clients.booker_client import BookerClient
from src.utils.logger import setup_logging

@pytest.fixture(scope="session")
def booking_client():
    """Клиент БЕЗ авторизации — для негативных тестов."""
    return BookerClient("https://restful-booker.herokuapp.com")


@pytest.fixture(scope="session")
def booker_client():
    """Создает клиента и вызывает authenticate()."""
    client = BookerClient("https://restful-booker.herokuapp.com")
    client.authenticate()
    return client

@pytest.fixture
def create_booking(booker_client):
    """Фабрика: создает бронирование, после теста удаляет."""
    created_ids = []

    def _create(**overrides):
        data = {
            "firstname": "Test",
            "lastname": "User",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-02"
            },
        }
        data.update(overrides)
        response = booker_client.create_booking(data)
        booking_id = response.json()["bookingid"]
        created_ids.append(booking_id)
        return booking_id

    yield _create

    for booking_id in created_ids:
        try:
            booker_client.delete_booking(booking_id)
        except Exception:
            pass

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging("INFO")