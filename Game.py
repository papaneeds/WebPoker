# This class plays a game of poker

from Player import Player
from Table import Table
from TexasHoldemGameDefinition import TexasHoldemGameDefinition
from datetime import datetime

class Game:
    def __init__(self, table):
        self.table = table

    # This function actually plays the game of poker
    def play(self):
        # get the current time
        self.table.setTimeGameStart(datetime.now())

        # continue on with the game from here