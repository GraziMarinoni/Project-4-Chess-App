from model.round import Round
from model.player import Player
from model.tournament import Tournament
from view.userView import UserView
from datetime import datetime
from tinydb import TinyDB
import random
import re
import os


# to get the current working directory and then use the path to create the data directory
directory_data = f"{os.path.dirname(__file__)}/../data"

players_db = TinyDB(f"{directory_data}/Players database.json")
tournaments_db = TinyDB(f"{directory_data}/Tournaments database.json")


class Controller:
    # Instantiate the tournament controller
    def __init__(self):
        self.view = UserView()
        self.players = Player.load_players()
        self.tournaments = Tournament.load_tournaments()
        self.round = []
        self.tour = None
        self.completed_rounds = []
        self.tournament_players = []
        self.tour_pairs = []
        self.player_score = {}
        self.tournament_input = [
            "Name",
            "Venue name",
            "Number of rounds",
            "Description"
        ]

    def main_menu_start(self):
        # Calls the main menu and takes the user input.
        self.view.show_main_menu()
        print("Please, select one of the options: ")
        self.user_input()

    def user_input(self):
        # Takes the user input and redirect it to the selected option.
        user_input = input().lower()
        if user_input == "1":
            self.add_player()
        elif user_input == "2":
            self.new_tournament_input()
        elif user_input == "3":
            self.start_tournament()
        elif user_input == "4":
            self.all_players()
        elif user_input == "5":
            self.all_tournaments()
        elif user_input == "6":
            self.show_given_tournament()
        elif user_input == "7":
            self.show_registered_players()
        elif user_input == "8":
            self.show_rounds()
        elif user_input == "9":
            user_input = input("\nPress Enter to exit or "
                               "type 'no' to get back to the menu: ", ).lower()
            if user_input == "":
                print("\nThank you for using this application\n")
                exit()
            elif user_input == "no":
                self.main_menu_start()
        else:
            print("Please, select one of the options from the menu: ")
            self.user_input()

    def player_input(self):
        # Takes the details for a new player, verifies the data
        # and displays the new player to the user for confirmation
        player_details = []
        for detail in self.view.player_headers:
            user_input = input(f"Please, type the player's {detail.lower()}: ", )
            if detail == "First name" or detail == "Last name":
                while True:
                    if re.match('^[a-zA-Z]+$', user_input):
                        break
                    else:
                        user_input = input(f"Please, type the player's {detail.lower()}: ", )
            if detail == "Date of birth":
                while True:
                    try:
                        datetime.strptime(user_input, "%d/%m/%Y")
                        break
                    except ValueError:
                        user_input = input(f"Please, type the player's {detail.lower()} DD/MM/YYYY: ", )
            if detail == "National Identifier":
                while True:
                    if re.match('([a-zA-Z]{2})([0-9]{5})$', user_input):
                        break
                    else:
                        user_input = input(f"Please, type the player's {detail.lower()} (e.g. AB12345): ", )
            player_details.append(user_input)
        player = Player(
            first_name=player_details[0],
            last_name=player_details[1],
            date_birth=player_details[2],
            national_identifier=player_details[3],
        )
        self.view.display_player(player_details)
        return player

    def add_player(self):
        # request user to input player's details and store in the players db
        player = self.player_input()
        user_input = input("\nPlease, press Enter to continue or type 'no' to re-input: ", )
        if user_input.lower() == "no":
            self.add_player()
        else:
            player.insert_player()
            user_input = input("Please, type 'add' to add another "
                               "player or press Enter to go back to the main menu: ", )
            if user_input.lower() == "add":
                self.add_player()
            else:
                self.main_menu_start()

    def add_tournament_player(self):
        # request a player details for the tournament and return player instance.
        player = self.player_input()
        user_input = input("\nPlease, press Enter to continue or type 'no' to re-input: ", )
        if user_input.lower() == "no":
            self.add_tournament_player()
        return player

    def new_tournament_input(self):
        # request user to input tournament's details and store it in the tournaments' db.
        tournament_details = []
        players_list = []
        for detail in self.tournament_input:
            user_input = input(f"Please, type the tournament's {detail.lower()}: ", )
            if detail == "Number of rounds":
                while True:
                    if re.match('([0-9])', user_input):
                        break
                    else:
                        user_input = input(f"Please, type the tournament's {detail.lower()}: ", )
            while user_input == "":
                user_input = input(f"Please, type the tournament's {detail.lower()}: ", )
            tournament_details.append(user_input)

        players_counter = 1
        while players_counter <= (int(tournament_details[2]) * 2):
            # loop to ask user to input as many players as the number of rounds x2
            print(f"Please, input player {players_counter} of {(int(tournament_details[2]) * 2)}: ")
            player_instance = self.add_tournament_player()
            # appending players as a dictionary to the players_list
            players_list.append(player_instance.entered_player())
            players_counter += 1
        tournament = Tournament(
            name=tournament_details[0],
            venue=tournament_details[1],
            start_date=self.get_time(),
            end_date="Not finished yet",
            num_rounds=tournament_details[2],
            current_round=1,
            registered_players=players_list,
            description=tournament_details[3]
        )
        self.view.display_tournament(tournament.entered_tournament())
        user_input = input("\nPlease, press Enter to continue or type 'no' to re-input: ", )
        if user_input.lower() == "no":
            self.new_tournament_input()
        else:
            # the tournament's players and the new tournament details will be added to their database
            for player in players_list:
                players_db.insert(player)
            tournament.insert_tournament()
            input("\nPlease, press Enter to go back to the main menu\n")
            self.main_menu_start()

    def start_tournament(self):
        # Show the user the unfinished tournaments and take their input to start a tournament.
        if not Tournament.unfinished_tournaments():
            print("There is no tournament to be played. Please, create a new tournament in the main menu.")
            input("\nPlease, press Enter to go back to the main menu\n")
            self.main_menu_start()
        else:
            self.view.display_all_tournaments(Tournament.unfinished_tournaments())
            self.tour = self.search_tournament_input()
            if self.tour:
                #  displays the tournament banner
                self.view.display_start_tournament(self.tour)
                # loading details from db to be processed in the next stage
                self.tour_pairs = self.tour['paired_players']
                self.player_score = self.tour['player_score']
                self.tournament_logic()

    def tournament_logic(self):
        # Check which round will be played
        if self.tour['current_round'] <= int(self.tour['num_rounds']):
            self.round = []
            user_input = input(f"\nPress Enter to start round [{self.tour['current_round']}] or "
                               f"type 'exit' to go back to the menu:\n")
            if user_input == "exit":
                self.main_menu_start()
            else:
                self.tournament_players = []
                player = 0
                # Store the tournament's players in a list in first + last names format.
                while player < len(self.tour['registered_players']):
                    self.tournament_players.append(
                        f"{self.tour['registered_players'][player]['first_name']} "
                        f"{self.tour['registered_players'][player]['last_name']}")
                    player += 1
                round_started = self.get_time()
                if self.tour['current_round'] == 1:
                    # If first round, will apply the logic for round one
                    self.round_one(self.tournament_players)
                else:
                    # Implements Swiss pairing for rounds beyond the first
                    self.other_rounds(self.tournament_players)

                # Displays the matches for that round with the paired players
                self.view.display_round(self.round)
                input("\nPress Enter to input the players' scores after the round is finished...")
                round_finished = self.get_time()
                round_matches = []
                match_number = 0
                # Displays the round matches, then updates the players' scores from the user input
                while match_number < int(self.tour['num_rounds']):
                    self.view.display_match(self.round[match_number])
                    self.match_winner(match_number)
                    # Creates a tuple with the final results for the match and append to round_matches list
                    finished_match = (([self.round[match_number][0], self.round[match_number][1]],
                                      [self.round[match_number][2], self.round[match_number][3]]))
                    round_matches.append(finished_match)
                    match_number += 1

                completed_round = Round(
                    round_name=f" Round {self.tour['current_round']}",
                    start_datetime=round_started,
                    end_datetime=round_finished,
                    matches=round_matches
                )
                self.view.display_round(self.round)

                # updates the details that changes in every round
                if self.tour['current_round'] < int(self.tour['num_rounds']):
                    self.tour['current_round'] += 1
                    Tournament.update_tournament(self.tour['name'], [completed_round.entered_round()],
                                                 self.tour['current_round'],
                                                 self.tour_pairs, self.player_score, "Not finished yet")
                # Last round
                else:
                    Tournament.update_tournament(self.tour['name'], [completed_round.entered_round()],
                                                 self.tour['current_round'],
                                                 self.tour_pairs, self.player_score, self.get_time())
                    self.tour['current_round'] += 1
                self.tournament_logic()

        # Reloads the updated rounds and displays them at the end of the tournament
        self.view.display_tour_rounds(Tournament.search_tournament(self.tour['name'])['rounds'])
        print(" This tournament has finished. Thank you for using this application")
        user_input = input("\nPress Enter to go back to the menu:\n")
        if user_input == "":
            self.main_menu_start()

    def other_rounds(self, players):
        # Swiss pairing system
        players = sorted(players, key=lambda player: self.player_score[player], reverse=True)
        # Go through the sorted list of players to create pairs according to their score and matches before this round
        while len(players) > 2:
            player_one = players[0]
            player_two = None
            # Try to find an opponent for player_one
            opponent_found = False
            for opponent in players[1:]:
                # Check if player_one and opponent have not played against each other before
                check = Controller.check_pairing(player_one, opponent, self.tour_pairs)
                if not check:
                    player_two = opponent
                    opponent_found = True
                    break
            # If an opponent is found, will pair and remove them from the players list to avoid re-matching
            if opponent_found:
                self.round.append([player_one, self.player_score[player_one],
                                   player_two, self.player_score[player_two]])
                self.tour_pairs.append((player_one, player_two))
                players.remove(player_one)
                players.remove(player_two)
            else:
                # If NO opponent is found, move player_one to the end of the list and start over
                players.append(player_one)
                players.pop(0)
        if len(players) == 2:
            # the remaining 2 players will be paired automatically
            self.round.append([players[0], self.player_score[players[0]],
                               players[1], self.player_score[players[1]]])
            self.tour_pairs.append((players[0], players[1]))

    @staticmethod
    def check_pairing(player_one, player_two, matches):
        # Check if a match between player_one and player_two has already been played before.
        for match in matches:
            if (player_one in match) and (player_two in match):
                return True
        return False

    def round_one(self, players):
        # Shuffle and pair players for first round,
        random.shuffle(players)
        self.player_score = {player: 0.0 for player in players}
        i = 0
        player_one = []
        player_two = []
        # Splits the players list into two groups of players
        while i < len(players):
            player_one.append(players[i])
            player_two.append(players[i + 1])
            i += 2
        x = 0
        while x < len(player_one):
            # Append the matches pairing for round one to an instance var to be used in the other functions.
            self.round.append([player_one[x], self.player_score[player_one[x]],
                               player_two[x], self.player_score[player_two[x]]])
            self.tour_pairs.append((player_one[x], player_two[x]))
            x += 1

    def match_winner(self, match):
        # Defines winning, losing and tie scores
        self.view.finished_match(match)
        user_input = input()
        if user_input == "1":
            self.round[match][1] += 1.0
            self.player_score[self.round[match][0]] += 1.0
        elif user_input == "2":
            self.round[match][3] += 1.0
            self.player_score[self.round[match][2]] += 1.0
        elif user_input == "0":
            self.round[match][1] += 0.5
            self.round[match][3] += 0.5
            self.player_score[self.round[match][0]] += 0.5
            self.player_score[self.round[match][2]] += 0.5
        else:
            self.match_winner(match)

    def show_rounds(self):
        # Loads and displays all rounds of a given tournament
        self.view.display_all_tournaments_names(Tournament.load_tournaments())
        if not self.search_tournament_input()['rounds']:
            print("No round was played yet.")
        else:
            self.view.display_tour_rounds(self.search_tournament_input()['rounds'])
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def all_players(self):
        # Displays all players stored in the database
        self.view.display_all_players(Player.load_players())
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def all_tournaments(self):
        # Displays all new_tournaments stored in the database
        self.view.display_all_tournaments(Tournament.load_tournaments())
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def show_registered_players(self):
        # Shows players of a given tournament
        self.view.display_all_tournaments_names(Tournament.load_tournaments())
        self.view.display_all_players(self.search_tournament_input()['registered_players'])
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def show_given_tournament(self):
        # Displays all details of a given tournament
        self.view.display_all_tournaments_names(Tournament.load_tournaments())
        tour = self.search_tournament_input()
        if tour:
            self.view.display_tournament(tour)
            input("\nPlease, press Enter to go back to the main menu\n")
            self.main_menu_start()

    def search_tournament_input(self):
        # Checks if the tournament exists in the db and returns it to the user
        user_input = input("Please, provide the tournament's name: ")
        print()
        if Tournament.check_tournament(user_input):
            return Tournament.search_tournament(user_input)
        else:
            print("The entered name is incorrect.\n")
            return self.search_tournament_input()

    @staticmethod
    def get_time():
        dt = datetime.now()
        return f"{dt.strftime('%Y-%m-%d %H:%M:%S')}"
