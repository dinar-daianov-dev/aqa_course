import pytest

from src.utils.helpers import http_status_description

@pytest.mark.parametrize("category", [
    "dev",
    "animal",
    "sport",
    "food",
    "celebrity",
])
@pytest.mark.regression
def test_joke_by_category(chuck_norris_client, category):
    """Тестируем получение шутки по категории."""
    # Получи шутку с этой категорией
    response = chuck_norris_client.get_random_joke(category=category)

    # Проверяем статус 200
    assert response.status_code == 200

    # Проверяем что categories есть в joke["categories"]
    joke = response.json()
    assert "categories" in joke
    assert category in joke["categories"]


@pytest.mark.parametrize("query, min_results", [
    ("computer", 1),
    ("phone", 1),
    ("python", 0),
    ("xyznonexistent123", 0),
])
@pytest.mark.regression
def test_search_various_queries(chuck_norris_client, query, min_results):
    """Проверка поиска с разными запросами"""

    # Сделай поиск
    response = chuck_norris_client.search(query=query)

    # Проверь статус 200
    assert response.status_code == 200

    # Проверь что total >= min_results
    data = response.json()
    assert "total" in data
    assert data["total"] >= min_results


@pytest.mark.parametrize("code, expected", [
    (200, "OK"),
    (201, "Created"),
    (400, "Bad Request"),
    (401, "Unauthorized"),
    (403, "Forbidden"),
    (404, "Not Found"),
    (500, "Internal Server Error"),
    (999, "Unknown"),
])
@pytest.mark.regression
def test_status_descriptions(code, expected):
    """Проверка что http_status_description работает для всех кодов"""

    # Вызови http_status_description(code)
    result = http_status_description(code)

    # Проверь что результат == expected
    assert result == expected