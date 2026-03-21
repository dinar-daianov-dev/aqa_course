import re

def http_status_description(status_code: int) -> str:
    """Функция принимает int, возвращает строку."""
    descriptions = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error"
    }
    return descriptions.get(status_code, "Unknown")

def extract_numbers(text: str) -> list[int]:
    """Принимает строку и возвращает список найденных в ней чисел (int)."""
    return [int(num) for num in re.findall(r'\d+', text)]

def group_by_status(responses: list) -> dict:
    """Принимает список словарей, группирует по статус-коду"""
    grouped = {}
    for resp in responses:
        status = resp.get("status")
        if status not in grouped:
            grouped[status] = []
        grouped[status].append(resp)
    return grouped