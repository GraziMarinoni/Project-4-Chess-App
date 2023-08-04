class Match:

    def __init__(self, playerwhite, playerblack):
        self.playerwhite = playerwhite
        self.playerblack = playerblack
        self.whitepoints = 0
        self.blackpoints = 0

    def declare_winner(self, colour):
        if colour == "black":
            self.blackpoints = 1
            self.whitepoints = 0
        elif colour == "white":
            self.blackpoints = 0
            self.whitepoints = 1
        else:
            self.blackpoints = 0.5
            self.whitepoints = 0.5
