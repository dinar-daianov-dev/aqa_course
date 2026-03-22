import requests


class BaseApiClient:
    """Базовый API-клиент. Все конкретные клиенты наследуются от него."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)
    
    def post(self, endpoint: str, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.post(f"{self.base_url}{endpoint}", **kwargs)
    
    def delete(self, endpoint: str, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

    def close(self):
        self.session.close()