#Basic info command	
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
#	if command.split()[1] == "property":
#		propsearch = input("What property are you wanting to know about? ")
#		for i in range(0, len(boardpos)):
#			if propsearch == boardpos[i][name].lower():
#				print(boardpos[i][name])
#				print("- " + boardpos[i][colour].title() + " -")
#				print("Price: $" + boardpos[i][price])
#				print("Rent with no buildings: $" + boardpos[i][rent])
#				print("    \"     one house: $" + boardpos[i][onehouse])
#				print("    \"     two houses: $" + boardpos[i][twohouse])
#				print("    \"     three houses: $" + boardpos[i][threehouse])
#				print("    \"     four houses: $" + boardpos[i][fourhouse])
#				print("    \"     hotel: $" + boardpos[i][hotel])
#				print("")
#				print("Price of single building: $" + boardpos[i][buildprice])
#				print("")
	else:
		print("Invalid input, try 'info player' or 'info properties'")
		print()