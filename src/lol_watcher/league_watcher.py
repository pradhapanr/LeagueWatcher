from src.lol_watcher.apis.league_of_legends.champion_rotation import Champion
from src.lol_watcher.apis.league_of_legends.summoner import Summoner
from src.lol_watcher.apis.league_of_legends.league import League
from src.lol_watcher.apis.league_of_legends.match import Match


class LeagueWatcher:
    def __init__(self, api_key: str = None,):
        if not api_key:
            raise ValueError("API Key must be set.")

        self._api_key = api_key
        self._champion = Champion(api_key)
        self._summoner = Summoner(api_key)
        self._league = League(api_key)
        self._match = Match(api_key)

    @property
    def champion(self) -> Champion:
        return self._champion

    @property
    def summoner(self) -> Summoner:
        return self._summoner

    @property
    def league(self) -> League:
        return self._league

    @property
    def match(self) -> Match:
        return self._match
