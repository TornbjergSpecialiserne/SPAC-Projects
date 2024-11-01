#include <iostream>
#include <string>
#include <algorithm>
#include <random>
#include <chrono>
#include <array>

using namespace std;

//Class representing a card
class Card{
	private:
		string suit;
		string rank;

	public:
		Card() : suit(""), rank(""){}
		Card(string s, string r) : suit(s), rank(r){}

		void set_suit(string s){suit = s;}
		void set_rank(string r){rank = r;}

		string get_suit(){return suit;}
		string get_rank(){return rank;}
};

//Class representing a deck
class Deck{
	private:
		array<Card,52> deck;
		int draw_amount = 0;
		string suits[4] = {"hearts","diamonds","spades","clubs"};
		string ranks[13] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
	public:
		//When a deck is made, it is filled with 52 cards and shuffled
		Deck(){
			for(int i=0; i<4; i++){
				for(int j=0;j<13;j++){
					deck[i * 13 + j].set_suit(suits[i]);
					deck[i * 13 + j].set_rank(ranks[j]);
				}
			}
			unsigned seed = chrono::system_clock::now().time_since_epoch().count();
			shuffle(deck.begin(), deck.end(), default_random_engine(seed));
		}

		//Returns the current card from the stack and incriments the pointer by one
		Card draw_card(){
			Card card = deck[draw_amount];
			draw_amount++;
			return card;
		}
};
