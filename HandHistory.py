import Table
import treys

# This class encapsulates the hand history
class HandHistory:
    def __init__(self, table, handNumber, currentBlinds, currentBlindlevel, currentAntes):
        # The actionOnRound variable holds the action as a 
        # function of handRound
        self.actionOnRound = []
        self.currentBlindlevel = currentBlindlevel
        self.currentAntes = currentAntes
        self.currentBlinds = currentBlinds
        # This set holds the antes paid by each player
        # The key is the seatNumber and the value is the ante
        self.antesPaid = {}
        self.handNumber = handNumber
        self.table = table

    # This function prints out the hand history in the format
    # that Poker Stars prints out the hand history
    #
    # Input:
    #    seatIndexToPrintHoleCards: the seatIndex of the player that you want
    #               the hole cards printed for
    #               if seatIndexToPrintHoleCards = -1 then print all player's hole cards
    #    returns:
    #             if successful: a string 
    #             if unsuccessful: None (this can happen if the seatIndex
    #                is not occupied, 
    #                or doesn't exist at the table) 
    #                or no seats are occupied at the table
    def print(self, seatIndexToPrintHoleCards):

        # First some sanity checks
        # See if any seats are occupied at the table
        occupiedSeats = self.table.getOccupiedSeats(Table.IndexStart.INDEX_START_AT_ZERO)
        if len(occupiedSeats) == 0:
            return None
        # See if 
        # seatIndexToPrintHoleCards is an occupiedSeat or -1
        if not (('seatIndexToPrintHoleCards' in occupiedSeats) 
        or (seatIndexToPrintHoleCards == -1)):
            return None

        # Okay, so far so good. Construct the output string
        
        textOutput = '*********** # ' + self.handNumber + ' **************'
        textOutput += 'PokerStars Home Game Hand #211213343323: {Rubes and Donks} Tournament #2849064867, $20+$2 CAD Hold\'em No Limit - Level VII (60/120) - 2020/04/02 20:45:33 ET'
        textOutput += 'Table \'' + self.table.getTableNumber() + '\' 9-max Seat #' 
        + self.table.getDealerSeat() + ' is the button'

        # Now, loop over each player and print out their seat number,
        # name, and stack
        # Example format: Seat 2: theo lecrow (6540 in chips)
        for seatIndex in occupiedSeats:
            player = occupiedSeats['seatIndex'].getPlayer()
            textOutput += 'Seat ' + seatIndex 
            + ':' +  player.getName() 
            + '(' + player.getStack() + ' in chips)'
        
        # Loop over each player that has paid an Ante
        # Example format: Donktastic12: posts the ante 15
        for seatIndex in self.antesPaid:
            player = occupiedSeats['seatIndex'].getPlayer()
            textOutput += player.getName() 
            + ': posts the ante' + self.antesPaid[seatIndex]

        # Print out this player's Hole Cards
        # If seatIndex = -1 then print out all player's hole cards
        # Example format: 
        # *** HOLE CARDS ***
        # Dealt to Papaneeds [Qh 3h]
        textOutput += '*** HOLE CARDS ***'
        if (seatIndexToPrintHoleCards == -1):
            # Print out the Hole Cards of all the Players            
            for seatIndex in occupiedSeats:
                player = occupiedSeats['seatIndex'].getPlayer()           
                textOutput += 'Dealt to ' + player.getName() + '['
                if player.getCards() is not None:
                    playerCards = player.getCards()
                    # The cards are represented by a list of integers
                    # by the Treys module. Convert them, one-by-one, into
                    # string representations
                    for i in range(len(playerCards)):
                        strCard = treys.Card.int_to_str(card[i])
                        textOutput += strCard
                        if i < len(playerCards) - 1:
                            textOutput += ' '

                textOutput += ']'

        

                        

    def payAnte(self, seatNumber, ante):
        self.antesPaid[seatNumber]=ante

    def getAntesPaid(self):
        return self.antesPaid

    def setAntes(self, antes):
        self.antes = antes

    def getAntes(self):
        return self.antes

    def setBlinds(self, blinds):
        self.blinds = blinds

    def getBlinds(self):
        return self.blinds
        
