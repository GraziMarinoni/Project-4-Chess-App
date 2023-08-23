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
            "Current round ",
            "Players",
            "Description "
        ]

    @staticmethod
    def show_main_menu():
        # Displays the main menu at the start of the application
        print("\n")
        print("  Chess Tournament Management Application")
        print("===========================================")
        print("\n1- Add a new player")
        print("2- Creat a new tournament")
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
                player["first_name"], player["last_name"], player["date_birth"], player["national_identifier"]
        ])
        print("\n")
        print(self.table)

    def display_all_players(self, players):
        # shows table with players
        self.table.clear()
        self.table.field_names = self.player_headers
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
        for item in tournaments:
            tournaments_players = []
            player = 0
            while player < len(item['registered_players']):
                tournaments_players.append(
                    f"[{(player + 1)}] {item['registered_players'][player]['first_name']} "
                    f"{item['registered_players'][player]['last_name']}")
                player += 1
            self.table.add_row([
                item["name"], item["venue"],
                item["start_date"], item["end_date"],
                item["num_rounds"], item["current_round"],
                tournaments_players, item["description"],
            ])
        print("\n")
        print(self.table.get_string(sortby="Name"))
