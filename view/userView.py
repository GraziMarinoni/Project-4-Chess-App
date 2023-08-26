from prettytable import PrettyTable


class UserView:
    def __init__(self):
        self.table = PrettyTable()
        # Creating headers for table
        self.player_headers = [
            "First name",
            "Last name",
            "Date of birth",
            "National ID"
        ]
        self.tournament_headers = [
            "Name",
            "Venue name",
            "Start date",
            "End date",
            "Number of rounds",
            "Current round",
            "Players",
            "Description"
        ]
        self.match_headers = [
            "Player One",
            "Player One - Score",
            "VS",
            "Player Two",
            "Player Two - Score",
        ]
        self.round_headers = [
            "Match",
            "Player One",
            "Player One - Score",
            "VS",
            "Player Two",
            "Player Two - Score",
        ]

    @staticmethod
    def show_main_menu():
        # Displays the main menu at the start of the application
        print("\n")
        print("  Chess Tournament Management Application")
        print("===========================================")
        print("\n1- Add a new player")
        print("2- Create a new tournament")
        print("3- Start an existing tournament")
        print("4- Show all players")
        print("5- Show all tournaments ")
        print("6- Show details of a given tournament ")
        print("7- Show the players of a given Tournament")
        print("8- Show the rounds of a given tournament ")
        print("9- Exit the application ")

    def display_player(self, player):
        # shows a single player's details
        self.table.clear()
        self.table.field_names = self.player_headers
        self.table.add_row([
                player[0], player[1], player[2], player[3]
        ])
        print("\n")
        print(self.table)

    def display_all_players(self, players):
        # shows table with players
        self.table.clear()
        self.table.field_names = self.player_headers
        # item rep a player from the dic-db
        for item in players:
            self.table.add_row([
                item["first_name"],
                item["last_name"],
                item["date_birth"],
                item["national_identifier"]
            ])
        print("\n")
        print(self.table.get_string(sortby="First name"))

    def display_tournament(self, tournament):
        # shows
        self.table.clear()
        self.table.field_names = self.tournament_headers
        tournament_players = []
        player = 0
        while player < len(tournament['registered_players']):
            tournament_players.append(
                f"[{(player+1)}] {tournament['registered_players'][player]['first_name']} "
                f"{tournament['registered_players'][player]['last_name']}")
            player += 1

        self.table.add_row([
                tournament['name'], tournament['venue'], tournament['start_date'], tournament['end_date'],
                tournament['num_rounds'], tournament['current_round'],
                tournament_players, tournament['description'],
            ])
        print("\n")
        print(self.table)

    def display_all_tournaments(self, tournaments):
        # shows
        self.table.clear()
        self.table.field_names = self.tournament_headers
        for tournament in tournaments:
            tournaments_players = []
            player = 0
            while player < len(tournament['registered_players']):
                tournaments_players.append(
                    f"[{(player + 1)}] {tournament['registered_players'][player]['first_name']} "
                    f"{tournament['registered_players'][player]['last_name']}")
                player += 1
            self.table.add_row([
                tournament["name"], tournament["venue"],
                tournament["start_date"], tournament["end_date"],
                tournament["num_rounds"], tournament["current_round"],
                tournaments_players, tournament["description"],
            ])
        print("\n")
        print(self.table.get_string(sortby="Name"))

    def display_match(self, match):
        # shows a single match's details
        self.table.clear()
        self.table.field_names = self.match_headers
        self.table.add_row([
                match[0], match[1], "VS", match[2], match[3]
        ])

        print(self.table)

    def display_round(self, round):
        # shows a single round's details
        self.table.clear()
        self.table.field_names = self.round_headers
        for match in round:
            self.table.add_row([
                match[0], match[1], match[2], match[5] , match[3], match[4]
            ])

        print(self.table)

