from model.match import Match
from model.player import Player
from view.userView import UserView
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.view = UserView()
        self.players = Player.load_players()

    def main_menu_start(self):
        # ask user input to select something from the main menu
        self.view.show_main_menu()
        print("Please select one of the options: ")
        user_input = input().lower()

        if user_input == "1":
            self.new_player()

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass
        elif user_input == "4":
            self.all_players()

        '''elif user_input == "5":
            pass

        elif user_input == "exit":
            self.menu_view.are_you_sure_exit()
            user_input = input().lower()

            if user_input == "y":
                exit()
            elif user_input == "n":
                self.view.show_main_menu()

        else:
            self.menu_view.input_error()
            self.view.show_main_menu()'''

    def new_player(self):
        # request user to input player's details
        player_details = []
        for detail in self.view.player_headers:
            user_input = input(f"Please, type the player's {detail}: ", )
            while user_input == "":
                user_input = input(f"Please, type the player's {detail}: ", )
            if detail == "National ID":
                while True:
                    if len(user_input) == 7:
                        if user_input[0:1].isalpha() and user_input[2:].isnumeric():
                            break
                        else:
                            user_input = input(f"Please, type the player's {detail}: ", )
                    else:
                        user_input = input(f"Please, type the player's {detail}: ", )
            player_details.append(user_input)

        player = Player(
            first_name=player_details[0],
            last_name=player_details[1],
            date_birth=player_details[2],
            national_identifier=player_details[3],
            )

        self.view.display_player(player_details)
        user_input = input("Please, press Enter to continue or type no to re-input: ", )
        if user_input.lower() == "no":
            self.new_player()
        else:
            player.insert_player()
            user_input = input("Please, type yes to add another "
                               "player or no to back to the main menu: ", )
            if user_input.lower() == "yes":
                self.new_player()
            else:
                self.main_menu_start()

    def all_players(self):
        # display all players stored in the database
        self.view.display_all_players(Player.load_players())
        input("Please, press Enter to go back to the main menu ")
        self.main_menu_start()

    @staticmethod
    def create_match(player1, player2):
        return Match(
            playerwhite=player1,
            playerblack=player2
        )

    @staticmethod
    def mark_as_started(self):
        return datetime.now()

    @staticmethod
    def mark_as_finished(self):
        return datetime.now()


test = TournamentController()
test.main_menu_start()