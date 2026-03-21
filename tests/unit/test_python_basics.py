import pytest

def test_float_trap():
    """Ловушка: 0.1 + 0.2 != 0.3 из-за IEEE 754."""
    # Что вернёт 0.1 + 0.2? Попробуй assert ==, потом исправь.
    # Подсказка: round() или pytest.approx()
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_mutable_vs_immutable():
    """Строки неизменяемые, списки изменяемые."""
    s = "hello"
    lst = [1,2,3]
    # Попробуй s[0] = "H" — что будет?
    # А с list: lst = [1,2,3]; lst[0] = 99 — что будет?
    lst[0] = 99

    # Проверка что s[0] == "H" бросает TypeError
    with pytest.raises(TypeError):
        s[0] = "H"

    assert lst[0] == 99

def test_is_vs_equals():
    """== сравнивает ЗНАЧЕНИЯ, is сравнивает ОБЪЕКТЫ."""
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    # Что вернёт a == b?
    # Что вернёт a is b?
    # Что вернёт a is c?
    assert a == b
    assert a is not b
    assert a is c

def test_falsy_values():
    """Что является False в Python?"""
    # Проверь: bool(0), bool(""), bool([]), bool(None), bool({}), bool(0.0)
    # А что True: bool(1), bool("text"), bool([1]), bool(-1)
    assert not bool(0)
    assert not bool("")
    assert not bool([])
    assert not bool(None)
    assert not bool({})
    assert not bool(0.0)

    assert bool(1)
    assert bool("text")
    assert bool([1])
    assert bool(-1)

def test_list_copy_trap():
    """Ловушка: присваивание списка НЕ копирует его."""
    a = [1, 2, [3, 4]]
    b = a          # b — ссылка на тот же объект!
    b[0] = 99
    # Что сейчас в a[0]? Проверь.
    # Как правильно скопировать? Попробуй a.copy() и import copy; copy.deepcopy(a)
    assert a[0] == 99
    a.copy()  # поверхностная копия, вложенные объекты всё равно общие
    import copy
    b = copy.deepcopy(a)  # глубокая копия, вложенные объекты копируются
    b[2][0] = 999

    # Проверка что a[2][0] НЕ изменилось
    assert a[2][0] == 3