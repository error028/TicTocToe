#tic toc toe 

import os
import platform

#board
board = [ "-", "-", "-",
	  		   "-", "-", "-",
	  		   "-", "-", "-" ]
				
#[0, 1, 2]
#[3, 4, 5] --> board positions
#[6, 7, 8]

#function find winner
def find_winner():
	#list of winnig conditions for X
	winX=[  
        board[0] == board[4] == board[8] == 'X',
		board[6] == board[4] == board[2] == 'X',
		board[0] == board[1] == board[2] == 'X',
		board[3] == board[4] == board[5] == 'X',
		board[6] == board[7] == board[8] == 'X',
		board[0] == board[3] == board[6] == 'X',
		board[1] == board[4] == board[7] == 'X',
		board[2] == board[5] == board[8] == 'X'   ]
	#list of winnig conditions for O
	winO=[   
        board[0] == board[4] == board[8] == 'O',
		board[6] == board[4] == board[2] == 'O',
		board[0] == board[1] == board[2] == 'O',
		board[3] == board[4] == board[5] == 'O',
		board[6] == board[7] == board[8] == 'O',
		board[0] == board[3] == board[6] == 'O',
		board[1] == board[4] == board[7] == 'O',
		board[2] == board[5] == board[8] == 'O'   ]
	if any(winX):#checks if any winning condition for X
		print("\u001b[32mX is winner\u001b[37m")
		exit()
	elif any(winO):#checks if any winning condition for O
		print("\u001b[32mO is winner\u001b[37m")
		exit()
	else:
		if "-" in board:
			print()
		else:
			print("\u001b[33mIts a Tie!")
			exit()

				
#function to display board
def display_board():
	print("    "+board[0] + "\t|\t" + board[1] + "\t|\t " + board[2])
	print("________|_______________|____________")
	print("    "+board[3] + "\t|\t" + board[4] + " \t|\t " + board[5])
	print("________|_______________|____________")
	print("    "+board[6] + " \t|\t" + board[7] + "\t|\t " + board[8])
	print()
	


#This function takes user input along with player as parameter
def take_user_input(player):	
	position = input(f"Player-{player} enter your position: ")
	if position.isdigit() and (int(position) in (1,2,3,4,5,6,7,8,9)):
		position=int(position)-1
		clear()
		if board[position] != "-":
			display_board()
			print("\u001b[31mPostion Taken!\u001b[37m")
			#The code \u001b[31m is ascii color code
			#you can google it for more info
			take_user_input(player)
		else:
			board[position] = player
			print()
			display_board()
	else:
		clear()
		display_board()
		print("\u001b[31mInvalid Entry!\u001b[37m")
		take_user_input(player)

#this function is for clearing screen both on windows and linux
def clear():
	if platform.system()=="Windows":
		os.system("cls")
	else:
		os.system("clear")
	
	
#This function is used to play game
def play():
		display_board()
		take_user_input("X")
		find_winner()
		take_user_input("O")
		find_winner()
		clear()
	
#this loop plays game untill a winner is found	
while True:
	play()

#Hope you guys understand my code 
#Thank you guys 
# Instagram:error_is_energy



