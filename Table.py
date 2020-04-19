
from enum import Enum

class PlayerState(Enum):
    # ACTIVE means that at the start of the hand the player had money
    ACTIVE = 1
    # BUSTED means that at the start of the hand the player had no money
    BUSTED = 0

# The Table class encapsulates the characteristics
# of a poker table
class Table:
    def __init__(self, tableNumber, numSeats)
          self.tableNumber = tableNumber
          self.numSeats = numSeats
          self.numPlayers = 0
          # The seats list stores all the information about
          # who is sitting in which seat
          self.seats = {}
          # The seat number of the dealer
          self.dealerSeat = 0
          # The time since the game started
          self.timeGameStart = None
          # The current pot
          self.pot = 0
          # The current board cards
          self.boardCards = None

# The Seat class encapsulates the characteristics
# of a seat at the table.
class Seat:
    def __init__(self, player)
        self.plater = player
        self.currentBet = 0
        # The playerState variable holds an instance
        # of the PlayerState class
        self.playerState = None

