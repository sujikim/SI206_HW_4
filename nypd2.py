from pygame import *
from pygame.sprite import *
from random import *



# creating colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (242, 177, 225)
DELAY = 1000 #Seed a timer to move sprite

# assigning background color
bgcolor = pink  

# creating sprites classes

class Pizza(Sprite):
    """ This class represents each single slice of pizza that will appear
    It derives from the "Sprite" class in Pygame"""
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("pizza.bmp").convert_alpha()
        self.rect = self.image.get_rect()


    #
    def move(self):
        randX = randint(0, 820)
        randY = randint(60, 620)
        self.rect.center = (randX,randY)

class Nypd(Sprite):
    """ This class represents each whole pizza that will appear
    It derives from the "Sprite" class in Pygame"""
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("nypd.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 820)
        randY = randint(60, 620)
        self.rect.center = (randX,randY)

class BlackNypd(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("blacknypd.bmp").convert_alpha()
        self.rect = self.image.get_rect()
    
    def move(self):
        randX = randint(0, 820)
        randY = randint(60, 620)
        self.rect.center = (randX,randY)

class Colleen(Sprite):
    """ This class represents the icon of Colleen's head that the player 
    controls with the mouse """
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("colleeen.bmp").convert()
        self.rect = self.image.get_rect()

    # Di shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()



# main
init()

screen = display.set_mode((840, 680))
display.set_caption('Colleen Pizza Depot')

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)

f = font.Font(None, 50)

# create the mole and shovel using the constructors
pizza = Pizza()
pizza1 = Pizza()
colleen = Colleen()
nypd = Nypd()
blacknypd = BlackNypd()


# creates a group of sprites so all can be updated at once
sprites = Group(pizza, pizza1, colleen)
nypd_sprites = Group(nypd, blacknypd)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if colleen.hit(pizza):
            mixer.Sound("pop.wav").play()
            pizza.move()
            hits += 1
        if colleen.hit(pizza1):
            mixer.Sound("pop.wav").play()
            pizza1.move()
            hits += 1
        
        if colleen.hit(nypd):
            mixer.Sound("cha-ching.wav").play()
            nypd.move()
            hits += 5
            # reset timer
        if colleen.hit(blacknypd):
            mixer.Sound("cha-ching.wav").play()
            blacknypd.move()
            hits -= 5
        time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        pizza.move()
        pizza1.move()
    
    elif e.type == USEREVENT + 10:
        nypd.move()
        blacknypd.move()

    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("Pizza Score = " + str(hits), False, (255, 255, 255))
    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    nypd_sprites.update()
    nypd_sprites.draw(s)
    display.update()
