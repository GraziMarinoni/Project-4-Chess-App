from model.match import Match
from model.player import Player
from model.tournament import Tournament
from view.userView import UserView
from datetime import datetime
from tinydb import TinyDB
import random

players_db = TinyDB('../data/Players database.json')
tournaments_db = TinyDB('../data/Tournaments database.json')


class TournamentController:
    def __init__(self):
        self.view = UserView()
        self.players = Player.load_players()
        self.tournaments = Tournament.load_tournaments()
        self.tournament_input = [
            "Name",
            "Venue name",
            "Number of rounds",
            "Description"
        ]

    def main_menu_start(self):
        # ask user input to select something from the main menu
        self.view.show_main_menu()
        print("Please, select one of the options: ")
        self.user_input()

    def user_input(self):
        user_input = input().lower()
        if user_input == "1":
            self.new_player()
        elif user_input == "2":
            self.new_tournament()
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
            pass
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

    def new_player_input(self):
        player_details = []
        for detail in self.view.player_headers:
            user_input = input(f"Please, type the player's {detail}: ", )
            while user_input == "":
                user_input = input(f"Please, type the player's {detail}: ", )
            # if detail == "National ID":
            #     while True:
            #         if len(user_input) == 7:
            #             if user_input[0:1].isalpha() and user_input[2:].isnumeric():
            #                 break
            #             else:
            #                 user_input = input(f"Please, type the player's {detail}: ", )
            #         else:
            #             user_input = input(f"Please, type the player's {detail}: ", )
            player_details.append(user_input)
        return player_details

    def new_player(self):
        # request user to input player's details
        player_instance = self.new_player_input()
        player = Player(
            first_name=player_instance[0],
            last_name=player_instance[1],
            date_birth=player_instance[2],
            national_identifier=player_instance[3],
            )

        self.view.display_player(player_instance)
        user_input = input("\nPlease, press Enter to continue or type 'no' to re-input: ", )
        if user_input.lower() == "no":
            self.new_player()
        else:
            player.insert_player()
            user_input = input("Please, type 'yes' to add another "
                               "player or 'no' to back to the main menu: ", )
            if user_input.lower() == "yes":
                self.new_player()
            else:
                self.main_menu_start()

    def new_tournament_player(self):
        player_instance = self.new_player_input()
        player_object = Player(
            first_name=player_instance[0],
            last_name=player_instance[1],
            date_birth=player_instance[2],
            national_identifier=player_instance[3],
        )
        self.view.display_player(player_instance)
        user_input = input("\nPlease, press Enter to continue or type 'no' to re-input: ", )
        if user_input.lower() == "no":
            self.new_tournament_player()
        # check how to use "No"
        return player_object

    def new_tournament(self):
        # request user to input player's details
        tournament_details = []
        players_list = []
        for detail in self.tournament_input:
            user_input = input(f"Please, type the tournament's {detail}: ", )
            while user_input == "":
                user_input = input(f"Please, type the tournament's {detail}: ",)
            tournament_details.append(user_input)
        i = 1
        while i <= (int(tournament_details[2])*2):
            print(f"Please, input player {i} of {(int(tournament_details[2])*2)}: ")

            player_instance = self.new_tournament_player()
            players_list.append(player_instance.entered_player())
            i += 1

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
        user_input = input("\nPlease, press Enter to continue or type no to re-input: ", )
        if user_input.lower() == "no":
            self.new_tournament()
        else:
            for player in players_list:
                players_db.insert(player)
            tournament.insert_tournament()
            input("\nPlease, press Enter to go back to the main menu\n")
            self.main_menu_start()

    def start_tournament(self):
        self.view.display_all_tournaments(Tournament.load_tournaments())
        tour = self.search_tournament()
        print(f"                          {tour['name']}, {tour['venue']}")
        print(f"                    Start date and time {tour['start_date']}")
        print(f"                            Round {tour['current_round']} "
              f"of {tour['num_rounds']} ")
        tournament_players = []
        player = 0
        while player < len(tour['registered_players']):
            tournament_players.append(
                f"{tour['registered_players'][player]['first_name']} "
                f"{tour['registered_players'][player]['last_name']}")
            player += 1

        self.round_one(tournament_players)

    def round_one(self, players):
        random.shuffle(players)
        i = 0
        player_one = []
        player_two = []
        while i < len(players):
            player_one.append(players[i])
            player_two.append(players[i+1])
            i += 2
        round = []
        i = 0
        while i < len(player_one):

            round.append([ (i + 1), player_one[i], 0.0 , player_two[i], 0.0,"VS" ])
            i +=1

        self.view.display_round(round)

    def all_players(self):
        # display all players stored in the database
        self.view.display_all_players(Player.load_players())
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def all_tournaments(self):
        # display all new_tournaments stored in the database
        self.view.display_all_tournaments(Tournament.load_tournaments())
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def show_registered_players(self):
        self.view.display_all_players(self.search_tournament()['registered_players'])
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    def show_given_tournament(self):
        self.view.display_tournament(self.search_tournament())
        input("\nPlease, press Enter to go back to the main menu\n")
        self.main_menu_start()

    @staticmethod
    def search_tournament():
        user_input = input(f"Please, provide the tournament's name: ")
        return Tournament.search_tournament(user_input)

    @staticmethod
    def create_match(player1, player2):
        return Match(
            playerwhite=player1,
            playerblack=player2
        )

    @staticmethod
    def get_time():
        dt = datetime.now()
        return f"{dt.strftime('%Y-%m-%d %H:%M:%S')}"


controller = TournamentController()
controller.main_menu_start()

