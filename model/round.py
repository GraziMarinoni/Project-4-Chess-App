from datetime import datetime

class Round:
    def __init__(self, round_name, start_datetime, end_datetime):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)
    def set_round(self):
        return [
            self.round_name,
            self.start_datetime,
            self.end_datetime,
            self.matches
        ]

    def get_match_pairing(self, player_white, player_black):
        match = (
            [f"{player_white['first_name']} + ' ' + {player_white['last_name']}",
            player_white["score"]],

            [f"{player_black['first_name']} + ' ' + {player_black['last_name']}",
            player_black["score"]]

        )
        self.add_match(match)

