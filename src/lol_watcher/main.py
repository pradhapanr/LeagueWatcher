from typing import Optional
from dotenv import load_dotenv
import os
import pprint

from .league_watcher import LeagueWatcher


def main():
    load_dotenv()
    token: Optional[str] = os.environ.get('API_KEY')
    pp = pprint.PrettyPrinter(indent=4)

    league_watcher = LeagueWatcher(api_key=token)

    champ_rotation = league_watcher.champion.rotation('na1')
    pp.pprint(champ_rotation)

    chall_queue = league_watcher.league.challenger_list(
        'na1', 'ranked')
    pp.pprint(chall_queue)


if __name__ == '__main__':
    main()
