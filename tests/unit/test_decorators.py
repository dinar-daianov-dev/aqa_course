import pytest

from src.utils.decorators import log_call, retry

# Декорированная функция возвращает правильный результат
def test_log_call_returns_result():
    @log_call
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

# add.__name__ == "add"(а не "wrapper")
def test_log_call_preserves_name():
    @log_call
    def add(a, b):
        return a + b

    assert add.__name__ == "add"

# Функция, которая всегда работает, возвращает результат
def test_retry_succeeds():
    @retry()
    def multiply(a, b):
        return a * b

    result = multiply(2, 3)
    assert result == 6

# Функция, которая всегда падает, бросает исключение после max_attempts
def test_retry_raises_after_max_attempts():
    @retry(max_attempts=3)
    def always_fail():
        raise ValueError("Fail")

    with pytest.raises(ValueError, match="Fail"):
        always_fail()

# Функция, которая падает 2 раза, потом работает
def test_retry_eventually_succeeds():
    attempts = [0]

    @retry(max_attempts=5)
    def sometimes_fail():
        if attempts[0] < 2:
            attempts[0] += 1
            raise ValueError("Fail")
        return "Success"

    result = sometimes_fail()
    assert result == "Success"