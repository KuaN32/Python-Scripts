#Snake Game in Python

#Import pygame, the python module designed for writing games
import pygame
#Import sys module, module holds exit function and other essential functions
import sys
#Import random module, needed to place food in random positions on the screen
import random
#Needed to "sleep" the game for game over screens before exiting
import time

check_errors = pygame.init()
#pygame.init() returns a tuple with 2 numbers, first number is number of initializations
#second number is number of errors. We want to check for errors and shut down if there are any

if(check_errors[1]) > 0:
	print ("(!) Had {0} initializing errors! exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) pygame successfully initalized!")

#Create a play surface
screen_width=1080
screen_height=720
playSurface = pygame.display.set_mode((screen_width,screen_height)) 
#Set the height of the window. Set_mode takes in 1 tuple as an argument so 
#it is necessary to place the tuple inside the parameter brackets

#Create Window Header
header = pygame.display.set_caption('snake game')

#Test
#time.sleep(10)

#Color creation using pygame
red = pygame.Color(255,0,0) #Game Over Text
green = pygame.Color(0,255,0) #Snake
black = pygame.Color(0,0,0) #Score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42)	#Food

#Frames per Second (FPS) controller
fpsController = pygame.time.Clock()

#important variables
snakePos = [420,250] 
#intial position of snake, in the lower left quadrant of the screen
#Using a list [] as a coordinate system here, in the form of [x,y]; is is horizontal, y is vertical

snakeBody = [[420,250],[410,250],[400,250],[390,250],[380,250]] 
#Snake Body is represented as a list of coordinate-system lists, with the head being the same as snakePos

#Initial Position of Food, needs to be randomized to be on the screen and NOT where the snake is
foodPos = [random.randrange(1,108)*10,random.randrange(1,72)*10]

#Boolean to see if food has spawned or not, initialized to True
foodSpawned = True

#Direction of snake, initialize to RIGHT
direction = 'RIGHT'
changeto = direction

#Game Over function
def gameOver():
	#Create Font. Using funtion pygame.font.SysFont(name,size,bold=False,italic=False)
	myFont = pygame.font.SysFont('monaco',100,True)
	#Render font on surface using function pygame.font.Font.render(text,antialias,color,background=None)
	GOsurface = myFont.render('Game Over!', True, red)
	#Rectangle Component of the Surface
	GORect = GOsurface.get_rect()
	#Place the actual message in the 'Rectangle'. It is a tuple with xy coordinates
	GORect.midtop = (540,20) 			#Middle of the horizontal, top of the screen
	#blit function placed on the play Surface, 2 argunments: Surface and Rectangle
	playSurface.blit(GOsurface,GORect)
	pygame.display.flip()
	time.sleep(4) #Have the screen hold until exit
	pygame.quit()	#Exit pygame
	sys.exit()	#Exit python console

#Main Logic of the Game
#Infinite Loop to loop the game until game over condition is reached
while True:
	for event in pygame.event.get():	#Get the events in a queue using a for loop
		if event.type == pygame.QUIT:	#Quit Event. pygame has an inbuilt event called QUIT that specifies quitting the game
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:	#Event when the user presses down on a key
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:	#Right arrow key or 'D' button to indicate right movement
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:	#Left arrow key or 'A' button to indicate right movement
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == pygame.K_w:		#Right arrow key or 'W' button to indicate right movement
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:	#Right arrow key or 'S' button to indicate right movement
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))			#Create a new event on the queue to quit the game

	#Validation of Direction, ie can't change direction to left while moving right, to up while moving down etc
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	#Alter the snakePos variable based on the direction LEFT/RIGHT modifies x-coordinate while UP/DOWN modifies y-coordinate
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -=10
	if direction == 'DOWN':
		snakePos[1] +=10

	#Snake Body Mechanism, 
	snakeBody.insert(0,list(snakePos))  #Insert a block to represent movement of the snake
	if snakePos[0] == foodPos[0] and snakePos[1]==foodPos[1]:  	#Head of Snake is the same place as the food
		foodSpawned = False		#Food has been eaten and needs to be set to temporarily False
	else:
		snakeBody.pop()  #Remove the last block of the snake to represent movement

	if foodSpawned == False:
		foodPos = [random.randrange(1,108)*10,random.randrange(1,72)*10]	#Spawn a new piece of food

	foodSpawned = True

	#Fill the game window (playSurface) with a color using the fill function
	playSurface.fill(white)

	#For loop to draw the sanke
	for pos in snakeBody:
		pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))

	#Draw the food
	pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

	#Checking for boundaries, added 10 to each boundary to give a bit of time for the player to react when reaching the side
	if snakePos[0] >= (screen_width+10) or snakePos[0] <= -10 or snakePos[1] >= (screen_height+10) or snakePos[1] <= -10:
		gameOver()

	#Checking to see if head hits snake body using a for loop
	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:	#The 0 and 1 in this case represent the x and y coordinates
			gameOver()

	#Update the display
	pygame.display.update()
	
	#This determines the speed of the game
	#Can use this to set difficulty, higher number means higher difficulty
	fpsController.tick(30)