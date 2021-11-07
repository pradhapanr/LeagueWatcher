from typing import Optional
from dotenv import load_dotenv
import os

from league_watcher import LeagueWatcher


def main():
    load_dotenv()
    token: Optional[str] = os.environ.get('API_KEY')

    league_watcher = LeagueWatcher(api_key=token)

    champ_rotation = league_watcher.champion.rotation('na1')
    print(champ_rotation)


if __name__ == '__main__':
    main()
