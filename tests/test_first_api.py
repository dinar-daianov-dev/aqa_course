import requests


def test_chuck_norris_random_joke():
    """Первый API-тест: получаем случайную шутку."""
    response = requests.get("https://api.chucknorris.io/jokes/random")

    # Проверяем статус
    assert response.status_code == 200
    
    # Парсим JSON
    joke = response.json()

    # Проверяем что есть нужные поля
    assert "id" in joke
    assert "value" in joke

    # Проверяем что шутка - не пустая строка
    assert isinstance(joke["value"], str)
    assert len(joke["value"]) > 0

    # Выводим для наглядности
    print(f"\nШутка: {joke['value']}")


def test_categories_returns_list():
    """Второй Api-тест: получаем список категорий."""
    response = requests.get("https://api.chucknorris.io/jokes/categories")

    # Проверяем статус
    assert response.status_code == 200

    # Парсим JSON
    category = response.json()

    # Проверяем что это список
    assert isinstance(category, list)

    # Проверка что список не пустой
    assert len(category) > 0

    # Проверка что "dev" есть в списке
    assert "dev" in category

def test_search_jokes():
    """Третий Api-тест: ищем шутки по запросу c параметром "computer"."""
    response = requests.get("https://api.chucknorris.io/jokes/search", params={"query": "computer"})

    # Проверяем статус
    assert response.status_code == 200

    # Парсим JSON
    search_results = response.json()

    # Проверяем что есть нужные поля "total", "result"
    assert "total" in search_results
    assert "result" in search_results

    # Проверяем что "total" больше 0
    assert search_results["total"] > 0

def test_invalid_category_returns_404():
    """Четвертый Api-тест: ищем шутки по несуществующей категории "fake_xyz"."""
    response = requests.get("https://api.chucknorris.io/jokes/random", params={"category": "fake_xyz"})

    # Проверяем статус 
    assert response.status_code == 404
