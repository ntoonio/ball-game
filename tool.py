from balls.tools import printBoard, boardFromString
import sys

def main():
	boardString = sys.argv[1]

	board = boardFromString(boardString)

	printBoard(board)

if __name__ == "__main__":
	main()
