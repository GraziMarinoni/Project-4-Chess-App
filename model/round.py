
class Round:
    # Round model init
    def __init__(self, round_name, start_datetime, end_datetime, matches):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches

    def entered_round(self):
        return [
            self.round_name,
            self.start_datetime,
            self.end_datetime,
            self.matches
        ]
