from src.utils.helpers import (
    http_status_description, 
    extract_numbers, 
    group_by_status
) 

def test_http_status_description_known():
    assert http_status_description(200) == "OK"

def test_http_status_description_unknown():
    assert http_status_description(999) == "Unknown"

def test_http_status_description_another():
    assert http_status_description(404) == "Not Found"


def test_extract_numbers_known():
    assert extract_numbers("abc123def") == [123]

def test_extract_numbers_unknown():
    assert extract_numbers("abc") == []

def test_extract_numbers_multiple():
    assert extract_numbers("abc123def456") == [123, 456]


def test_group_by_status_known():
    responses = [
        {"url": "/api/users", "status": 200},
        {"url": "/api/orders", "status": 500},
        {"url": "/api/users", "status": 200},
    ]
    grouped = group_by_status(responses)
    assert grouped == {
        200: [
            {"url": "/api/users", "status": 200},
            {"url": "/api/users", "status": 200},
        ],
        500: [
            {"url": "/api/orders", "status": 500},
        ],
    }

def test_group_by_status_empty():
    responses = []
    grouped = group_by_status(responses)
    assert grouped == {}

def test_group_by_status_single():
    responses = [
        {"url": "/api/users", "status": 200},
    ]
    grouped = group_by_status(responses)
    assert grouped == {
        200: [
            {"url": "/api/users", "status": 200},
        ],
    }
