import os
from tinydb import TinyDB, Query
from tinydb.operations import add
import re

# to get the current working directory and then use the path to create the data directory
# Get the current project directory
directory_data = f"{os.path.dirname(__file__)}/../data"

# Check if the directory exists
if not os.path.exists(directory_data):
    # If it doesn't exist, create it.
    os.makedirs(directory_data)
players_db = TinyDB(f"{directory_data}/Players database.json")
tournaments_db = TinyDB(f"{directory_data}/Tournaments database.json")

tournament = Query()


class Tournament:
    # Instantiate the tournament model
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
        self.rounds = []
        self.paired_players = []

    def entered_tournament(self):
        # Returns a dictionary of the tournament
        return {
            'name': self.name,
            'venue': self.venue,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'description': self.description,
            'registered_players': self.registered_players,
            'rounds': [],
            'paired_players': []
        }

    def insert_tournament(self):
        # Add tournament to the tournaments database
        tournaments_db.insert(self.entered_tournament())
        print("Thank you! The tournament was added to the Chess club database")

    def search_tournament(title):
        # Search and return tournament by a given name.
        given_tournament = tournaments_db.search(tournament.name.matches(title, flags=re.IGNORECASE))[-1]
        return given_tournament

    def check_tournament(title):
        # Check the tournaments database for a tournament by a given name and return Ture or False.
        if tournaments_db.search(tournament.name.matches(title, flags=re.IGNORECASE)):
            return True
        else:
            return False

    def update_tournament(title, round_details, current_round, tour_pairs, end_date):
        # Update an existing tournament details after each round.
        tournaments_db.update(add('rounds', round_details), tournament.name == title)
        tournaments_db.update({'end_date': end_date}, tournament.name == title)
        tournaments_db.update({'current_round': current_round}, tournament.name == title)
        tournaments_db.update({'paired_players': tour_pairs}, tournament.name == title)

    @staticmethod
    def load_tournaments():
        # Get data for all tournaments from the tournaments database
        return tournaments_db.all()

    @staticmethod
    def unfinished_tournaments():
        # Search and return unfinished tournaments.
        unfinished_tours = tournaments_db.search(tournament.end_date.matches("Not finished yet"))
        return unfinished_tours
