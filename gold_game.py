# Dig for gold
# Based on Whack-a-mole game using pygame by Kimberly Todd

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000; #Seed a timer to move sprite

bgcolor = (0,42,196) #Color taken from background of sprite

class Gold(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("gold.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("shovel.gif").convert()
        self.rect = self.image.get_rect()

    # Di shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()


#main
init()

screen = display.set_mode((640, 480))
display.set_caption('Dig-some-Gold')

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)

f = font.Font(None, 25)

# create the mole and shovel using the constructors
gold = Gold()
shovel = Shovel()
# creates a group of sprites so all can be updated at once
sprites = RenderPlain(gold, shovel)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if shovel.hit(gold):
            mixer.Sound("cha-ching.wav").play()
            gold.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        gold.move()

    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("Jackpot = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    display.update()