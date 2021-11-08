from ..endpoint import Endpoint


class Summoner(Endpoint):
    def __init__(self, api_key):
        super().__init__()
        self._api_key = api_key

    def by_account_id(self, region: str, account_id: str) -> dict:
        url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}?api_key={api_key}".format(
            region=region, account_id=account_id, api_key=self._api_key)
        return self.make_request(url)

    def by_summoner_name(self, region: str, name: str) -> dict:
        url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{name}?api_key={api_key}".format(
            region=region, name=name, api_key=self._api_key)
        return self.make_request(url)

    def by_puuid(self, region: str, puuid: str) -> dict:
        url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}".format(
            region=region, puuid=puuid, api_key=self._api_key)
        return self.make_request(url)

    def by_summoner_id(self, region: str, summoner_id: str) -> dict:
        url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={api_key}".format(
            region=region, summoner_id=summoner_id, api_key=self._api_key)
        return self.make_request(url)
