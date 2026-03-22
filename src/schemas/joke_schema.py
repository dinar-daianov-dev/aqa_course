JOKE_SCHEMA = {
    "type": "object",
    "required": ["id", "value", "url", "icon_url", "categories", "created_at", "updated_at"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "value": {"type": "string", "minLength": 1},
        "url": {"type": "string"},
        "icon_url": {"type": "string"},
        "categories": {
            "type": "array",
            "items": {"type": "string"}
        },
        "created_at": {"type": "string"},
        "updated_at": {"type": "string"},
    }
}