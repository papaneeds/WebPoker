from datetime import datetime, timedelta

class BlindsAndAntes:
    def __init__(self):
        # The blinds and antes are defined by:
        # startTime (expressed as hour,minute,second in a datetime object)
        # [smallBlind, bigBlind]
        # ante
        # So, for example: [40, [50, 100], 10]
        # means:
        # At time=40 minutes after start of game
        # [smallBlind=50, bigBlind=100]
        # ante = 10
        #
        self.blindsAndAntes = [[ 0,  [10, 20], 0], \
                                [20, [20, 40], 0], \
                                [40, [50, 100], 10], \
                                [60, [100, 200], 20]  ]

    def getBlindsAndAntes(self):
        return self.blindsAndAntes

# The TexasHoldemGameDefinition encapsulates the
# characteristics of a Texas Hold'em game
class TexasHoldemGameDefinition:
    def __init__(self):
        # Texas hold'em has 
        self.numBettingRounds = 4

        # numCardsPerBettingRound holds the number of hole cards and
        # board cards to be dealt on each betting round
        # In the definition below there are:
        # bettingRound 0 (pre-flop) [2 hole cards, 0 board cards]
        # bettingRound 1 (flop)     [0 hole cards, 3 board cards]
        # bettingRound 2 (turn)     [0 hole cards, 1 board card]
        # bettingRound 3 (river)    [0 hole cards, 1 board card]
        self.numCardsPerBettingRound = [[2, 0], [0, 3], [0, 1], [0, 1]]

        # blindsAndANtes holds the blinds and antes as a function
        # of time.
        self.blindsAndAntes = BlindsAndAntes()

    def getNumBettingRounds(self):
        return self.numBettingRounds

    # Returns the current blinds and antes structure
    # Not recommended to use this function as the internal
    # structure of blindsAndAntes may change and break your
    # code
    def getBlindsAndAntes(self):
        return self.blindsAndAntes.getBlindsAndAntes()

    # Returns a list of the current blinds and antes at currentTime
    # indexed by 0 being the player immediately clockwise from 
    # the dealer, and the current blind level (indexed starting from
    # 0)
    def getCurrentBlindsAndAntes(self, timeGameStart):
        # Find the time range that bounds timeGameStart
        for i in range(len(self.blindsAndAntes.getBlindsAndAntes()[0])-1):
            # Element [i][0] is the time
            # Element [i][1] contains the blinds
            # Element [i][2] contains the ante
            currentTime = datetime.now()
            timeIntervalStart = timeGameStart+ timedelta(minutes=self.blindsAndAntes.getBlindsAndAntes()[i][0])
            timeIntervalEnd = timeGameStart+ timedelta(minutes=self.blindsAndAntes.getBlindsAndAntes()[i+1][0])
            if currentTime <= timeIntervalEnd and \
                currentTime > timeIntervalStart:
                    return [self.blindsAndAntes.getBlindsAndAntes()[i][1], 
                    self.blindsAndAntes.getBlindsAndAntes()[i][2], i]
        # Else return the largest blind (assume that the blinds
        # are maxed out)
        maxIndex = len(self.blindsAndAntes)-1
        return [self.blindsAndAntes.getBlindsAndAntes()[maxIndex][1], 
            self.blindsAndAntes.getBlindsAndAntes()[maxIndex][2], maxIndex]

    # This function returns the number of cards that are dealt per
    # betting round.
    # Input: bettingRound
    # Output: a list of [numHoleCards, numBoardCards] for this betting
    #         round.
    def getNumCardsPerBettingRound(self, bettingRound):
        return self.numCardsPerBettingRound[bettingRound]

"""     # Returns a list of the current blinds at currentTime
    # indexed by 0 being the player immediately clockwise from 
    # the dealer, and the current blind level (indexed starting from
    # 0)
    def getCurrentBlinds(self, timeGameStart):
        # Find the time range that bounds timeGameStart
        for i in range(len(self.blindsAndAntes[0])-1):
            # Element [i][0] is the time
            # Element [i][1] contains the blinds
            currentTime = datetime.now()
            timeIntervalStart = timeGameStart+ timedelta(minutes=self.blindsAndAntes[i][0])
            timeIntervalEnd = timeGameStart+ timedelta(minutes=self.blindsAndAntes[i+1][0])
            if currentTime <= timeIntervalEnd and \
                currentTime > timeIntervalStart:
                    return [self.currentBlindsAndAntes[i][1], i]
        # Else return the largest blind (assume that the blinds
        # are maxed out)
        return self.blindsAndAntes[len(self.blindsAndAntes)-1][1]


    # Returns the current antes at the currentTime
    #  
    def getCurrentAntes(self, timeGameStart):
        # Find the time range that bounds timeGameStart
        for i in range(len(self.blindsAndAntes[0])-1):
            # Element [i][0] is the time
            # Element [i][2] contains the antes
            currentTime = datetime.now()
            timeIntervalStart = timeGameStart+ timedelta(minutes=self.blindsAndAntes[i][0])
            timeIntervalEnd = timeGameStart+ timedelta(minutes=self.blindsAndAntes[i+1][0])
            if currentTime <= timeIntervalEnd and \
                currentTime > timeIntervalStart:
                    return self.currentBlindsAndAntes[i][2]
        # Else return the last ante (assume that the antes
        # are maxed out)
        return self.blindsAndAntes[len(self.blindsAndAntes)-1][2] """





