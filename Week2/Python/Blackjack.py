from Deck import *
from Player import *
import os
import sys
import math

#Instigates a new round for all players
def start_new_round(players : [], dealer : Player):
    i = 0
    for player in players:
        if player.get_split():
            normal_player = Player()
            normal_player.change_chips(player.get_chips()-500)
            player = normal_player
            players[i] = player
        player.new_round()
        i = i + 1
    dealer.new_round()

#Checks if all players has 0 chips left
def all_players_out(players : []):
    all_out = True
    for player in players:
        all_out = all_out and player.is_out()
    return all_out


#Checks if all players has busted
def all_players_busted(players : []):
    all_busted = True
    for player in players:
        all_busted = all_busted and player.has_busted()
        if player.get_split():
            all_busted = all_busted and player.has_busted()
    return all_busted

#Checks if all players stood
def all_players_stood(players : []):
    all_stood = True
    for player in players:
        all_stood = all_stood and player.has_stood()
        if player.get_split():
            all_stood = all_stood and player.has_stood2()
    return all_stood

#Displays the current cards drawn and the total count for each player. The second dealer card is hidden
def show_status(players : [], dealer : Player, bets : [], hide_dealer = True):
    os.system("cls")
    print("The dealer has: {}".format(dealer.get_count(hide_dealer)))
    print("Cards drawn:")
    dealer_hand = dealer.show_hand(hide_dealer)
    dealer_cards = ""
    for card in dealer_hand:
        dealer_cards = dealer_cards + card + "\t"
    print(dealer_cards + "\n")
    player_hands = []

    #Creates empty strings to fill with player information
    player_have_text = ""
    player_bet_status = ""
    player_chip_status = ""
    i = 1
    for player in players:
        player_hands.append(player.show_hand())

        #If a player is split it needs to show the value of the second hand
        if player.get_split():
            player_have_text = player_have_text + "Player {} has: {} and {} ".format(i,player.get_count(),player.get_count2()) + "\t"
        else:
            player_have_text = player_have_text + "Player {} has: {}  ".format(i,player.get_count()) + "\t\t"
        player_chip_status = player_chip_status + "Player {} total {}".format(i,player.get_chips()) + "\t\t"
        if bets[i-1] != 0:
            player_bet_status = player_bet_status + "Player {} bet {}  ".format(i,bets[i-1]) + "\t\t"
        else:
            player_bet_status = player_bet_status + "Player {} folded".format(i,bets[i-1]) + "\t\t\t"
        i = i +1
    i = 1

    #Collects information on the players hands
    player_cards = ""
    for hands in player_hands:
        player_cards = player_cards + "Player {} cards:".format(i)
        for card in hands:
            player_cards = player_cards + "\t" + card
        player_cards = player_cards + "\n\n"
        i = i + 1
    print(player_have_text)
    print(player_chip_status)
    print(player_bet_status + "\n")
    print(player_cards+"\n")
    print("------------------------------")
    
