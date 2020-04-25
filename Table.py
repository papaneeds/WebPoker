
from enum import Enum

class PlayerState(Enum):
    # ACTIVE means that at the start of the hand the player had money
    ACTIVE = 1
    # BUSTED means that at the start of the hand the player had no money
    BUSTED = 0

# The Table class encapsulates the characteristics
# of a poker table
class Table:
    def __init__(self, tableNumber, numSeats):
          self.tableNumber = tableNumber
          self.numSeats = numSeats
          self.numPlayers = 0
          # The seats list stores all the information about
          # who is sitting in which seat.
          # Initialize each seat to None
          self.seats = [None]*self.numSeats
          # The seat number of the dealer
          self.dealerSeat = 0
          # The time since the game started
          self.timeGameStart = None
          # The current pot
          self.pot = 0
          # The current board cards
          self.boardCards = None

    def getTableNumber(self):
        return self.tableNumber

    def getNumSeats(self):
        return self.numSeats

    def getNumPlayers(self):
        return self.numPlayers

    def getTimeGameStart(self):
        return self.timeGameStart

    def setTimeGameStart(self, timeGameStart):
        self.timeGameStart = timeGameStart

    # This function adds player to the table.
    # If there is no room at the table this function
    # returns False. 
    # If the player was successfully added then this function
    # returns True
    def addPlayerToTable(self, player):
        numEmptySeats = self.seats.count(None)
        if numEmptySeats > 0 :
            # seat the player at the first unoccupied seat
            positionOfFirstUnoccupiedSeat = self.seats.index(None)
            self.seats[positionOfFirstUnoccupiedSeat] = player
            self.numPlayers += 1
            return True
        else:
            # There are no seats left at the table
            return False

    # This function removes a player from the table.
    # This function returns:
    #    True if the player was successfully removed
    #    False if the player didn't exist at the table
    def removePlayerFromTable(self, player):
        # find the position that this player is sitting in
        try:
            positionOfPlayer = self.seats.index(player)
        except:
            return False
        finally:
            # The player is sitting at the table
            # at positionOfPlayer. Set that seat to None.
            self.seats[positionOfPlayer] = None 
            return True

# The Seat class encapsulates the characteristics
# of a seat at the table.
class Seat:
    def __init__(self, player):
        self.plater = player
        self.currentBet = 0
        # The playerState variable holds an instance
        # of the PlayerState class
        self.playerState = None

