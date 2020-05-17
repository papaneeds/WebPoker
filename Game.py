# This class plays a game of poker

#from Player import Player
#from Table import Table
from datetime import datetime
# This is the poker hand dealer and hand evaluator
import treys
from treys import Deck

from HandHistory import HandHistory

#from TexasHoldemGameDefinition import TexasHoldemGameDefinition

class Game:
    def __init__(self, table, gameDefinition):
        self.table = table
        self.gameDefinition = gameDefinition
        self.handNumber = 0
        self.currentAntes = None
        self.currentAntes = []

    # This function actually plays the game of poker
    def play(self):
        # get the current time
        self.table.setTimeGameStart(datetime.now())

        # Choose the first non-null player as the dealer to start
        # the game.
        self.table.moveDealerButton()

        # Initialize the Hand History
        handHistory = HandHistory(self.gameDefinition.getNumBettingRounds())

        for handRound in range(self.gameDefinition.getNumBettingRounds()):
            currentMaxBet = 0
            currentBettorPosition = None
            playersInHand = None
            currentBlinds = None
            currentAntes = None
            currentBlindLevel = None

            # Use the deck implementation from Treys
            deck = Deck()

            # This is the number of blind positions
            # For example, if there is a small blind and a big blind
            # then this is 2
            numBlindPositions = len(self.gameDefinition.getBlindsAndAntes()[1])

            # This variable holds the seat number of the player
            # who is currently betting
            currentBettorPosition = None

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

                # Set the current blinds and current blind level
                [currentBlinds, currentBlindLevel] = gameDefininiton.getCurrentBlinds(self.table.getTimeGameStart())

                # Set the current antes
                self.currentAntes = gameDefininiton.getCurrentAntes(self.table.getTimeGameStart())

                # Initialize the hand history. This object will
                # hold the history of the way that the hand plays
                # out. The "print" function of this object is
                # used to see the hand history in human readable
                # format.
                handHistory = HandHistory(self.table, handNumber, 
                    currentBlinds, currentBlindLevel, currentAntes)

                # Make the players pay the antes
                for seatNumber in playersInHand:
                    ante = self.currentAntes
                    self.table.addToCurrentBet(seatNumber, ante)
                    handHistory.payAnte(seatNumber, ante)

                # Make each player pay the blinds
                # The playersInHand list contains all the players
                # in this hand starting at the player to the left of
                # the dealer.
                # The currentBlindsAndAntes[1] list contains a list
                # of the blinds
                # First the blinds
                for i in range(len(self.currentBlinds)):
                    blind = self.currentBlinds[i]
                    self.table.addToCurrentBet(playersInHand[i], blind)
                    handHistory.payBlind(seatNumber, blind)

                # The bets start out at the player to the right of the
                # big blind
                #   
                numBlindPositions = len(self.currentBlinds)
                currentBettorPosition = playersInHand[0 + numBlindPositions]

                # Now the dealer deals out the cards to each player
                # For this use the deck implementation from Treys
                for seatNumber in playersInHand:
                   # The number of cards each player is dealt
                    # is held in the 0 element of numCardsPerBettingRound
                    for cardNumber in range(self.gameDefinition.getNumCardsPerBettingRound()[handRound][0]):
                        playerCards = self.table.getCards(seatNumber)
                        drawCard = deck.draw(1)
                        playerCards.append(drawCard)

                    self.table.getPlayer(seatNumber).setCards(playerCards)

            # Now, the dealer goes around the table and
            # asks each player what their bet is
            continueWithNextBettor = True
            
            while continueWithNextBettor:
                # Ask the next bettor for their bet.
                # Send the bettor the information that 
                # they need in order to make a decision
                # This information is contained in the 
                # HandHistory.print() function.

            # Now, the dealer deals out the board cards
            # The number of board cards is in the numCardsPerBettingRound[handround][1]
            for cardNumber in range(self.gameDefinition.getNumCardsPerBettingRound()[handRound][1]):
                    boardCards = self.table.getBoardCards()
                    drawCard = deck.draw(1)
                    playerCards.append(drawCard)

                      
          

