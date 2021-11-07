import requests


class Endpoint():
    def __init__(self):
        pass

    def make_request(self, url: str) -> dict:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data
