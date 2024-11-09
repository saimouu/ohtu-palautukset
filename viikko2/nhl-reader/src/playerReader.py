import requests

from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            self.players.append(Player(player_dict))
        return self.players

    def get_nationalities(self):
        nationalities = []
        for player in self.players:
            if player.nationality not in nationalities:
                nationalities.append(player.nationality)
        return sorted(nationalities)
