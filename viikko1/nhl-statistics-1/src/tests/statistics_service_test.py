import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_finds_the_correct_player(self):
        found_player = self.stats.search("Semenko")
        self.assertEqual(found_player, self.stats._players[0])

    def test_none_when_no_player_found(self):
        found_player = self.stats.search("Nieminen")
        self.assertEqual(found_player, None)

    def test_lists_correct_players_of_a_team(self):
        found_players = self.stats.team("EDM")
        self.assertEqual(found_players, 
                         [self.stats._players[0], self.stats._players[2], self.stats._players[4]])

    def test_lists_correct_top_players(self):
        found_players = self.stats.top(2)
        expected_result = [self.stats._players[4], self.stats._players[1], self.stats._players[3]]
        self.assertEqual(found_players, expected_result) 

    def test_correct_top_players_by_goals(self):
        found_players = self.stats.top(2, SortBy.GOALS)
        expected_result = [self.stats._players[1], self.stats._players[3], self.stats._players[2]]
        self.assertEqual(found_players, expected_result)

    def test_correct_top_players_by_assists(self):
        found_players = self.stats.top(2, SortBy.ASSISTS)
        expected_results = [self.stats._players[4], self.stats._players[3], self.stats._players[1]]
