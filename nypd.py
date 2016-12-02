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
# class Start(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         self.image = image.load("start.bmp").convert_alpha()
#         self.rect = self.image.get_rect()


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

# class BlackNypd(Nypd):


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


# def layers(self):
#     layers = set()
#     for layer in self.spritelayers.values():
#         layers.add(layer)
#     return list(layers)
# def get_top_layer(self):
#     return self.__spritelayers[self._spritelist[-1]]
# def move_to_front(self, sprite):
#     self.change_layer(sprite, self.get_top_layer())



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
nypd = Nypd()
blacknypd = BlackNypd()
# start = Start()


colleen = Colleen()

# creates a group of sprites so all can be updated at once

sprites = RenderPlain(pizza, pizza1, nypd, blacknypd, colleen)
# sprites = RenderPlain(pizza, pizza1, colleen)
# nypd_sprites = RenderPlain(nypd, blacknypd)


DELAY = 1000;
LONG_DELAY = 10000;
hits = 0
time.set_timer(USEREVENT + 1, DELAY)
time.set_timer(USEREVENT + 1, LONG_DELAY)
# countdown = 

# loop until user quits


# screen.fill(black)
# start = f.render("START", False, (255, 255, 255))
# screen.blit(start, (310, 310))
# display.update()
once = 0
while True:

    e = event.poll()
    # if e.type != QUIT and once == 0:
    #     screen.fill(black)
    #     gamestart = f.render("CLICK ANYWHERE TO START", False, (255, 255, 255))
    #     screen.blit(gamestart, (250, 310))
    #     display.update()
    #     if e.type == MOUSEBUTTONDOWN:
    #         colleen.hit(screen)
    #         once += 1


    # elif e.type == MOUSEBUTTONDOWN:
    #     if colleen.hit(start):
    #         continue
    
    if e.type == QUIT:
        quit() 
    
    
    elif e.type == MOUSEBUTTONDOWN:
        if colleen.hit(pizza):
            mixer.Sound("pop.wav").play()
            pizza.move()
            hits += 100
        if colleen.hit(pizza1):
            mixer.Sound("pop.wav").play()
            pizza1.move()
            hits += 100
        if colleen.hit(nypd):
            mixer.Sound("cha-ching.wav").play()
            nypd.move()
            hits += 500
        # time.set_timer(USEREVENT + 1, LONG_DELAY)       
        if colleen.hit(blacknypd):
            mixer.Sound("bomb.wav").play()
            blacknypd.move()
            hits -= 500
        time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        pizza.move()
        pizza1.move()
        nypd.move()
        blacknypd.move()


    elif hits < 0:
        mixer.Sound("bomb.wav").play()
        screen.fill(black)
        gameover = f.render("GAME OVER", False, (255, 255, 255))
        final_score = f.render("FINAL SCORE: " + str(hits), False, (255, 255, 255))
        screen.blit(gameover, (310, 310))
        screen.blit(final_score, (250, 370))
        display.update()
        break 




    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("Pizza Score = " + str(hits), False, (255, 255, 255))
    screen.blit(t, (0, 0))      # draw text to screen.  Can you move it?


    # update and redraw sprites
    # move_to_front(colleen)
    sprites.update()
    sprites.draw(screen)
    display.update()
    # count += 1


