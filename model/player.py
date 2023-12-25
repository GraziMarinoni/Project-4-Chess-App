import os
from tinydb import TinyDB

# To get the current directory and then use the path to create the data directory
directory_data = f"{os.path.dirname(__file__)}/../data"

# Check if the directory exists
if not os.path.exists(directory_data):
    # If it doesn't exist, create it.
    os.makedirs(directory_data)
# Creates the player's database in the data directory
players_db = TinyDB(f"{directory_data}/Players database.json")


class Player:
    # instantiate the tournament model
    def __init__(self, first_name, last_name, date_birth, national_identifier):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.national_identifier = national_identifier

    def entered_player(self):
        # Return a dictionary of the player
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_birth': self.date_birth,
            'national_identifier': self.national_identifier,
           }

    def insert_player(self):
        # Add player to the players database
        players_db.insert(self.entered_player())
        print("\nThank you! The player was added to the Chess club database")
        print()

    @staticmethod
    def load_players():
        # Get data for all players from the players database
        return players_db.all()
