# This file tests the Game

from Lobby import Lobby
from Game import Game
from Player import Player
from Table import Table

# Create your lobby. In this lobby we will limit the number of players to 10
lobby = Lobby("RubesAndDonks", 20)

# Create a bunch of players and add them to the lobby
# In real life this would be done asynchronously
stackSize = 1000
try:
    lobby.addPlayerToWaitingList(Player(1, stackSize, "Joe Blow"))
    lobby.addPlayerToWaitingList(Player(2,stackSize, "Freddy Mercury"))
    lobby.addPlayerToWaitingList(Player(3,stackSize,"Harry Legg"))
except:
    print("Could not add a player to the lobby")

# Create the table and add the players to the table
tableNumber = 1
numSeats = 10
table = Table(tableNumber, numSeats)

numberOfEmptySeatsAtTable = table.getNumSeats() - table.getNumPlayers()

while (numberOfEmptySeatsAtTable > 0):
    # See if anyone is waiting in the lobby to fill the empty
    # seats
    player = lobby.removeNextPlayerFromWaitingList()
    if (player is not None):
        # add them to the table
        if (table.addPlayerToTable(player)):
            print("Successfully added player " + player.getName() + " to table " + table.getTableNumber())
            numberOfEmptySeatsAtTable = table.getNumSeats() - table.getNumPlayers()
        else:
            # This should not happen. It's an error
            print("ERROR. was not able to add player" + player.getName() + "to table " + table.getTableNumber)
            exit
    else:           
         # There are no more players in the lobby
        print("There are " + numberOfEmptySeatsAtTable + \
                " empty seats at the table left. However, there is no one left in the lobby")
        # break out of the while loop by setting the number of empty
        # seats to a negative number
        numberOfEmptySeatsAtTable = -1

# Now, play the game
game = Game(table)
game.play()

 