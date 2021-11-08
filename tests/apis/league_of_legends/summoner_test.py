import unittest
import responses
import requests
from src.lol_watcher.apis.league_of_legends.summoner import Summoner


class TestSummonerAPI(unittest.TestCase):
    @responses.activate
    def test_by_summoner_name(self):
        responses.add(responses.GET, 'http://blabla.com/api/1',
                      json={'foo': 'bar'}, status=200)

        res = requests.get('http://blabla.com/api/1')

        assert res.json() == {'foo': 'bar'}
