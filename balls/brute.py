import sys
from copy import deepcopy
import random
from math import ceil

from balls.tools import printBoard, _p

DEBUG_PRINT = True
BRUTE_DEPTH = 50
TRIES = 0
def isSolved(board):
	global TRIES
	TRIES += 1
	for pipe in board:
		pc = None
		for c in pipe:
			if pc == None:
				pc = c
			elif pc != c or len(pipe) != 4:
				return False
	return True

# Att lägga till:
# - inte påbörja ny pipe om färg kan flyttas ner till annan som ännu inte är fylld
# - flytta den mindre högen till den större, för att spara steg
def findValidMoves(board):
	def _groupSize(pipe):
		c = None
		n = 0

		for p in reversed(pipe):
			if c == None:
				c = p
			elif c != p:
				return n
			n += 1
		return n

	moves = []
	
	def _isPipeSingleColor(pipe):
		pc = None

		for c in pipe:
			if pc == None:
				pc = c
			elif pc != c:
				return False
		
		return True
	
	pn = 0
	for pipe in board:
		if len(pipe) == 0:
			pn += 1
			continue

		topColor = pipe[-1]
		size = _groupSize(pipe)

		pipeMoves = []
		usedPipes = [] # If two destination pipes are identical they both shouldn't be added as moves

		pn2 = 0
		for pipe2 in board:
			# if they're the same pipe, or
			#	 the pipes are identical, unless they are made of a single color, or
			#	 there's an identical pipe already added as a destination pipe, or
			#	 when the top leaves the pipe it will create a pipe identical to the destination pipe before the move
			if pn == pn2 or (pipe == pipe2 and not _isPipeSingleColor(pipe)) or pipe2 in usedPipes or pipe[:-size] == pipe2:# (len(pipe2) == 0 and len(pipe) < 4):
				pn2 += 1
				continue

			# if the pipe is empty, or
			#	 the top can fit ontop of destination pipe, and has the correct top color
			if len(pipe2) == 0 or ((len(pipe2) <= 4 - size) and pipe2[-1] == topColor):
				move = (pn, pn2, size)
				pipeMoves.append(move)
				usedPipes.append(pipe2)

			pn2 += 1
		
		# if a color can be moved to a non empty pipe, moving to an empty should not be an alternative	
		if len(pipeMoves) > 1 and [] in [board[x[1]] for x in pipeMoves]:
			for pm in pipeMoves:
				if len(board[pm[1]]) == 0:
					pipeMoves.remove(pm)
					break

		moves.extend(pipeMoves)

		pn += 1
	
	def _priority(x):
		return len(board[x[1]]) == 0

	moves.sort(key=_priority)

	return moves

def move(board, move):
	opipe, dpipe, size = move
	
	if len(board[opipe]) == 0:
		raise Exception("trying to move from empty pipe")

	if len(board[dpipe]) == 4:
		raise Exception("trying to move to full pipe")

	if len(board[dpipe]) > 0 and board[opipe][-1] != board[dpipe][-1]:
		raise Exception("trying to move color ontop of another color")

	for _ in range(0, size):
		color = board[opipe].pop()
		board[dpipe].append(color)

def _brute(board, history = [], newMove = None, d = 0, **kwargs):
	if newMove:
		_p(d, "Move: ", newMove)

		move(board, newMove)
		history.append(newMove)

		printBoard(board, lambda *s,**kwargs: _p(d, *s, **kwargs))

		if isSolved(board):
			return history
		elif d >= kwargs.get("max_depth", BRUTE_DEPTH):
			print("Reached max depth", d, kwargs.get("max_depth"))
			return False
	
	moves = findValidMoves(board)

	_p(d, "Moves:", moves)

	if moves == []:
		_p(d, "---- ^")
		return False

	for m in moves:
		solved = _brute(deepcopy(board), deepcopy(history), m, d+1, **kwargs)
		if solved:
			return solved

def solve(board, **kwargs):
	moves = _brute(board, **kwargs)
	print("tries:", TRIES)
	return moves

