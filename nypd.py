from pygame import *
from pygame.sprite import *
from random import *


# creating colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (242, 177, 225)
green = (0,  255, 127)
DELAY = 1000 #Seed a timer to move sprite

# assigning background color
bgcolor = pink  


class Pizza(Sprite):
    """ This class represents each single slice of pizza that will appear
    It derives from the "Sprite" class in Pygame"""
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("pizza.bmp").convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 820)
        randY = randint(60, 620)
        self.rect.center = (randX,randY)

class Nypd(Sprite):
    """ This class represents each red nypd icon that will appear
    It derives from the "Sprite" class in Pygame"""
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("nypd.bmp").convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 820)
        randY = randint(60, 620)
        self.rect.center = (randX,randY)


class BlackNypd(Nypd):
    """ This class represents each black nypd icon that will appear
    It derives from the "Nypd" class in Pygame"""
    def __init__(self):
        Nypd.__init__(self)
        self.image = image.load("blacknypd.bmp").convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
    
    # def move(self):
    #     randX = randint(0, 820)
    #     randY = randint(60, 620)
    #     self.rect.center = (randX,randY)


class Colleen(Sprite):
    """ This class represents the icon of Colleen's head that the player 
    controls with the mouse """
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("colleeen.bmp").convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
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

# hide the mouse cursor so we only see colleen's face
mouse.set_visible(False)

f = font.Font(None, 50)


# create the pizza slices and nypd icons using the constructors
pizza = Pizza()
pizza1 = Pizza()
pizza2 = Pizza()
nypd = Nypd()
blacknypd = BlackNypd()
blacknypd1 = BlackNypd()
# start = Start()

colleen = Colleen()


# creating sprite groups so they can be called by groups
sprites = RenderPlain(pizza, pizza1, pizza2)
nypd_sprites = RenderPlain(nypd, blacknypd)
black_sprites = RenderPlain(blacknypd1)
colleen_sprites = RenderPlain(colleen)


DELAY = 600;

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits

# screen.fill(black)
# start = f.render("START", False, (255, 255, 255))
# screen.blit(start, (310, 310))
# display.update()
nypd_time_counter = 0
once = 0
while True:
    #pygame.sprite.LayeredUpdates.move_to_front(colleen)
    nypd_time_counter += 1

    e = event.poll()

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
        if colleen.hit(pizza2):
            mixer.Sound("pop.wav").play()
            pizza1.move()
            hits += 100
        if colleen.hit(nypd):
            mixer.Sound("Star.wav").play()
            nypd.move()
            hits += 500 
        if colleen.hit(blacknypd):
            mixer.Sound("mappipe.wav").play()
            blacknypd.move()
            hits -= 500
        if colleen.hit(blacknypd1):
            mixer.Sound("mappipe.wav").play()
            blacknypd.move()
            hits -= 500
        time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # time passed
        pizza.move()
        pizza1.move()
        pizza2.move()
        #nypd.move()
        #blacknypd.move()


    elif hits < 0:
        mixer.Sound("Byebye.wav").play()
        screen.fill(black)
        gameover = f.render("GAME OVER", False, (255, 255, 255))
        final_score = f.render("FINAL SCORE: " + str(hits), False, (255, 255, 255))
        screen.blit(gameover, (310, 310))
        screen.blit(final_score, (250, 370))
        display.update()
        break 

    elif hits > 2000:
        mixer.Sound("fanfare.wav").play()
        screen.fill(green)
        win = f.render("YOU WIN!", False, (255, 255, 255))
        win_display = f.render("FINAL SCORE: " + str(hits), False, (255, 255, 255))
        screen.blit(win, (330, 290))
        screen.blit(win_display, (250, 350))
        display.update()
        break





    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("PIZZA SCORE = " + str(hits), False, (255, 255, 255))
    tt = f.render("SCORE OVER 2000 TO WIN", False, (255, 255, 255))
    screen.blit(t, (0, 0))      # draw text to screen.  Can you move it?
    screen.blit(tt, (0, 35))


    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    if nypd_time_counter>100 and nypd_time_counter<155:
        nypd_sprites.update()
        nypd_sprites.draw(screen)
        black_sprites.update()
        black_sprites.draw(screen)
    if nypd_time_counter == 155:
        nypd_time_counter = 0
        nypd.move()
        blacknypd.move()
        #nypd_sprites.update()
        #nypd_sprites.draw(screen)
    colleen_sprites.update()
    colleen_sprites.draw(screen)

    display.update()



