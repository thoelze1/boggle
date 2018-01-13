# Current obstacle is to find out how to store partial solutions. 
# https://math.stackexchange.com/questions/92555/counting-the-number-of-paths-on-a-graph

import random

wordsFilePath = "/usr/share/dict/words"

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

A = [
	[0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
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

def boggleable(word, letters):
	# Must be at least 3 letters long
	if len(word) < 3:
		return False
	# Cannot be a proper noun
	if word[0].isupper():
		return False
	# Must be spellable on the board
	for letter in word.upper():
		if letter in letters:
			letters.remove(letter)
		else:
			return False
	return True

def boggleGraph():
	m = 4
	n = 4
	graph = []
	for k in range(m * n):
		line = m * n * [0]
		# Horizontal gridlines
		if ((k + 1) % n) != 0:
			line[k+1] = 1
		if (k % n) != 0:
			line[k-1] = 1
		# Vertical gridlines
		if (k + n) < (m * n):
			line[k+n] = 1
		if (k - n) >= 0:
			line[k-n] = 1
		# \ diagonals
		if (k % n) != (n - 1) and k < ((m-1) * n):
			line[k+n+1] = 1
		if (k % n) != 0 and k >= n:
			line[k-n-1] = 1
		# / diagonals
		if (k % n) != (n - 1) and k >= n:
			line[k-n+1] = 1
		if (k % n) != 0 and k < (m-1) * n:
			line[k+n-1] = 1
		graph.append(line)
		print(line)
	return graph

def main():
	# Square Boggle Board
	board = makeBoard()
	# List of Letters
	letters = [letter for row in board for letter in row]
	# Make grid graph with diagonals
	graph = boggleGraph()
	# Get possible words
	words = []
	with open(wordsFilePath, "r") as wordsFile:
		words = [w.upper() for w in wordsFile.read().splitlines() if boggleable(w,list(letters))]

if __name__ == "__main__":
	main()
