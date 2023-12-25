from prettytable import PrettyTable


class UserView:
    # View model init.
    def __init__(self):
        self.table = PrettyTable()
        self.table.vertical_char = "│"
        self.table.horizontal_char = "─"
        # Creating headers for table
        self.player_headers = [
            "First name",
            "Last name",
            "Date of birth",
            "National Identifier"
        ]
        self.tournament_headers = [
            "Name",
            "Venue name",
            "Start date",
            "End date",
            "Number of rounds",
            "Current round",
            "Players",
            "Description",
            "Rounds"
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
        self.tournament_rounds = [
            "Round",
            "Start Datetime",
            "End Datetime",
            "Match",
            "Player One",
            "Player One Score",
            "Vs",
            "Player Two",
            "Player Two Score"
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

    def display_player(self, player_details):
        # Shows a single player's details - 1st name, last name, date of birth and national ID
        self.table.clear()
        self.table.field_names = self.player_headers
        self.table.add_row([
                player_details[0], player_details[1], player_details[2], player_details[3]
        ])
        print("\n")
        print(self.table)

    def display_all_players(self, players):
        # Shows table with players
        self.table.clear()
        self.table.field_names = self.player_headers
        for player_details in players:
            self.table.add_row([
                player_details["first_name"],
                player_details["last_name"],
                player_details["date_birth"],
                player_details["national_identifier"]
            ])
        print("\n")
        # Prints the table of players sorted alphabetically
        print(self.table.get_string(sortby="First name"))

    def display_start_tournament(self, tour):
        # Shows a single player's details
        self.table.clear()
        self.table.header = False
        self.table.add_column("tournament", [f"{tour['name']}, {tour['venue']}",
                                             f"Start date and time {tour['start_date']}",
                                             f"Round {tour['current_round']} of {tour['num_rounds']} "
                                             ])
        print(self.table)
        self.table.header = True

    def tournament_table(self, tournament):
        tournament_players = []
        player = 0
        # Appends the first and last names of a player into the new list
        while player < len(tournament['registered_players']):
            tournament_players.append(
                f"[{(player+1)}] {tournament['registered_players'][player]['first_name']} "
                f"{tournament['registered_players'][player]['last_name']}")
            player += 1
        self.table.add_row([
                tournament['name'], tournament['venue'], tournament['start_date'], tournament['end_date'],
                tournament['num_rounds'], tournament['current_round'],
                tournament_players, tournament['description'], tournament['rounds'],
            ])

    def display_tournament(self, tournament):
        # Shows the complete details of a tournament
        self.table.clear()
        self.table.field_names = self.tournament_headers
        self.tournament_table(tournament)
        print("\n")
        print(self.table)

    def display_all_tournaments(self, tournaments):
        # Shows the complete details of all tournaments
        self.table.clear()
        self.table.field_names = self.tournament_headers
        for tournament in tournaments:
            self.tournament_table(tournament)
        print("\n")
        print(self.table.get_string(sortby="Name"))

    def display_match(self, match):
        # shows a single match details with both player's name and score
        self.table.clear()
        self.table.field_names = self.match_headers
        self.table.add_row([
                match[0], match[1], "  VS  ", match[2], match[3]
        ])
        print(self.table)

    @staticmethod
    def finished_match(match_num):
        print(f"Who won match [{match_num+1}]")
        print("[1] if player One won")
        print("[2] if player Two won ")
        print("[0] if it is a tie")

    def display_round(self, round_details):
        # shows a single round details with the match number and both player's name and score
        self.table.clear()
        self.table.field_names = self.round_headers
        match_number = 0
        for match in round_details:
            match_number += 1
            self.table.add_row([
                match_number, match[0], match[1], " VS ", match[2], match[3]
            ])
        print(self.table)

    def display_tour_rounds(self, rounds):
        self.table.clear()
        self.table.field_names = self.tournament_rounds
        line_counter = 0
        for round in rounds:
            line_counter += 1
            match = 0
            while match < len(round[3]):
                # match represents complete round details as:
                # round number = round[0], round start-datetime = round[1], round end-datetime = round[2]
                # match number = (match + 1)
                # player one = round[3][match][0][0] , player one score =  round[3][match][0][1]
                # player two = round[3][match][1][0] , player two score = round[3][match][1][1]
                self.table.add_row([
                    round[0], round[1], round[2], (match + 1),
                    round[3][match][0][0], round[3][match][0][1], " VS ", round[3][match][1][0], round[3][match][1][1]
                ])
                match += 1

            if line_counter < len(rounds):
                self.table.add_row(["───────────", "──────────────────────", "──────────────────────",
                                    "─────────", "──────────────────────", "──────────────────",
                                    "─────────", "──────────────────────", "──────────────────"])
        print(self.table)
