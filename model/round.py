
class Round:
    def __init__(self, round_name, start_datetime, end_datetime):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    # ????
    def add_match(self, match):
        self.matches.append(match)

    # work in progress
    def entered_round(self):
        return [
            self.round_name,
            self.start_datetime,
            self.end_datetime,
            self.matches
        ]

    @staticmethod
    def get_match_pairing(player_one, player_two):
        match = (
            player_one,
            player_two
        )
        return match
