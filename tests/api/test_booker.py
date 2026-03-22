import pytest

@pytest.mark.smoke
def test_health_check(booker_client):
    """Позитивный тест для проверки что API жив"""
    response = booker_client.get_bookings()
    assert response.status_code == 200

@pytest.mark.regression
def test_create_booking(booker_client):
    """Позитивный тест для создания бронирования"""
    booking_data = {
    "firstname": "Dinar",
    "lastname": "Dayanov",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-06-01",
        "checkout": "2024-06-10"
    },
    "additionalneeds": "Breakfast"
}
    response = booker_client.create_booking(booking_data)
    assert response.status_code == 200

@pytest.mark.regression
def test_get_bookings(booker_client):
    """Позитивный тест для получения списка бронирований"""
    response = booker_client.get_bookings()
    assert response.status_code == 200

@pytest.mark.regression
def test_get_booking(booker_client):
    """Позитивный тест для получения информации о конкретном бронировании. Сначала создадим бронирование."""
    data = {
    "firstname": "Test",
    "lastname": "User",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-01-02"
    },
    "additionalneeds": "None"
    }
    create_resp = booker_client.create_booking(data)
    booking_id = create_resp.json()["bookingid"]
    response = booker_client.get_booking(booking_id)
    assert response.status_code == 200

@pytest.mark.regression
def test_delete_booking(booker_client):
    """Позитивный тест для удаления бронирования"""
    data = {
        "firstname": "Delete",
        "lastname": "Me",
        "totalprice": 50,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": ""
    }
    create_resp = booker_client.create_booking(data)
    booking_id = create_resp.json()["bookingid"]
    response = booker_client.delete_booking(booking_id)
    assert response.status_code == 201

@pytest.mark.negative
def test_get_nonexistent_booking(booker_client):
    """Негативный тест для получения несуществующего бронирования"""
    booking_id = 999942142121  # Предположительно несуществующий ID
    response = booker_client.get_booking(booking_id)
    assert response.status_code == 404
