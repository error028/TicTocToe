#tic toc toe 

import os

#board
board = [ "-", "-", "-",
	  "-", "-", "-",
	  "-", "-", "-" ]
				
#[0, 1, 2]
#[3, 4, 5]
#[6, 7, 8]

#function find winner
def find_winner():
	#winnig conditions for X
	winX=[  
                board[0] == board[4] == board[8] == 'X',
		board[6] == board[4] == board[2] == 'X',
		board[0] == board[1] == board[2] == 'X',
		board[3] == board[4] == board[5] == 'X',
		board[6] == board[7] == board[8] == 'X',
		board[0] == board[3] == board[6] == 'X',
		board[1] == board[4] == board[7] == 'X',
		board[2] == board[5] == board[8] == 'X'   ]
	#winnig conditions for O
	winO=[   
                board[0] == board[4] == board[8] == 'O',
		board[6] == board[4] == board[2] == 'O',
		board[0] == board[1] == board[2] == 'O',
		board[3] == board[4] == board[5] == 'O',
		board[6] == board[7] == board[8] == 'O',
		board[0] == board[3] == board[6] == 'O',
		board[1] == board[4] == board[7] == 'O',
		board[2] == board[5] == board[8] == 'O'   ]

	if any(winX):
		print("X is winner")
		exit()
	elif any(winO):
		print("O is winner")
		exit()
	else:
		if "-" in board:
			print()
		else:
			print("its a tie")
			exit()

				
#function to display board
def display_board():
	print(" "+board[0] + "  |  " + board[1] + "  |  " + board[2])
	print("____|_____|____")
	print(" "+board[3] + "  |  " + board[4] + "  |  " + board[5])
	print("____|_____|____")
	print(" "+board[6] + "  |  " + board[7] + "  |  " + board[8])
	print()
	
	
#take user 1 input
def take_user1_input():	
	position = int(input("Player-X enter your position: "))-1
	clear()
	if board[position] != "-":
		print("postion taken")
		display_board()
		take_user1_input()
	else:
		board[position] = "X"
		print()
		display_board()

#takes user 2 input
def take_user2_input():
	position = int(input("Player-O enter your position: "))-1
	clear()
	if board[position] != "-":
		print("postion taken")
		display_board()
		take_user2_input()
	else:
		board[position] = "O"
		print()
		display_board()
	

def clear():
	os.system("clear")
	
	
#start game
def play():
	display_board()
	take_user1_input()
	find_winner()
	take_user2_input()
	find_winner()
	clear()
	

while True:
	play()


