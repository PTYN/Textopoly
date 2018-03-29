import random
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
	
	#Rolling the dice, allowing it to be ready for visual dice.
	elif (command == "roll") & (hasrolled == False):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		move = dice1+dice2
		#print(dice1)
		#print(dice2)
		print("You have moved",move,"spaces.")
		print()
		hasrolled = True
		if dice1 == dice2: # <-- allowing for rolling again
			print("DOUBLE, Roll again")
			print()
			hasrolled = False
			
	#Telling that they can't roll again.
	elif (command == "roll") & (hasrolled == True):
		print("You've already rolled, you can't roll again")
		print()
		
	elif infocheck[0] == "info":
		if len(infocheck) == 1:
			print("Invalid input, try 'info player' or 'info properties'")
			print()
		elif infocheck [1] == "player":
			print("Character: ")
			print("Money: ")
			print("Properties: ")
			print()

		#gives information on specified property
#		if command.split()[1] == "property":
#			propsearch = input("What property are you wanting to know about? ")
#			for i in range(0, len(boardpos)):
#				if propsearch == boardpos[i][name].lower():
#					print(boardpos[i][name])
#					print("- " + boardpos[i][colour].title() + " -")
#					print("Price: $" + boardpos[i][price])
#					print("Rent with no buildings: $" + boardpos[i][rent])
#					print("    \"     one house: $" + boardpos[i][onehouse])
#					print("    \"     two houses: $" + boardpos[i][twohouse])
#					print("    \"     three houses: $" + boardpos[i][threehouse])
#					print("    \"     four houses: $" + boardpos[i][fourhouse])
#					print("    \"     hotel: $" + boardpos[i][hotel])
#					print("")
#					print("Price of single building: $" + boardpos[i][buildprice])
#					print("")
		else:
			print("Invalid input, try 'info player' or 'info properties'")
			print()

	#buying the property that they are on
	elif command == "buy":
		#if boardpos[playerpos][owner]!= "":
			#print("This property is already owned")
			#print()
		#elif playermoney >= boardpos[playerpos][price]:
			#playermoney = playermoney-boardpos[playerpos][price]
			#boardpos[playerpos][owner] = playerchar
			#print("You now own",boardpos[playerpos][name])
			#print()
		#else:
			print("You do not have enough money for that.")
			print()
	
	#error statement for invalid commands
	else:
		print ("Not a valid command. (enter ? for command list)")
		print()
	
	command = input("What do you want me to do? ").lower()
