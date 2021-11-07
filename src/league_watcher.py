from apis.league_of_legends.champion_rotation import Champion


class LeagueWatcher:
    def __init__(self, api_key: str = None,):
        if not api_key:
            raise ValueError("API Key must be set.")

        self._api_key = api_key
        self._champion = Champion(api_key)

    @property
    def champion(self) -> Champion:
        return self._champion
