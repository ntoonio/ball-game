DEBUG_PRINT = True

def _p(d, *s, **kwargs):
	if not DEBUG_PRINT:
		return
	print("  - " * d, *s, **kwargs)

def _dec(i):
	return int(i, 16)

def printBoard(board, pp=print):
	for r in range(0, 10):
		if r == 4 or r == 9:
			pp(" ".join(["‾" * 5 for x in range(0, 7)]))
		else:
			# 3 7 11 15 19 23 27 31
			# 2 6 10 14 18 22 26 30
			# 1 5  9 13 17 21 25 29
			# 0 4  8 12 16 20 24 28

			# 0-3 1-3 2-3 3-3 4-3 5-3 6-3
			# 0-2 1-2 2-2 3-2 4-2 5-2 6-2
			# 0-1 1-1 2-1 3-1 4-1 5-1 6-1
			# 0-0 1-0 2-0 3-0 4-0 5-0 6-0

			ss = []
			for p in range(0, 7):
				pipe = p + (7 if r > 4 else 0)
				depth = 3 - r + (5 if r > 4 else 0)

				color = hex(board[pipe][depth])[2:] if len(board[pipe]) > depth else " "

				ss.append("| " + color + " |")

			pp(" ".join(ss))

def boardFromString(s):
	board = []

	for i in range(0, 14*4):
		if i % 4 == 0:
			board.append([])

		if len(s) > i:
			c = s[i]
			if c != "x":
				board[int(i / 4)].append(_dec(c))
			i += 1

	return board

