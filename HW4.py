import pygame
import random
import math
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
pygame.display.set_caption("Pizza!")
pygame.display.update() #only updates portion specified


def angles_velocity(velocity, angle):
	if angle is None:
		return 0,0
	else:
		return velocity*math.cos(math.radians(angle)), velocity*math.sin(math.radians(angle))

def sign(num):
    if num >= 0:
        return 1
    else:
        return -1

class BO_Object(pygame.sprite.Sprite):

	def __init__(self, img_file = None, x_pos, y_pos, game = None):
		pygame.sprite.Sprite.__init__(self, img_file, x_pos, y_pos)
		self.game = game

		self.x_pos = x_pos
		self.y_pos = y_pos

		self.set_initial_position()

	def set_initial_position(self):
		self.set_position(self.x_pos, self.y_pos)
		self.velocity = 0.0
		self.angle = None

	def move_GO(self):
		x_delta, y_delta = angles_velocity(self.velocity, self.angle)
		self.set_position(self.x + int(x_delta), self.y + int(y_delta))

	def update(self, pressed_keys):
		self.move()

class Colleen(BO_Object):

	def deflect_pizza(self, pizza, side_hit):

		if side_hit == 'RIGHT' or side_hit == 'LEFT':
			pizza.angle = (180-ball.angle) % 360
		elif side_hit = 'BOTTOM' or side_hit = 'TOP':
			pizza.angle = (- ball.angle) % 360 

		self.shunt(ball)

	def shunt(self, pizza):
		while pizza.colliding_with(self):
			pizza.move()
			if (ball.x < 0) or (ball.y < 0):
				foobar

class EndLine(Colleeen):

	def deflect_ball(self, pizza, side_hit):
		if side_hit == 'LEFT':
			self.game.reset()
		elif side_hit == 'RIGHT':
			self.game.reset()
		else:
			raise Exception(side_hit)


class Pizza(Gameobject):

	default_velocity = 6.0

	def update(self, pressed_keys):
		self.move()
		if self.in_play:
			for game_object in self.game.game_objects:
				side_hit = self.colliding_with(game_object)
				if side_hit:
					game_object.deflect_ball(self, side_hit)

	def set_initial_position(self):
		self.set_position(self.x_pos, self.y_pos)
		self.velocity = self.default_velocity
		self.angle = self.generate_random_starting_angle()
		self.in_play = True

	def generate_random_starting_angle(self):
		angle = random.randint(10, 75)
		debug_print('Starting ball angle: ' + str(angle) + 'degrees')
		return angle






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