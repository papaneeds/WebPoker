class BlindsAndAntes:
    def __init__(self):
        # The blinds and antes are defined by:
        # startTime 
        # [smallBlind, bigBlind]
        # ante
        # So, for example: [40, [50, 100], 10]
        # means:
        # At time=40 minutes after start of game
        # [smallBlind=50, bigBlind=100]
        # ante = 10
        #
        self.blindsAndAntes = { [0,  [10, 20], 0], \
                                [20, [20, 40], 0], \
                                [40, [50, 100], 10], \
                                [60, [100, 200], 20]  }

# The TexasHoldemGameDefinition encapsulates the
# characteristics of a Texas Hold'em game
class TexasHoldemGameDefinition:
    def __init__(self):
        # Texas hold'em has 
        self.numBettingRounds = 4

        # numCards holds the number of hole cards and
        # board cards to be dealt on each betting round
        # In the definition below there are:
        # bettingRound 0 (pre-flop) [2 hole cards, 0 board cards]
        # bettingRound 1 (flop)     [0 hole cards, 3 board cards]
        # bettingRound 2 (turn)     [0 hole cards, 1 board card]
        # bettingRound 3 (river)    [0 hole cards, 1 board card]
        self.numCards = [[2, 0], [0, 3], [0, 1], [0, 1]]

        # blinds holds the blinds and antes as a function
        # of time.
        self.blinds = BlindsAndAntes()


