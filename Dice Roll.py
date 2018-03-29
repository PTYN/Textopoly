def Diceroll():
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