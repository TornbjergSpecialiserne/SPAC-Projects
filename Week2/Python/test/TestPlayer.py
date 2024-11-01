import unittest
from Player import *

class TestFunctionality(unittest.TestCase):

    def test_player_change_bet(self):
        amount = 10
        player = Player()
        total = 500
        self.assertEqual(player.get_chips(), total)
        player.change_chips(-amount)
        self.assertEqual(player.get_chips(),total-amount)
        player.change_chips(amount)
        self.assertEqual(player.get_chips(),total)

    def test_player_add_card(self):
        player = Player()
        card = ("Ace","Spades")
        player.add_card(card)
        self.assertTrue(player.deck[0][0] == card[0] and player.deck[0][1] == card[1])

    def test_player_ace_should_round_down(self):
        player = Player()
        card1 = ("Ace","Spades")
        card2 = ("Ace","Hearts")
        card3 = (10,"Spades")
        player.add_card(card1)
        self.assertEqual(player.get_count(),11)
        player.add_card(card2)
        self.assertEqual(player.get_count(),12)
        player.add_card(card3)
        self.assertEqual(player.get_count(),12)

    def test_player_should_bust(self):
        player = Player()
        card = (10,"Spades")
        self.assertFalse(player.has_busted())
        player.add_card(card)
        player.add_card(card)
        player.add_card(card)
        self.assertEqual(player.get_count(),30)
        self.assertTrue(player.has_busted())

    def test_dealer_should_show_11(self):
        dealer = Player()
        card = ("Ace","Spades")
        dealer.add_card(card)
        dealer.add_card(card)
        self.assertEqual(dealer.get_count(True),11)

    def test_dealer_should_show_one_card(self):
        dealer = Player()
        card = ("Ace","Spades")
        card2 = (11,"Hearts")
        dealer.add_card(card)
        dealer.add_card(card2)
        hand = dealer.show_hand(True)
        self.assertEqual(len(hand),1)
        self.assertEqual(hand[0],"{} of {}".format(card[0],card[1]))

    def test_player_should_split(self):
        player = Player()
        card = ("Ace","Spades")
        self.assertFalse(player.get_can_split())
        player.add_card(card)
        player.add_card(card)
        self.assertTrue(player.get_can_split())

    def test_player_splits(self):
        player = Player()
        card = ("Ace","Spades")
        card2 = ("Ace","Hearts")
        player.add_card(card)
        player.add_card(card2)
        hand = player.show_hand()    
        self.assertEqual(hand[0],"{} of {}".format(card[0],card[1]))
        self.assertEqual(hand[1],"{} of {}".format(card2[0],card2[1]))
        (card3,card4,chips) = player.splits()
        self.assertTrue(card4[0] == card[0] and card4[1] == card[1])
        self.assertTrue(card3[0] == card2[0] and card3[1] == card2[1])
        self.assertEqual(chips,500)

    def test_splitplayer_add_cards(self):
        player = SplitPlayer()
        card = ("Ace","Spades")
        card2 = (9,"Hearts")
        player.add_card(card)
        player.add_card2(card2)
        hand = player.show_hand()
        print(player.show_hand())
        self.assertEqual(hand[0],"{} of {}".format(card[0],card[1]))
        self.assertEqual(hand[1],"\nHand 2:")
        self.assertEqual(hand[2],"{} of {}".format(card2[0],card2[1]))
        self.assertEqual(player.get_count(),11)
        self.assertEqual(player.get_count2(),9)


if __name__ == '__main__':
    unittest.main()
