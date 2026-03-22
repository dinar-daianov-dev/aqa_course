from src.clients.base_client import BaseApiClient


class BookerClient(BaseApiClient):
    base_url: str = "https://restful-booker.herokuapp.com"
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def authenticate(self, username="admin", password="password123") -> str:
        """Логин admin пароль password123 Сохраняет token в cookies сессии."""
        response = self.session.post(f"{self.base_url}/auth", json={
            "username": username,
            "password": password
        })
        token = response.json().get("token")
        self.session.cookies.set("token", token)
        return token
    
    def get_bookings(self) -> list:
        """Получить список всех бронирований."""
        return self.get("/booking")
    
    def get_booking(self, booking_id: int) -> dict:
        """Получить данные бронирования по ID."""
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, booking_data: dict) -> dict:
        """Создать новое бронирование."""
        return self.post("/booking", json=booking_data)

    def delete_booking(self, booking_id: int) -> None:
        """Удалить бронирование по ID."""
        return self.delete(f"/booking/{booking_id}")

