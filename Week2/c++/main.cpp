#include <iostream>
#include "Player.cpp"
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

//Checks if all players has busted
bool all_players_has_busted(vector<Player> players){
	bool all_busted = true;

	//I like using auto might not be the most sound thing
	for(auto &player : players){
		all_busted = all_busted && player.has_busted();
	}
	return all_busted;
};

//Checks if all players has stood
bool all_players_has_stood(vector<Player> players){
	bool all_stood = true;
	for(auto &player : players){
		all_stood = all_stood && player.has_stood();
	}
	return all_stood;
};

//Displays the status of all players
void show_status(vector<Player> players, Player dealer, bool hide){
	system("cls");
	cout << "Dealer has: " + to_string(dealer.get_card_count(hide));
	cout << "\nDealer hand:\n";
	cout << dealer.show_hand(hide);
	string player_scores = "";
	string player_hands = "";
	int i = 1;
	for(auto &player : players){
		player_scores = player_scores + "Player " + to_string(i) + " count:" + to_string(player.get_card_count(false)) + "\t";
		player_hands = player_hands + "Player " + to_string(i) + ":" + + "\t" + player.show_hand(false) + "\n";
		i++;
	}
	cout << "\n" + player_scores;
	cout << "\n" + player_hands;
	cout << "\n--------------------------";
};

int main(){
	string input;
	int number_of_players;
	vector<Player> players;
	Player dealer;
	cout << "Please input number of players: \t";

	//Makes the user input the number of players
	while(getline(cin,input)){

		//error handling on the user input. It must be an integer and between 1 and 4
		try{
			number_of_players = stoi(input);
			if(0<number_of_players<5){
				for(int i = 0; i<number_of_players; i++){Player player; players.push_back(player);}
				break;
			}
			else{
				throw "Wrong number";
			}
		}
		catch(...){
			cout << "Please input an number between 1 and 4: \t";
		}
	
	}
	Deck deck;

	//Dealer and player draws 2 cards
	dealer.add_card(deck.draw_card());
	dealer.add_card(deck.draw_card());
	for(auto &player : players){
		player.add_card(deck.draw_card());	
		player.add_card(deck.draw_card());	
	}
	show_status(players, dealer,true);

	//Makes all players draw untill they either bust or stand
	while(!all_players_has_stood(players)){
		int i = 1;
		for(auto &player : players){
			if(player.has_stood()){i++; continue;}
			cout << "\nPlayer " + to_string(i) + ":\n1) Draw card 2) Stand";
			string input;
			while(getline(cin,input)){
				//Error handling on user input
				try{
					int command = stoi(input);
					switch(command){
						case 1:
							player.add_card(deck.draw_card());
							break;
						case 2:
							player.stands();
							break;
						default:
							throw("Wrong nuber");
					}
					break;
				}
				catch(...){
					cout << "Please input a : \t";
				}
			}
			i++;
			show_status(players,dealer,true);
		}
	}

	//If all players bust the house auto wins
	if(all_players_has_busted(players)){cout << "\nHouse always wins";}
	else{
		while(dealer.get_card_count(false)<17){dealer.add_card(deck.draw_card());}
		show_status(players,dealer,false);
		int i = 1;
		bool house_won = true;
		for(auto &player : players){
			if(!player.has_busted()){
				if(dealer.has_busted() || player.get_card_count(false)>dealer.get_card_count(false)){cout << "\nPlayer " + to_string(i) + " has won"; house_won = false;}
			}
			i++;
		}
		if(house_won){cout << "\nHouse always wins";}
	}

};
