from os import system,name
import random
import sys

global board 
board = [['_','_','_'],
		 ['_','_','_'],
		 ['_','_','_']]

global pos
pos = ['11','12','13',
	   '21','22','23',
	   '31','32','33']

def show(state):
	print("Press Enter for next move\n")
	for i in range(0,len(state)):
		print(state[i])


def xpos(rxpos,cxpos):
	if (board[rxpos-1][cxpos-1] == '_'):
		board[rxpos-1][cxpos-1] = "X"
		return True
	else:
		return False


def opos(ropos,copos):
	if (board[ropos-1][copos-1] == '_'):
		board[ropos-1][copos-1] = "O"
		return True
	else:
		return False

def clrsrc():
	if name == 'nt':
		scr = system('cls')
	else:
		scr = system('clear')

def get():
	get = input()
	return get

def status(txt):
	print(f"\n{txt}")

def run():
	clrsrc()
	print("Press X or O to continue")
	while True:
		game = input()
		if ((game == "x") or (game == "X")):
			print("Press Enter to Start the Game")
			xplay()
		elif ((game == "0") or (game == "O") or (game == "o")):
			print("Press Enter to Start the Game")
			oplay()
		else:
			clrsrc()
			print("Press X or O to continue")
	
def xplay():
	while True:
		if (get() == ""):
			clrsrc()
			show(board)
			determine()
			lst = getpos()			
			rxpos = lst[0]
			cxpos = lst[1]
			if xpos(int(rxpos),int(cxpos)):
				clrsrc()
				show(board)
				determine()
				status("Computer's Turn")
				randomplay("O")
			else:
				print("Already Occupied")
				xplay()

		elif (get() == "exit"):
			break
		else:
			break

	
def oplay():
	while True:
		if (get() == ""):
			clrsrc()
			show(board)
			determine()
			lst = getpos()			
			ropos = lst[0]
			copos = lst[1]
			if opos(int(ropos),int(copos)):
				clrsrc()
				show(board)
				determine()
				status("Computer's Turn")
				randomplay("X")
			else:
				print("Already Occupied")
				oplay()

		elif (get() == "exit"):
			break
		else:
			break

def randomplay(play):
	r = random.randint(1,3)
	c = random.randint(1,3)
	if play == "X":
		if xpos(r,c):
			oplay()
			determine()
		else:
			randomplay("X")
	elif play == "O":
		if opos(r,c):
			xplay()
			determine()
		else:
			randomplay("O")
	else:
		print("Computer is Sleeping")



def getpos():
	getposv = str(input("\nEnter Position: "))
	if getposv in pos:
		lst = []
		for i in getposv:
			lst.append(i)
		return lst
	else:
		clrsrc()
		show(board)
		getpos()

def check(result):
	if ((result[0] == ['X','X','X']) or (result[1] == ['X','X','X']) or (result[2] == ['X','X','X'])):
		return "X"
	elif ((result[0] == ['O','O','O']) or (result[1] == ['O','O','O']) or (result[2] == ['O','O','O'])):
		return "O"
	elif ((result[0][0] == 'X') and (result[1][0] == 'X') and (result[2][0] == 'X')):
		return "X"
	elif ((result[0][1] == 'X') and (result[1][1] == 'X') and (result[2][1] == 'X')):
		return "X"
	elif ((result[0][2] == 'X') and (result[1][2] == 'X') and (result[2][2] == 'X')):
		return "X"
	elif ((result[0][0] == 'O') and (result[1][0] == 'O') and (result[2][0] == 'O')):
		return "O"
	elif ((result[0][1] == 'O') and (result[1][1] == 'O') and (result[2][1] == 'O')):
		return "O"
	elif ((result[0][2] == 'O') and (result[1][2] == 'O') and (result[2][2] == 'O')):
		return "O"
	elif ((result[0][0] == 'X') and (result[1][1] == 'X') and (result[2][2] == 'X')):
		return "X"
	elif ((result[0][0] == 'O') and (result[1][1] == 'O') and (result[2][2] == 'O')):
		return "O"
	elif ((result[0][2] == 'X') and (result[1][1] == 'X') and (result[2][0] == 'X')):
		return "X"
	elif ((result[0][2] == 'O') and (result[1][1] == 'O') and (result[2][0] == 'O')):
		return "O"
	elif ('_' not in result[0]) and ('_' not in result[1]) and ('_' not in result[2]):
		return "Die"


def determine():
	if (check(board) == "X"):
		clrsrc()
		show(board)
		sys.exit("\nX won the Game")

	elif (check(board) == "O"):
		clrsrc()
		show(board)
		sys.exit("\nO won the Game")

	elif (check(board) == "Die"):
		clrsrc()
		show(board)
		sys.exit("\nGame Die")

if __name__ == "__main__":
	run()