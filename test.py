import random
import sys

import balls

balls.tools.DEBUG_PRINT = True

def _randomBoardString():
	seed = random.randrange(sys.maxsize)
	random.seed(seed)

	print("Generating random board, seed:", seed)

	return balls.generate.generateRandomBoardString()


def main():
	boardString = None

	# -----------------------------------------------------

	boardString = "8a279320979413b850a1b724459536b0350816a6b876412a" # took slightly longer
	#boardString = "0a3260071ab42161272548bbb9176053958634a8893a9745" # no solution yet
	#boardString = "00123145627642289071a4aab889bb6761b3a98437905553"
	#boardString = "21005413672682241709aa4a988b76bb3b16489a09733555"
	#boardString = "0000111122223333444455556666777788889999aaaabbxxbb"
	#boardString = "0000111122223333444455556666777788889999baaaxbbba"

	# -----------------------------------------------------

	if boardString == None:
		boardString = _randomBoardString()

	print("Board string:", boardString)

	mainBoard = balls.tools.boardFromString(boardString)

	moves = balls.solve(mainBoard)

	if not moves:
		print("Not solvable. Maybe a deeper brute depth can solve it")
		return
	
	print("Solvable in " + str(len(moves)) + " moves")

	for i, m in enumerate(moves):
		if i % 5 == 0 and i != 0:
			print()
		# This might just be the weirdest line I've ever written
		print(str(i + 1).rjust(len(str(len(moves)))) + ":", str(m[0]).rjust(2), "->", str(m[1]).rjust(2), m[2])

if __name__ == "__main__":
	main()
