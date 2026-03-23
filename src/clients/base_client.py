import requests
import logging
import time


class BaseApiClient:
    """Базовый API-клиент. Все конкретные клиенты наследуются от него."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.logger = logging.getLogger(self.__class__.__name__)

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)

        self.logger.info(f"-> {method} {endpoint}")

        start = time.perf_counter()
        response = self.session.request(method, url, **kwargs)
        elapsed = time.perf_counter() - start

        # Лог ответа
        status_emoji = "✅" if response.ok else "❌"
        self.logger.info(
            f"<- {status_emoji}, {response.status_code} {response.reason} ({elapsed:.3f}s, {len(response.content)} bytes)"
        )

        # Лог params если есть
        if "params" in kwargs and kwargs["params"]:
            self.logger.debug(f"Params: {kwargs['params']}")
        
        # Предупреждение если медленно
        if elapsed > 2.0:
            self.logger.warning(f"   ⚠ Slow response: {elapsed:.1f}s")

        return response

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def close(self):
        self.session.close()