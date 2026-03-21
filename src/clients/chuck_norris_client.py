from src.clients.base_client import BaseApiClient


class ChuckNorrisClient(BaseApiClient):
    """Клиент для работы с API Chuck Norris."""

    def __init__(self):
        super().__init__("https://api.chucknorris.io")

    def get_random_joke(self, category: str | None = None):
        params = {"category": category} if category else {}
        return self.get("/jokes/random", params=params)
    
    def get_categories(self):
        return self.get("/jokes/categories")

    def search(self, query: str):
        return self.get("/jokes/search", params={"query": query})