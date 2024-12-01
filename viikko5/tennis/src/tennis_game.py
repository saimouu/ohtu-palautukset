class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def _get_point_names(self):
        return ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def _check_win(self, score_difference):
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _equal_score(self):
        if self.m_score1 <= 2:
            return f"{self._get_point_names()[self.m_score1]}-All"
        else:
            return "Deuce"

    def _generate_score(self):
        point_names = self._get_point_names()
        return f"{point_names[self.m_score1]}-{point_names[self.m_score2]}"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score_difference = self.m_score1 - self.m_score2
            return self._check_win(score_difference)
        else:
            return self._generate_score()
