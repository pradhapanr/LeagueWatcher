from endpoint import Endpoint


class Champion(Endpoint):
    def __init__(self, api_key):
        super().__init__()
        self._api_key = api_key

    def rotation(self, region: str):
        url = "https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={api_key}".format(
            region=region, api_key=self._api_key)
        return self.make_request(url)
