def test_create_booking_empty_body(booker_client):
    """Создание бронирования с пустым телом"""
    response = booker_client.post("/booking", json={})
    assert response.status_code == 500


def test_create_booking_missing_firstname(booking_client):
    """Создание бронирования без обязательного поля (firstname)"""
    response = booking_client.post("/booking", json={"lastname": "Doe"})
    assert response.status_code == 500


def test_update_without_auth(booking_client, create_booking):
    """Обновление бронирования без авторизации"""
    booking_id = create_booking()

    response = booking_client.put(f"/booking/{booking_id}", json={
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
    })

    assert response.status_code == 403


def test_delete_nonexistent_booking(booker_client):
    """Удаление несуществующего бронирования"""
    response = booker_client.delete("/booking/999999999")
    assert response.status_code == 405


def test_full_crud_lifecycle(booker_client):
    """Полный lifecycle в одном тесте"""
    # 1. CREATE → проверь 200, сохрани id
    response = booker_client.post("/booking", json={
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
    })
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")

    # 2. READ → проверь данные совпадают
    response = booker_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json().get("firstname") == "John"
    assert response.json().get("lastname") == "Doe"
    assert response.json().get("totalprice") == 100
    assert response.json().get("depositpaid") is True

    # 3. UPDATE → измени firstname и totalprice
    response = booker_client.put(f"/booking/{booking_id}", json={
        "firstname": "Jane",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
    })
    assert response.status_code == 200

    # 4. READ → проверь что обновилось
    response = booker_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json().get("firstname") == "Jane"
    assert response.json().get("totalprice") == 150

    # 5. DELETE → проверь 201
    response = booker_client.delete(f"/booking/{booking_id}")
    assert response.status_code == 201

    # 6. READ → проверь 404
    response = booker_client.get(f"/booking/{booking_id}")
    assert response.status_code == 404
