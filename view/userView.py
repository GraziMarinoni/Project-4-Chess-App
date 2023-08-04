from controller.tournamentController import TournamentController


class UserView:
    def __init__(self):
        self.tournament_controller = TournamentController()

    def show_main_menu(self):
        print("\n   MAIN MENU")
        print("\n1. Play a new Tournament ")
        print("2. List of all players ")
        user_choice = input("Chose one of the options above by typing the number ")
        if user_choice == "1":
            self.chose_tournament()
        elif user_choice == "2":
            print("You chose option 2")
        else:
            print("\nPlease, chose one of the available options")
            self.show_main_menu()

    def chose_tournament(self):
        print("\n1. Play Regional Tournament")
        print("2. Play National Tournament")
        print("3. Play World Tournament")
        user_choice = input("Chose one of the options above by typing the number ")
        if user_choice == "1":
            self.tournament_controller.create_first_round("Regional Tournament")
        elif user_choice == "2":
            self.tournament_controller.create_first_round("National Tournament")
        elif user_choice == "3":
            self.tournament_controller.create_first_round("World Tournament")
        else:
            print("\nPlease, chose one of the available options")
            self.chose_tournament()

    @staticmethod
    def show_tournament_attr(tournament):
        tournament.show_tournament_name()
        tournament.show_venue()
        tournament.show_start_date()
        tournament.show_end_date()
        tournament.show_num_rounds()
        tournament.show_current_round()
