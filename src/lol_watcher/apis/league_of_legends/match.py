from src.lol_watcher.apis.endpoint import Endpoint
from src.lol_watcher.utils.convert_queue import queue_to_int


class Match(Endpoint):
    def __init__(self, api_key):
        super().__init__()
        self._api_key = api_key

    def by_account_id(self, region: str, account_id: str) -> dict:
        url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}?api_key={api_key}".format(
            region=region, account_id=account_id, api_key=self._api_key)
        return self.make_request(url)

    def matchlist_by_puuid(self, region: str, puuid: str, start: int = None, count: int = None, queue: int = None, type: str = None, start_time: int = None, end_time: int = None):
        url = f'https://{start}'
        return url
