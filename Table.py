
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

    # find the next occupied seat from the dealer
    # seat.
    # Returns:
    #   if successful returns the next occupied seatNumber index
    #   if unsuccessful returns -1 
    def getNextOccupiedSeat(self):
        for i in range(1, self.numSeats):
            seatIndex = (self.dealerSeat + i) % self.numSeats
            if (self.seats[seatIndex] is not None):
                # You've found the next unoccupied seat
                return seatIndex
        # If you got this far then there are no occupied seats
        # Return an error
        return -1


    # This function moves the dealer button to the next
    # player
    # Returns:
    #   if successful then return seatNumber of dealer
    #   else if unsuccessful then return -1
    def moveDealerButton(self):
        if self.numPlayers > 1 :
            self.dealerSeat = self.getNextOccupiedSeat()
            return self.dealerSeat
        else:
            return -1

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
            self.seats[positionOfFirstUnoccupiedSeat] = Seat(player)
            self.numPlayers += 1
            return True
        else:
            # There are no seats left at the table
            return False

    # This function returns the player in a particular seat number
    # Returns:
    #   If successful returns the player in seat number
    #   If unsuccessful (or the seat is unoccupied) returns None
    def getPlayer(self, seatNumber):
        if seatNumber < self.numSeats:
            return self.seats[seatNumber].getPlayer()
        else:
            return None

    # This function gets the player state at the table.
    # The player's table state tells you whether the 
    # player is ACTIVE or BUSTED
    # (that is, whether they had money at the start of the
    # hand or not)
    # Returns:
    #    If successful and instance of PlayerState
    #    If unsuccessful then None
    def getPlayerTableState(self, seatNumber):
        seat = self.seats[seatNumber]
        if seat is not None:
            return seat.getPlayerState()
        else:
            return None
            
    # This function returns a list of seatNumbers, starting
    # at the player to the left of the dealer (the small blind), 
    # which are currently occupied by
    # players that have tableState = ACTIVE
    # Returns: A list of active players
    def getPlayersInHand(self):
        occupiedSeatIndices = []
        for i in range(self.dealerSeat+1, self.numSeats+dealerSeat+1):
            seatNumber = i % self.numSeats
            if self.seats[seatNumber] is not None:
                # Check to make sure that is player is not busted
                if self.seats[seatNumber].playerState == PlayerState.ACTIVE:
                    occupiedSeatIndices.append(seatNumber)
        return occupiedSeatIndices
    
    # This function returns the current bet at a seat
    # Returns:
    #   If successful: The current bet at seatNumber
    #   If unsuccessful: None
    def getCurrentBet(self, seatNumber):
        if self.seats[seatNumber] is not None:
            return self.seats[seatNumber].getCurrentBet()
        else:
            return None

    # This function allows you to add to a current bet at seatNumber
    # Returns : True if successful
    #           False if unsuccessful
    def addToCurrentBet(self, seatNumber, amount):
        if self.seats[seatNumber] is not None:
            self.seats[seatNumber].addToCurrentBet(amount)
            return True
        else:
            return False  

    # This function allows you to set the current bet at seatNumber
    # Returns : True if successful
    #           False if unsuccessful
    def setCurrentBet(self, seatNumber, amount):
        if self.seats[seatNumber] is not None:
            self.seats[seatNumber].setCurrentBet(amount)
            return True
        else:
            return False        
    
    # This function sets the player state at the table.
    # The player's table state tells you whether the 
    # player is ACTIVE or BUSTED
    # (that is, whether they had money at the start of the
    # hand or not)
    # This function is intended to be called only once
    # at the start of a hand.
    # Returns: nothing
    def setPlayerTableState(self, seatNumber):
        seat = self.seats[seatNumber]
        if seat is not None:
            # Check to see if the player has money. 
            # If they have money then set their table state
            # to ACTIVE.
            # If they don't have money then set their table
            # state to BUSTED.
            if seat.getPlayer.getStack() > 0:
                seat.setPlayerState(PlayerState.ACTIVE)
            else:
                seat.setPlayerState(PlayerState.BUSTED)

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
        self.player = player
        self.currentBet = 0
        # The playerState variable holds an instance
        # of the PlayerState class
        self.playerState = None

    def setPlayerState(self, playerState):
        self.playerState = playerState

    def getPlayerState(self):
        return self.playerState

    def setCurrentBet(self, currentBet):
        self.currentBet = currentBet

    def getCurrentBet(self):
        return self.currentBet

    def getPlayer(self):
        return self.player

    def setPlayer(self, player):
        self.player = player

    def addToCurrentBet(self, amount)
        self.currentBet += amount

