import os
from tinydb import TinyDB, Query

directory_data = "../data"

# Check if the directory exists
if not os.path.exists(directory_data):
    # If it doesn't exist, create it
    os.makedirs(directory_data)
players_db = TinyDB('../data/Players database.json')
tournaments_db = TinyDB('../data/Tournaments database.json')


class Tournament:
    def __init__(self, name, venue, start_date, end_date,
                 current_round, registered_players, description, num_rounds=4):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.registered_players = registered_players
        self.description = description

    def entered_tournament(self):
        # create a dic for tournament
        return {
            'name': self.name,
            'venue': self.venue,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'description': self.description,
            'registered_players': self.registered_players,
        }

    def insert_tournament(self):
        # add tournament to database
        tournaments_db.insert(self.entered_tournament())
        print("Thank you! The tournament was added to the Chess club database")

    def search_tournament(title):
        tournament = Query()
        given_tournament = tournaments_db.search(tournament.name == title)[0]
        # why list with zero ??
        return given_tournament

    @staticmethod
    def load_tournaments():
        # get data for all tournament from database
        tournaments = []
        tournaments_db.all()
        for tournament in tournaments_db:
            tournaments.append(tournament)
        return tournaments
