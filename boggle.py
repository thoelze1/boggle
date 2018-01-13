# Current obstacle is to find out how to store partial solutions. 
# https://math.stackexchange.com/questions/92555/counting-the-number-of-paths-on-a-graph

import random
import sys

# Language parameters
wordsFilePath = "/usr/share/dict/words"

# Boggle parameters
m = 4
n = 4
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
graph = []
coverBoard = [
	['G','A','U','T'],
	['P','R','M','R'],
	['D','O','L','A'],
	['E','S','I','C']
]

def randomBoard():
	diceOrder = list(range(m*n))
	random.shuffle(diceOrder)
	return [[random.choice(boggleDice[diceOrder[n*i+j]%len(boggleDice)]) for j in range(n)] for i in range(m)]

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

def makeBoggleGraph():
	g = []
	for k in range(m * n):
		row = m * n * [0]
		# Horizontal gridlines
		if ((k + 1) % n) != 0:
			row[k+1] = 1
		if (k % n) != 0:
			row[k-1] = 1
		# Vertical gridlines
		if (k + n) < (m * n):
			row[k+n] = 1
		if (k - n) >= 0:
			row[k-n] = 1
		# \ diagonals
		if (k % n) != (n - 1) and k < ((m-1) * n):
			row[k+n+1] = 1
		if (k % n) != 0 and k >= n:
			row[k-n-1] = 1
		# / diagonals
		if (k % n) != (n - 1) and k >= n:
			row[k-n+1] = 1
		if (k % n) != 0 and k < (m-1) * n:
			row[k+n-1] = 1
		g.append(row)
	return g

def getWordSpace(letters):
	words = []
	with open(wordsFilePath, "r") as wordsFile:
		words = [w.upper() for w in wordsFile.read().splitlines() if boggleable(w,list(letters))]
	return words

def dfs(letters, wordSpace, path):
	# Start a list of new words
	newWords = []
	# Construct the word represented by the current path
	currWord = ''.join([letters[i] for i in path])
	# Determine if the path is promising by checking if any
	# possible words start with the current word
	promising = False
	for word in wordSpace:
		if word.startswith(currWord):
			promising = True
			break
	if not promising:
		return []
	else:
		if currWord in wordSpace:
			newWords.append(currWord)
	# Continue dfs with each adjacent letter
	for i in range(m*n):
		if graph[path[-1]][i] == 1 and i not in path:
			newPath = list(path)
			newPath.append(i)
			newWords.extend(dfs(letters, wordSpace, newPath))
	return newWords

def bruteForce(board):
	# List of Letters
	letters = [letter for row in board for letter in row]
	# Get all words that can be spelled with the letters on the board in any order
	wordSpace = getWordSpace(letters)
	# Find present words with DFS search. Start at each vertex in turn and add new words.
	words = []
	for v in range(m*n):
		words.extend(dfs(letters, wordSpace, [v]))
	# Remove duplicates and sort by descending length
	words = list(set(words))
	words.sort(key=len, reverse=True)
	return words

def main():
	# If user specified board dimensions, set them
	if len(sys.argv) == 3:
		global m
		global n
		m = int(sys.argv[1])
		n = int(sys.argv[2])
	# Make adjacency graph representing a grid graph with diagonals
	global graph
	graph = makeBoggleGraph()
	# Make a random boggle board
	board = randomBoard()
	# Find all words present in the boggle board
	words = bruteForce(board)
	# Print the results!
	printBoard(board)
	print()
	for word in words:
		print(word)

if __name__ == "__main__":
	main()
