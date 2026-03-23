# AQA Course — API Test Automation Framework

Учебный фреймворк для автоматизации тестирования REST API, построенный на Python + pytest. Покрывает позитивные, негативные и параметризованные сценарии для двух публичных API с валидацией JSON-схем и CI/CD-пайплайном.

---

## Стек

| Инструмент | Версия | Назначение |
|---|---|---|
| Python | 3.12 | Основной язык |
| pytest | 9.0.2 | Тест-раннер |
| requests | 2.32.5 | HTTP-клиент |
| jsonschema | 4.26.0 | Валидация схем ответов |
| allure-pytest | 2.15.3 | Репортинг |
| Docker | — | Изолированный запуск |
| GitHub Actions | — | CI/CD |

---

## Тестируемые API

| API | Base URL | Документация |
|---|---|---|
| Restful Booker | `https://restful-booker.herokuapp.com` | https://restful-booker.herokuapp.com/apidoc |
| Chuck Norris Jokes | `https://api.chucknorris.io` | https://api.chucknorris.io |

---

## Установка

```bash
git clone https://github.com/dinar-daianov-dev/aqa_course.git
cd aqa_course

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

## Запуск тестов

### Все тесты
```bash
pytest
```

### По маркерам
```bash
pytest -m smoke          # быстрая проверка работоспособности
pytest -m regression     # полный набор тестов
pytest -m negative       # негативные сценарии
```

### С отчётом Allure
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### В Docker
```bash
docker build -t aqa-tests .
docker run aqa-tests
```

---

## CI/CD

Пайплайн запускается при каждом пуше и pull request в `main`.

```
push / PR
    │
    ▼
┌─────────┐        ┌────────────┐
│  smoke  │──OK──▶ │ regression │
│ (fast)  │        │ + allure   │
└─────────┘        └────────────┘
```

- **smoke** — запускает тесты с маркером `smoke`, блокирует pipeline при падении
- **regression** — запускает весь набор тестов, сохраняет Allure-артефакты

Конфигурация: [.github/workflows/tests.yml](.github/workflows/tests.yml)

---

## Структура проекта

```
aqa_course/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI/CD пайплайн
│
├── src/
│   ├── clients/
│   │   ├── base_client.py      # Базовый HTTP-клиент (requests + logging)
│   │   ├── booker_client.py    # Клиент Restful Booker API
│   │   └── chuck_norris_client.py  # Клиент Chuck Norris API
│   ├── schemas/
│   │   ├── booking_schema.py   # JSON Schema для Booking API
│   │   └── joke_schema.py      # JSON Schema для Chuck Norris API
│   └── utils/
│       ├── algorithms.py       # Вспомогательные алгоритмы
│       ├── decorators.py       # @log_call, @retry
│       ├── helpers.py          # HTTP-хелперы, парсинг
│       └── logger.py           # Настройка логирования
│
├── tests/
│   ├── conftest.py             # Session-фикстуры (chuck_norris_client)
│   ├── api/
│   │   ├── conftest.py         # API-фикстуры (booker_client, create_booking)
│   │   ├── test_booker.py      # CRUD-тесты Restful Booker (позитивные)
│   │   ├── test_booker_negative.py  # Негативные сценарии Booker
│   │   ├── test_chuck_parametrized.py  # Параметризованные тесты Chuck Norris
│   │   └── test_schemas.py     # Валидация JSON-схем
│   └── unit/
│       ├── test_algorithms.py  # Юнит-тесты алгоритмов
│       ├── test_decorators.py  # Юнит-тесты декораторов
│       ├── test_helpers.py     # Юнит-тесты хелперов
│       └── test_python_basics.py  # Python-основы (edge cases)
│
├── Dockerfile
├── pytest.ini                  # Маркеры, testpaths, addopts
└── requirements.txt
```
