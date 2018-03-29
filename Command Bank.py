#initialisation
import random
import Dice Roll
dice1 = 0
dice2 = 0
move = 0

flag = True
hasrolled = False
rollcount = 0

command = input("What do you want me to do? ").lower()

while flag == True: 
	
	#giving the player's info
	infocheck = command.split()
	
	#Making sure that you don't end turn before rolling the dice.
	if (command == "end") & (hasrolled == False):
		print("You can't end now, you have to at least roll.")
		print()
		
	#Ending the loop
	elif command == "end":
			break
		
	#Bringing up the command list	
	elif command == "?":
		print("end - ends your turn")
		print("roll - rolls for your turn, letting you move that number of spaces.")
		print("info player - for your player info (money, properties etc.)")
		print("info property - get the info for a property you specify.")
		print("buy - attempt to buy the property your piece is currently on.")
		#print("buy house - attempt to buy a house on a property you own")
		print()
	
	#Rolling Dice
		import Dice Roll

	#Basic info command
		import Getting Info

	#Buy property
		import Buy Property

	#error statement for invalid commands
	else:
		print ("Not a valid command. (enter ? for command list)")
		print()
		
	command = input("What do you want me to do? ").lower()