def validChoice(choice, range=0):
	isValidCmd = False
	while (not isValidCmd):

		if choice.isnumeric():
			if range == 0:
				isValidCmd = True
			elif int(choice) > 0 and int(choice) < range:
				isValidCmd = True
			else:
				choice = input("Invalid choice. Try again, in the range: ")
		else:
			choice = input("Invalid choice. Try a number: ")

	return int(choice)