import unittest
from Deck import Deck

class TestFunctionality(unittest.TestCase):

    def test_deck_should_have_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.deck),52)

    def test_deck_no_duplicates(self):
        deck = Deck().deck
        for i in range(0,len(deck)-2):
            for j in range(i+1,len(deck)-1):
                self.assertTrue(deck[i][0] != deck[j][0] or deck[i][1] != deck[j][1],"cards {} and {} where the same".format(deck[i],deck[j]))

    def test_deck_draw_should_remove_card(self):
        deck = Deck()
        card = deck.draw_card()
        self.assertTrue(len(deck.deck),51)
        for i in range(0,len(deck.deck)-1):
            self.assertTrue(deck.deck[i][0] != card[0] or deck.deck[i][1] != card[1],"cards {} and {} where the same".format(deck.deck[i],card))

if __name__ == '__main__':
    unittest.main()