if __name__ == "__main__":
    os.system("cls")
    print("Please choose number of players (max 4):")
    #User input for number of players max 4 and min 1
    number_of_players = input()
    player_input = False
    while not player_input:
        if number_of_players == "q":
            sys.exit()
        #Error handling for user input
        try:
            number_of_players = int(number_of_players)
            if number_of_players > 4 or number_of_players<=0:
                print("Try again")
                number_of_players = input()
                continue
            players = []
            i=0
            while i < number_of_players:
                players.append(Player())
                i = i + 1
            player_input = True
        except:
            print("Try again")
            number_of_players = input()
    #A dealer is a normal player with no human input
    dealer = Player()

    #Gets a new deck
    deck = Deck()
   
    #Game runs aslong as anyplayer can still bet
    while not all_players_out(players):
        bets = []
        i = 1
        #Players writes their bets
        for player in players:
            if not player.is_out():
                print("Current chips {}".format(player.get_chips()))
                print("player {} enter bet or type fold:".format(i))
                player_betted = False
                while not player_betted:
                    #Error handling on user input
                    try:
                        player_input = input()
                        if player_input == "fold":
                            player.stands()
                            bets.append(0)
                            player_betted = True
                            continue
                        elif player_input == "q":
                            sys.exit()
                        bet = int(player_input)
                        if bet > player.get_chips():
                            print("Bet is higher than your current chips")
                        elif bet <= 0:
                            print("Bet should be a positive integer")
                        else:
                            player.change_chips(-bet)
                            bets.append(bet)
                            player_betted = True
                    except SystemExit:
                        sys.exit()
                    except:
                        print("Please enter a number or type stand")
            else:
                player.stands()
                bets.append(0)
            i = i + 1
        
        #All players draw two cards
        dealer.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())
        
        i = 1
        for player in players:
            if not player.is_out():
                player.add_card(deck.draw_card())
                player.add_card(deck.draw_card())

                #If a player can split they can choose to do so
                if player.get_can_split():
                    print("Player {} can split press 1 to do so".format(i))
                    print("Cards drawn:")
                    hand = player.show_hand()
                    print(hand[0] + " " + hand[1])
                    command = input()
                    if command == "1":
                        #Gets information on the cards drawn before the split and the chip amount
                        (card,card2,chips) = player.splits()
                        player = SplitPlayer()

                        #Replaces the player with a split player and draws another card for both hands
                        player.add_card(card)
                        player.add_card(deck.draw_card())
                        player.add_card2(card2)
                        player.add_card2(deck.draw_card())
                        player.set_chips(chips-bets[i-1])
                        players[i-1] = player
                        print("Player split")
            i = i+1        
        show_status(players,dealer,bets)

        #The maximum draw aim for the dealer is 17
        smallest_stand = 17
        
        #Each player can choose to draw a card or stand
        while not all_players_stood(players):
            i = 1
            for player in players:
                if not player.has_stood():
                    valid_input = False
                    while not valid_input:
                        print("Player {}".format(i))

                        #A player can double down on their first turn. A split player cannout double down in this version
                        if len(player.show_hand()) < 3:
                            print("1) To draw 2) To stand 3) To double down")
                        else:
                            print("1) To draw 2) To stand")
                        command = input()
                        match command:
                            case "1":
                                player.add_card(deck.draw_card())
                                valid_input = True
                            case "2":
                                player.stands()
                                valid_input = True
                                smallest_stand = min(smallest_stand,player.get_count())
                            case "3":

                                #Ensures that a player can not double down on subsequent turns
                                if len(player.show_hand()) < 3:
                                    player.add_card(deck.draw_card())
                                    player.change_chips(-bets[i-1])
                                    bets[i-1] = 2*bets[i-1]
                                    valid_input = True
                                    player.stands()
                            case "q":
                                sys.exit()

                            case _:
                                print("Invalid input")
                    show_status(players,dealer,bets)

                #A split player should be able to draw a card to their second hand
                if player.get_split():
                    if not player.has_stood2():
                        valid_input = False
                        while not valid_input:
                            print("Player {} hand 2".format(i))
                            print("1) To draw 2) To stand")
                            command = input()
                            match command:
                                case "1":
                                    player.add_card2(deck.draw_card())
                                    valid_input = True
                                case "2":
                                    player.stands2()
                                    valid_input = True
                                    smallest_stand = min(smallest_stand,player.get_count2())
                                case "q":
                                    sys.exit()
                                case _:
                                    print("Invalid input")
                        show_status(players,dealer,bets)
                i = i + 1

        #If all players bust the house automatically wins (house can't bust with two cards)        
        if all_players_busted(players):
            print("house won")
        else:
            #Dealer draws untill they reach past the smallest stand
            while dealer.get_count()<smallest_stand:
                dealer.add_card(deck.draw_card())
            show_status(players,dealer,bets, hide_dealer = False)
            house_won = True
            i = 1
            for player in players:
                #Players scoring higher than a non busting dealer wins
                if not player.has_busted():
                    if player.get_count() == 21 and len(player.deck) == 2:

                        #A natural 21 beats all besides a natural 21 dealer and pays out 3:2. Draw means you get the bet back
                        if dealer.get_count() == 21 and len(dealer.show_hand()) == 2:
                            print("Player {} and dealer tied".format(i))
                            player.change_chips(bets[i-1])
                            house_won = False
                        else:
                            print("Player {} got blackjack!".format(i))
                            house_won = False
                            player.change_chips(math.ceil(2.5*bets[i-1]))
                    elif dealer.get_count()>21  or player.get_count()>dealer.get_count():
                        print("Player {} won".format(i))
                        player.change_chips(2*bets[i-1])
                        house_won = False
                    elif dealer.get_count() == player.get_count():
                        print("Player {} and dealer tied".format(i))
                        player.change_chips(bets[i-1])
                        house_won = False

                #Split players can win with their second hand
                if player.get_split():
                    if not player.has_busted2():
                        if player.get_count2() == 21 and len(player.deck2) == 2:
                            if dealer.get_count() == 21 and len(dealer.show_hand()) == 2:
                                print("Player {} hand 2 and dealer tied".format(i))
                                player.change_chips(bets[i-1])
                                house_won = False
                            else:
                                print("Player {} hand 2 got blackjack!".format(i))
                                house_won = False
                                player.change_chips(math.ceil(2.5*bets[i-1]))
                        elif dealer.get_count()>21  or player.get_count2()>dealer.get_count():
                            print("Player {} hand 2 won".format(i))
                            player.change_chips(2*bets[i-1])
                            house_won = False
                        elif dealer.get_count() == player.get_count():
                            print("Player {} hand 2 and dealer tied".format(i))
                            player.change_chips(bets[i-1])
                            house_won = False
                i = i + 1

            if house_won:
                print("House won")
        start_new_round(players,dealer)
