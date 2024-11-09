from playerReader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        players_from_country = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(players_from_country, key=lambda player: player.goals + player.assists, reverse=True)
