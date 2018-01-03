/*
 * Find all words in a boggle config
 *
 * Other challenges would be to see what words can be made with the boggle dice  * (solve every game), find just the longest word, adjust the boggle dice to
 * improve gameplay, ...
 */

#include <iostream>
#include <algorithm>
#include <random>
#include <vector>

const char boggleDice[16][6] = {
	{'M','E','D','A','P','C'},
	{'L','E','K','G','U','Y'},
	{'L','A','R','E','S','C'},
	{'P','U','L','E','S','T'},
	{'N','S','P','H','E','I'},
	{'T','N','K','D','U','O'},
	{'S','O','W','E','N','D'},
	{'M','A','R','O','S','H'},
	{'F','O','R','I','B','X'},
	{'Y','E','E','I','F','H'},
	{'L','I','B','A','T','Y'},
	{'O','I','A','A','T','C'},
	{'Q','A','M','O','J','B'},
	{'Z','D','V','N','A','E'},
	{'R','W','G','L','I','U'},
	{'E','V','I','T','G','N'}
};

void printBoard() {

	auto rng = std::default_random_engine {};
	rng.seed(time(NULL));

	std::vector<int> diceOrder;
	for(int i = 0; i < 16; i++) diceOrder.push_back(i);

	for(int i = 0; i < 16; i++) std::cout << diceOrder[i] << " ";
	std::cout << "\n";

	std::shuffle(std::begin(diceOrder), std::end(diceOrder), rng);

	for(int i = 0; i < 16; i++) std::cout << diceOrder[i] << " ";
	std::cout << "\n";

}
	
int main(int argc, char **argv) {

	std::srand(unsigned(time(NULL)));
	printBoard();

	return 0;

}
