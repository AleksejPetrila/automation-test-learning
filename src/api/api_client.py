import requests


class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}

    def _url(self, endpoint: str) -> str:
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint, params=None):
        return requests.get(self._url(endpoint), headers=self.headers, params=params)

    def post(self, endpoint, json_body=None):
        return requests.post(self._url(endpoint), headers=self.headers, json=json_body)

    def put(self, endpoint, json_body=None):
        return requests.put(self._url(endpoint), headers=self.headers, json=json_body)

    def patch(self, endpoint, json_body=None):
        return requests.patch(self._url(endpoint), headers=self.headers, json=json_body)

    def delete(self, endpoint):
        return requests.delete(self._url(endpoint), headers=self.headers)
