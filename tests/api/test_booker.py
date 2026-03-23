import pytest
import allure


@allure.epic("Booking API")
@allure.feature("Health Check")
@allure.story("API availability")
@allure.title("Health check — API returns 200")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_health_check(booker_client):
    """Позитивный тест для проверки что API жив"""
    response = booker_client.get_bookings()
    assert response.status_code == 200


@allure.epic("Booking API")
@allure.feature("Bookings")
@allure.story("Create booking")
@allure.title("Create a new booking")
@allure.severity(allure.severity_level.NORMAL)
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


@allure.epic("Booking API")
@allure.feature("Bookings")
@allure.story("Get bookings")
@allure.title("Get list of all bookings")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_bookings(booker_client):
    """Позитивный тест для получения списка бронирований"""
    response = booker_client.get_bookings()
    assert response.status_code == 200


@allure.epic("Booking API")
@allure.feature("Bookings")
@allure.story("Get booking by ID")
@allure.title("Get booking by ID — verify firstname and lastname")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking(booker_client, create_booking):
    """Позитивный тест для получения информации о конкретном бронировании. Сначала создадим бронирование."""
    booking_id = create_booking(firstname="Read", lastname="Test")
    response = booker_client.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Read"
    assert response.json()["lastname"] == "Test"


@allure.epic("Booking API")
@allure.feature("Bookings")
@allure.story("Delete booking")
@allure.title("Delete an existing booking")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_delete_booking(booker_client, create_booking):
    """Позитивный тест для удаления бронирования"""
    booking_id = create_booking(firstname="Delete", lastname="Me")
    response = booker_client.delete_booking(booking_id)
    assert response.status_code == 201


@allure.epic("Booking API")
@allure.feature("Bookings")
@allure.story("Get booking by ID")
@allure.title("Get nonexistent booking — expect 404")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.negative
def test_get_nonexistent_booking(booker_client):
    """Негативный тест для получения несуществующего бронирования"""
    booking_id = 999942142121  # Предположительно несуществующий ID
    response = booker_client.get_booking(booking_id)
    assert response.status_code == 404
