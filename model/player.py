import os
from tinydb import TinyDB, Query

directory_data = "../data"

# Check if the directory exists
if not os.path.exists(directory_data):
    # If it doesn't exist, create it
    os.makedirs(directory_data)
players_db = TinyDB('../data/Players database.json')


class Player:
    def __init__(self, first_name, last_name, date_birth, national_identifier):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.national_identifier = national_identifier

    def entered_player(self):
        #  create a dic for player
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_birth': self.date_birth,
            'national_identifier': self.national_identifier,
        }

    def insert_player(self):
        # add player to database
        players_db.insert(self.entered_player())
        print("Thank you! The player was added to the Chess club database")
        print()

    @staticmethod
    def load_players():
        # get all players from database
        players = []
        players_db.all()
        for player in players_db:
            players.append(player)
        return players
