from ..endpoint import Endpoint


class League(Endpoint):
    def __init__(self, api_key):
        super().__init__()
        self._api_key = api_key

    def challenger_list(self, region: str, queue: str) -> dict:
        queue_type = self._check_queue_type(queue)
        url = 'https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue_type}?api_key={api_key}'.format(
            region=region, queue_type=queue_type, api_key=self._api_key)
        return self.make_request(url)

    def grandmaster_list(self, region: str, queue: str) -> dict:
        queue_type = self._check_queue_type(queue)
        url = 'https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue_type}?api_key={api_key}'.format(
            region=region, queue_type=queue_type, api_key=self._api_key)
        return self.make_request(url)

    def master_list(self, region: str, queue: str) -> dict:
        queue_type = self._check_queue_type(queue)
        url = 'https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue_type}?api_key={api_key}'.format(
            region=region, queue_type=queue_type, api_key=self._api_key)
        return self.make_request(url)

    def by_summoner(self, region: str, summoner_id: str) -> dict:
        url = 'https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'.format(
            region=region, summoner_id=summoner_id, api_key=self._api_key)
        return self.make_request(url)

    def by_rank(self, region: str, division: int, tier: str, queue: str) -> dict:
        queue_type = self._check_queue_type(queue)
        tier_name = self._check_tier(tier)
        division_str = self._check_division(division)
        url = 'https://{region}.api.riotgames.com/lol/league/v4/entries/{queue_type}/{tier_name}/III?api_key=RGAPI-2cb083ad-c541-4431-a448-542dac697e80'

    def _check_queue_type(self, queue: str) -> str:
        queue_name = queue.lower()
        if (queue_name == 'ranked'):
            return 'RANKED_SOLO_5x5'
        elif (queue_name == 'flex'):
            return 'RANKED_FLEX_SR'

        raise ValueError(
            'Queue type must be either \'ranked\' or \'flex\'. Refer to docs for more information about this endpoint.')

    def _check_tier(self, tier: str) -> str:
        tier_list = ['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

        tier_name = tier.upper()
        if tier_name not in tier_list:
            raise ValueError(
                'Tier name invalid. Refer to docs for more information about this endpoint.')
        return tier_name

    def _check_division(self, division: int) -> str:
        if division == 1:
            return 'I'
        elif division == 2:
            return 'II'
        elif division == 3:
            return 'III'
        elif division == 4:
            return 'IV'

        raise ValueError(
            'Division type must be an integer between 1 and 4 (inclusive). Refer to docs for more information about this endpoint.')
