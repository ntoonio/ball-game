import random
import sys

import balls

balls.tools.DEBUG_PRINT = False

BOARD_DATA_KEYS = ["successfull", "exception", "tries", "steps", "individual_steps"]

def generateDataOutput(boardString, boardData):
	out = ""

	out += "- - - - - - - \n"
	out += "Board: " + boardString + "\n"

	for k in BOARD_DATA_KEYS:
		out += k + ": " + str(boardData[k] if k in boardData else 0) + "\n"

	out += "- - - - - - - \n"
	
	return out

def main():
	
	f = open("result_benchmark.txt", "w")

	boardStrings = [
		"8a279320979413b850a1b724459536b0350816a6b876412a",
		"00123145627642289071a4aab889bb6761b3a98437905553",
		"996792ba7856741b050615a364b2a33888442013b02a7159",
		"077625b04688ba6689441a0b43795a93232052185971a3b1",
		"2863385364b9210779a558501369ba760a942b480a1217b4",
		"774a9103170bb933252558986640219368a4670a1ba2485b",
		"26a3147a1444328231098375b2a196b0b08b07597a659865",
		"2b2b431939aa0928114698715a6b437475a020b556788306",
		"3230603a8877b946055a0474892a7821231bb466a51b9195",
		"765a625ab72b281238417683ab64a00139859410b9093745"
	]

	for bs in boardStrings:
		board = balls.tools.boardFromString(bs)

		boardData = {}

		moves = []

		try:
			moves = balls.brute.solve(board, boardData)

			boardData["successfull"] = 1
		except Exception  as e:
			boardData["exception"] = "1 " + str(e)

		boardData["steps"] = len(moves)

		boardData["individual_steps"] = 0

		for m in moves:
			boardData["individual_steps"] += m[2]

		runStatistics = generateDataOutput(bs, boardData)

		print(runStatistics)
		f.write(runStatistics)

	f.close()

if __name__ == "__main__":
	main()
