#class for handeling a player.
class Player:
    def __init__(self):
        self.count = 0
        self.chips = 500
        self.deck = []
        self.aces = 0
        self.stood = False
        self.busted = False
        self.last_number = 0
        self.split = False
        self.can_split = False

    #Cheks if the player is a split player
    def get_split(self):
        return self.split

    #Return if the player can split
    def get_can_split(self):
        return self.can_split

    #If the player splits the cards are returned and the current chip amount is transfered
    def splits(self):
        return (self.deck.pop(),self.deck.pop(),self.chips)

    #Add or subtract chips from the player
    def change_chips(self, amount : int):
        self.chips = self.chips + amount

    #Return the total amount of chips
    def get_chips(self):
        return self.chips

    #The total is calculated after each draw. Kings jacks and queens count for 10 and ace 11 with a roll down effect. If the player draws two cards with the same value they will be able to split
    #According to the rule you can split even of you draw a jack and a 10, they just need the same value which seems silly but ohh well
    def calc_count(self,card : ()):
        match card[0]:
            case "Jack" | "King" | "Queen":
                self.count = self.count + 10
                if self.last_number == 10:
                    self.can_split = True
                self.last_number = 10

            case "Ace":
                self.count = self.count + 11
                #If the dealer draws two aces it should only subtract the ace that gets rolled down
                if self.last_number == 11:
                    self.can_split = True
                    self.last_number = 1
                else:
                    self.last_number = 11
                self.aces = self.aces + 1
            case _:
                self.count = self.count + card[0]
                if self.last_number == card[0]:
                    self.can_split = True
                self.last_number = card[0]
        if self.count>21:
            while self.count > 21 and self.aces > 0:
                self.count = self.count - 10
                self.aces = self.aces - 1
            if self.count>21:
                self.busted = True
                self.stands()
        elif self.count==21:
            self.stands()

    #Gets the running total of the player. Hide hides the last card drawn for the dealer
    def get_count(self,hide = False):
        if hide:
            return self.count-self.last_number
        else:
            return self.count

    #Initiates the player for a new round, removinf their deck, card count and other information
    def new_round(self):
        self.deck = []
        self.count = 0
        self.aces = 0
        self.stood = False
        self.busted = False
        self.last_number = 0
        self.split = False
        self.can_split = False

    #Adds a card to the players hand
    def add_card(self,card : ()):
        self.deck.append(card)
        self.calc_count(card)

    #Gets the current cards in the players hand
    def show_hand(self,hide = False):
        hand = []
        if hide:
            card = self.deck[0]
            hand.append("{} of {}".format(card[0],card[1]))
        else:    
            for card in self.deck:
                hand.append("{} of {}".format(card[0],card[1]))
        return hand

    #Return if the player has stood
    def has_stood(self):
        return self.stood

    #Makes the player stand
    def stands(self):
        self.stood = True

    def is_out(self):
        return self.chips <= 0

    #Checks if the player has busted
    def has_busted(self):
        return self.busted

#Class representing a player that chose to split. Inherits the functions above and gets similar functions for teir second hand
class SplitPlayer(Player):
    def __init__(self):
        self.last_number = 0
        self.count = 0
        self.count2 = 0
        self.chips = 500
        self.deck = []
        self.deck2 = []
        self.aces = 0
        self.aces2 = 0
        self.stood = False
        self.stood2 = False
        self.busted = False
        self.busted2 = False
        self.split = True

    #The total is calculated after each draw. Kings jacks and queens count for 10 and ace 11 with a roll down effect
    def calc_count2(self,card : ()):
        match card[0]:
            case "Jack" | "King" | "Queen":
                self.count2 = self.count2 + 10
            case "Ace":
                self.count2 = self.count2 + 11
                self.aces2 = self.aces2 + 1
            case _:
                self.count2 = self.count2 + card[0]
        if self.count2>21:
            while self.count2 > 21 and self.aces2 > 0:
                self.count2 = self.count2 - 10
                self.aces2 = self.aces2 - 1
            if self.count2>21:
                self.busted2 = True
                self.stands2()
        elif self.count2==21:
            self.stands2()

    #Gets the running total of the player. Hide hides the last card drawn for the dealer
    def get_count2(self):
        return self.count2

    #Adds a card to the players hand
    def add_card2(self,card : ()):
        self.deck2.append(card)
        self.calc_count2(card)

    #Gets the current cards in the players hands
    def show_hand(self,hide = False):
        hand = []
        for card in self.deck:
            hand.append("{} of {}".format(card[0],card[1]))
        hand.append("\nHand 2:")
        for card in self.deck2:
            hand.append("{} of {}".format(card[0],card[1]))
        return hand

    #Return if the player has stood
    def has_stood2(self):
        return self.stood2

    #Makes the player stand
    def stands2(self):
        self.stood2 = True

    #Sets the players chips. Used for when a player splits to set it to the amount the original player had
    def set_chips(self,chips):
        self.chips = chips

    #Checks if the player has busted
    def has_busted2(self):
        return self.busted
