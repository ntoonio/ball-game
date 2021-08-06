import random

# TODO: pass rand variable
def generateRandomBoardString():
	colors = "".join([x*4 for x in "0123456789ab"])
	
	s = ""

	while len(colors)>0:
		i = random.randint(0, len(colors) - 1)
		s += colors[i]
		colors = colors[:i] + colors[i + 1:]
	
	return s
