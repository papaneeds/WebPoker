from enum import Enum

# The player's state in this hand
class HandState(Enum):
    # IN_HAND means that the player is still in this hand
    IN_HAND = 1
    # FOLDED means that the player has folded
    FOLDED = 0

# The player's state at the table
class TableState(Enum):
    # The player is ready and willing to play
    ACTIVE = 1
    # The player is sitting out
    SITTING_OUT = 0

# The Player class encapsulates the characteristics of
# a poker player
class Player:
    def __init__(id, stack, name)
    self.id = id
    self.stack = stack
    self.name = name 
    self.cards = None