# This file abstracts the Lobby for a poker game

import queue
from Player import Player

class Lobby:
    def __init__(self, lobbyName, lobbyCapacity):
        self.lobbyName = lobbyName
        self.lobbyCapacity = lobbyCapacity
        self.waitingList = queue.Queue(lobbyCapacity)

    # This function adds a player to the lobby.
    # The player can be added to the waiting
    # list until the lobby is full
    # Returns:
    #  True if successful
    #  False if unsuccessful (the table is full)
    def addPlayerToWaitingList(self, Player):
        try:
            self.waitingList.put(Player, False)
        except:
            return False
        finally:
            return True

    # This function returns the next player from the waiting list
    # Returns:
    #   player if successful
    #   None if unsuccessful 
    def removeNextPlayerFromWaitingList(self):
        try:
            nextPlayer = self.waitingList.get(False)
            return nextPlayer
        except:
            return None



        



