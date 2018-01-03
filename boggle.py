import random

boggleDice = [
	['M','E','D','A','P','C'],
	['L','E','K','G','U','Y'],
	['L','A','R','E','S','C'],
	['P','U','L','E','S','T'],
	['N','S','P','H','E','I'],
	['T','N','K','D','U','O'],
	['S','O','W','E','N','D'],
	['M','A','R','O','S','H'],
	['F','O','R','I','B','X'],
	['Y','E','E','I','F','H'],
	['L','I','B','A','T','Y'],
	['O','I','A','A','T','C'],
	['Q','A','M','O','J','B'],
	['Z','D','V','N','A','E'],
	['R','W','G','L','I','U'],
	['E','V','I','T','G','N']
]

def makeBoard():
	diceOrder = list(range(16))
	random.shuffle(diceOrder)
	return [[random.choice(boggleDice[diceOrder[4*i+j]]) for j in range(4)] for i in range(4)]

def printBoard(boggleBoard):
	for row in boggleBoard:
		for letter in row:
			print(letter,end='')
		print()
	
def main():
	boggleBoard = makeBoard()
	printBoard(boggleBoard)

if __name__ == "__main__":
	main();
