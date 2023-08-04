from model.match import Match
from model.player import Player
from model.round import Round
from view.userView import UserView
from model.tournament import TournamentAttributes
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.view = UserView()

    @staticmethod
    def define_venue(tournament_name):
        venue = ""
        if tournament_name == "Regional Tournament":
            venue = "London"
        elif tournament_name == "National Tournament":
            venue = "New York"
        elif tournament_name == "World Tournament":
            venue = "Paris"
        return venue

    @staticmethod
    def num_rounds(tournament_name):
        num_rounds = ""
        if tournament_name == "Regional Tournament":
            num_rounds = "4"
        elif tournament_name == "National Tournament":
            num_rounds = "6"
        elif tournament_name == "World Tournament":
            num_rounds = "8"
        return num_rounds

    @staticmethod
    def create_player(first_name, last_name, date_birth):
        return Player(
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            national_id="AB12345"
        )

    @staticmethod
    def create_match(player1, player2):
        return Match(
            playerwhite=player1,
            playerblack=player2
        )

    def create_tournament(self, tournament_name):
        return TournamentAttributes(
            name=tournament_name,
            venue=self.define_venue(tournament_name),
            start_date=datetime.now(),
            end_date="",
            current_round="1",
            num_rounds=self.num_rounds(tournament_name)
        )

    def create_first_round(self, tournament_name):
        tournament = self.create_tournament(tournament_name)

        player1 = self.create_player("James", "Bond", "1980-08-12")
        player2 = self.create_player("Sherlock", "Holmes", "1950-03-23")
        player3 = self.create_player("Agatha", "Christie", "1948-09-15")
        player4 = self.create_player("Lara", "Croft", "1985-03-07")

        match1 = self.create_match(player1, player2)
        match2 = self.create_match(player3, player4)

        tournament.add_player(player1)
        tournament.add_player(player2)

        round1 = Round(
            name="Round 1",
            start_datetime=datetime.now()
        )

        round1.add_match(match1)
        round1.add_match(match2)
