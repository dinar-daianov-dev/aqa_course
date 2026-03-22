from jsonschema import validate
from src.schemas.joke_schema import JOKE_SCHEMA
from src.schemas.booking_schema import BOOKING_SCHEMA

def test_random_joke_matches_schema(chuck_norris_client):
    response = chuck_norris_client.get_random_joke()
    validate(instance=response.json(), schema=JOKE_SCHEMA)

def test_booking_matches_schema(booker_client, create_booking):
    """Создать бронирование, получить по id, валидировать схемой"""
    booking_id = create_booking()
    response = booker_client.get_booking(booking_id)
    validate(instance=response.json(), schema=BOOKING_SCHEMA)