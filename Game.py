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
            playersInHand = None
            currentBlindsAndAntes = None

            # When you are just starting out the hand then
            # you have to initialize a bunch of things
            if handRound == 0:
                # Set whether the player has chips or is busted.
                # If the player does not have chips then then
                # cannot participate in this hand (they are BUSTED
                # and must re-buy before they can participate in a
                # subsequent hand) 
                self.table.setPlayerTableState()

                # Get the list of players that are currently 
                # in the hand. The first element of this list
                # is the dealer
                playersInHand = self.table.getPlayersInHand()

                # Go around the table, starting at the seat to
                # the left of the dealer (the small blind)
                # and for each participating
                # player set their current bets to zero (0)
                for seatNumber in playersInHand:
                    self.table.setCurrentBet(seatNumber, 0)

                # Set the current blinds
                # The blinds are based on time. So, get the
                # current time and see how long it's been since
                # the game started
                timeSinceStartOfGame = datetime.now() - self.table.getTimeGameStart()
                # iterate through the blinds to see which blind level is applicable
                for blindsAndAntes in self.gameDefinition.getBlindsAndAntes():
                    # The first element is the time
                    if blindsAndAntes[0] <= timeSinceStartOfGame and \
                        blindsAndAntes[1] > timeSinceStartOfGame:
                        self.currentBlindsAndAntes = blindsAndAntes[0]

                # Make each player pay the blinds and antes
                # The playersInHand list contains all the players
                # in this hand starting at the player to the left of
                # the dealer.
                # The currentBlindsAndAntes[1] list contains a list
                # of the blinds
                # First the blinds
                for i in range(len(self.currentBlindsAndAntes)):
                    self.table.addToCurrentBet(playersInHand[i], self.currentBlindsAndAntes[i])
                # And then the antes
                # The antes are in currentBlindsAndAntes[2]
                for seatNumber in playersInHand:
                    self.table.addToCurrentBet(seatNumber, self.currentBlindsAndAntes[2])

            # Now the dealer deals out the cards    
          

