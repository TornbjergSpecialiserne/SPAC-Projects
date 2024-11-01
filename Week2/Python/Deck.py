import random

#Creates a new deck and shuffles it
class Deck:
    def __init__(self):
        self.suits = ["spades","clubs","diamonds","hearts"]
        self.ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
        self.generate_deck()


    def shuffle(self):
        random.shuffle(self.deck)
    
    #Generates a new deck of 52 playing cars
    def generate_deck(self):
        self.deck = []
        for suit in self.suits:
           for rank in self.ranks:
                self.deck.append((rank,suit))
        self.shuffle()

    #Draws a card which is removed from the deck
    def draw_card(self):
        card = self.deck.pop()
        return card

