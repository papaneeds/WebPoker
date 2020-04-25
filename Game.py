# This class plays a game of poker

#from Player import Player
#from Table import Table
from datetime import datetime
#from TexasHoldemGameDefinition import TexasHoldemGameDefinition

class Game:
    def __init__(self, table, gameDefinition):
        self.table = table
        self.gameDefinition = gameDefinition
        self.handNumber = 0

    # This function actually plays the game of poker
    def play(self):
        # get the current time
        self.table.setTimeGameStart(datetime.now())

        # Choose the first non-null player as the dealer to start
        # the game.
        self.table.moveDealerButton()

        for handRound in range(self.gameDefinition.getNumBettingRounds()):
            currentMaxBet = 0
            currentBettorPosition = None

            # When you are just starting out the hand then
            # you have to initialize a bunch of things
            if handRound == 0:
                # Go around the table and
                # set whether the player has chips or is busted
                for seatNumber in range(self.table.getNumSeats()):
                    self.table.setPlayerTableState(seatNumber)
                            



