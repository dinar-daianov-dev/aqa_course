def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

def is_palindrome(s):
    """Убираем пробелы и приводим к нижнему регистру для проверки палиндрома."""
    cleaned = s.replace(" ", "").lower()
    # Проверяем, является ли строка палиндромом
    return cleaned == reverse_string(cleaned)
