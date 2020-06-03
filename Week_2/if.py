answer = input("Do you want to hear a joke? ")

yes = ["yes", "y"]
no = ["no" , "n"]

if answer.lower() in yes:
	print("I'm against picketing, but I don't know how to show it.")
	# Mitch Hedburg

elif answer.lower() in no:
	print("Well fine...")

else:
	print("Huh?")