import pygame
pygame.init()


# creating colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# assigning position variables
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

# create a game display surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

# lets add a title, aka "caption"
pygame.display.set_caption("Let's find Colleen!")
pygame.display.update() #only updates portion specified


gameExit = False
while not gameExit:
	gameDisplay.fill(black)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
	
	x_pos +=x_delta
	y_pos +=y_delta
	gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()		
	clock.tick(30)



pygame.quit()
quit() # exits python