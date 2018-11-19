def RPS():
	p1choice = input("Player 1 Enter your choice (R, P or S): ")
	p2choice = input("Player 2 Enter your choice (R,P, or S): ")
	if p1choice == "R" or p1choice == "Rock":
		if p2choice == "S" or p2choice == "Scissors":
				print "Player 1 Wins! Congratulations Player 1!"
		elif p2choice == "P" or p2choice == "Paper":
				print "Player 2 Wins! Congratulations Player 2!"
		elif p











