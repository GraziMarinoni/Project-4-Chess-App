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

    def display_player(self, player):
        # shows a single player's details
        self.table.clear()
        self.table.field_names = self.player_headers
        self.table.add_row([
                player[0],
                player[1],
                player[2],
                player[3]
            ])

        print(self.table)

    def display_all_players(self, players):
        # shows table with players
        self.table.clear()
        self.table.field_names = self.player_headers
        for item in range(len(players)):
            self.table.add_row([
                players[item]["first_name"],
                players[item]["last_name"],
                players[item]["date_birth"],
                players[item]["national_identifier"]
            ])

        print(self.table.get_string(sortby="First name"))







