class Tournament:
    def __init__(self, name, venue, start_date, end_date,
                 current_round, num_rounds=4):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.registered_players = []
        self.description = ""

    def add_player(self, player):
        self.registered_players.append(player)


class TournamentAttributes(Tournament):
    def show_tournament_name(self):
        print(f"\nThis is a {self.name}")

    def show_venue(self):
        print(f"It's taking place in {self.venue}")

    def show_start_date(self):
        print(f"It will start on {self.start_date}")

    def show_end_date(self):
        print(f"It will end on {self.end_date}")

    def show_num_rounds(self):
        print(f"There are {self.num_rounds} rounds in this tournament")

    def show_current_round(self):
        print(f"This is round {self.current_round}")



