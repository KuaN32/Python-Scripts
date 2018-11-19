import random
#DICTIONARY MAPPING FUNCTION TO CONVERT INT TO RPS CHOICE
def rpsget(choice):
	"0 is Rock, 1 is Paper, 2 is Scissors"
	switcher = {
		0: "R",
		1: "P",
		2: "S",
	}
	return switcher.get(choice)

#PROGRAM START
restart = True
print ("Welcome to Rock, Paper and Scissors!")

while restart == True:
	flag = False

	#VS COMPUTER
	choice = str(input( "Enter your choice (R,P or S): "))

	#Check User Input
	if choice == "R" or choice == "S" or choice == "P" or choice == "r" or choice == "s" or choice =="p":
		flag = True

	while flag == False:
		choice = str(input("Invalid Input. Enter Again: "))
		if choice == "R" or choice == "S" or choice == "P" or choice == "r" or choice == "s" or choice =="p":
			flag = True

	compchoiceint = random.randint(0,2)

	compchoice = rpsget(compchoiceint)

	if choice == "R" or choice == "r":
		if compchoice == "P":
			print ("Sorry! Computer Wins!")
		elif compchoice == "R":
			print ("Draw!")
		else:
			print ("Congratulations! You Win!")
	elif choice == "P" or choice == "p":
		if compchoice == "S":
			print ("Sorry! Computer Wins!")
		elif compchoice == "P":
			print ("Draw!")
		else:
			print ("Congratulations! You Win!")
	else:
		if compchoice == "R":
			print ("Sorry! Computer Wins!")
		elif compchoice == "S":
			print ("Draw!")
		else:
			print ("Congratulations! You Win!")

	print ("Your choice was " + choice)
	print ("Computer choice was " + compchoice)

	rFlag = False
	rChoice = str(input("Play Again? (Y/N): ")) 
	while rFlag == False:
		if rChoice == "Y":
			restart = True
			rFlag = True
		elif rChoice == "N":
			restart = False
			rFlag = True
		else:
			rChoice = str(input("Sorry, we didn't get that. Enter 'Y' or 'N': "))