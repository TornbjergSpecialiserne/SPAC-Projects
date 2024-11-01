#include "Deck.cpp"
#include <vector>
#include <iostream>

using namespace std;

// Player class
class Player{
	private:
		vector<Card> hand;
		int card_count = 0;
		int last_count = 0;
		int aces = 0;
		bool stood = false;
		bool busted = false;

	public:
		Player(){}
		
		// Adds cards to player
		void add_card(Card c){hand.push_back(c); count_card(c);};

		// Shows the players hand. A dealer can hide their last drawn card
		string show_hand(bool hide_card = false){
			string cards = "";
			if(hide_card){
				cards = cards + hand[0].get_rank() + " of " + hand[0].get_suit() + "\t";
			}
			else{
				for(auto &card : hand){
					cards = cards + card.get_rank() + " of " + card.get_suit() + "\t";
				};
			}
			return cards;
		};
		
		//Counts the current card total. The last value drawn is stored
		void count_card(Card c){
			card_count = card_count + to_int(c.get_rank());
			if(last_count == 11 && to_int(c.get_rank()) == 11){last_count = 1;}
			else{last_count = to_int(c.get_rank());}
			while(card_count>21 && aces>0){
				card_count = card_count - 10;
				aces = aces - 1;
			}
			if(card_count>21){
				stood = true;
				busted = true;
			}
			else if(card_count==21){
				stood = true;
			}
		};
		
		//Converts the cards rank to an integer
		int to_int(string const& in_string){
			if(in_string == "2"){return 2;}
			if(in_string == "3"){return 3;}
			if(in_string == "4"){return 4;}
			if(in_string == "5"){return 5;}
			if(in_string == "6"){return 6;}
			if(in_string == "7"){return 7;}
			if(in_string == "8"){return 8;}
			if(in_string == "9"){return 9;}
			if(in_string == "10"){return 10;}
			if(in_string == "Jack"){return 10;}
			if(in_string == "Queen"){return 10;}
			if(in_string == "King"){return 10;}
			if(in_string == "Ace"){aces ++; return 11;}
			return 0;
		};
		
		//Returns the current card count. Dealer can hide their last value
		int get_card_count(bool hide){if(hide){return card_count-last_count;}else{return card_count;}};

		//Makse the player stand
		void stands(){stood=true;};

		bool has_stood(){return stood;};

		bool has_busted(){return busted;};
};
