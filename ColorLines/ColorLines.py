import pygame, sys, math, random, time
from pygame.locals import *

#Set up pygame
pygame.init()

windowHeight = 480
windowWidth = 400

#Set up the window
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0 , 32)
pygame.display.set_caption('Playing Around')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
colorArray = (BLACK, RED, GREEN, BLUE)


def randColorUpdate():
    return colorArray[random.randint(0,3)]
def randColor():
    COLOR = (random.randint(0, 254),random.randint(0, 254),random.randint(0, 254))
    return COLOR
def randWidth():
    randomWidth =  windowWidth - random.randint(10, windowWidth)
    return randomWidth

#Draw the white background onto the surface
windowSurface.fill(WHITE)

def circle():
    #Draw a red circle onto the surface
    circleWidth = 125
    circle1 = pygame.draw.circle(windowSurface, randColorUpdate(), (0,(windowHeight/2)), circleWidth)
    circle2 = pygame.draw.circle(windowSurface, randColorUpdate(), (windowWidth,(windowHeight/2)), circleWidth)
    circle3 = pygame.draw.circle(windowSurface, randColorUpdate(), ((windowWidth/2),0), circleWidth)
    circle4 = pygame.draw.circle(windowSurface, randColorUpdate(), ((windowWidth/2),windowHeight), circleWidth)

    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.1)


def square():
    windowSurface.fill(WHITE)
    
    for i in range(0, windowHeight, 8):
        randomWidth = randWidth()
        rect5 = pygame.draw.rect(windowSurface, randColor(), (0, i, randomWidth, 8))
        rect6 = pygame.draw.rect(windowSurface, randColor(), (randomWidth, i, (windowWidth-randomWidth), 8))


    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.1)


#Run the game loop
while True:
    square()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()