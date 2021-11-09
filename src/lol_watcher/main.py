from typing import Optional
from dotenv import load_dotenv
import os
import pprint

from src.lol_watcher.league_watcher import LeagueWatcher


def main():
    load_dotenv()
    token: Optional[str] = os.environ.get('API_KEY')
    pp = pprint.PrettyPrinter(indent=4)

    league_watcher = LeagueWatcher(api_key=token)

    match = league_watcher.match.matchlist_by_puuid('na1', 'blah')
    print(match)


if __name__ == '__main__':
    main()
