import pygame, sys, math, random, time
from pygame.locals import *

pygame.init()

windowHeight = 512
windowWidth = 512
blockWidth = 16
randomChance = 0.45

#Set up the window
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0 , 32)
pygame.display.set_caption('Playing Around')

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
colorArray = (BLACK, RED, GREEN, BLUE)

windowSurface.fill(WHITE)

def createRandom():
    for y in range(0, int(windowHeight/blockWidth), 1):
        for x in range(0, int(windowWidth/blockWidth), 1):            
            if(random.random() < randomChance):
                pygame.draw.rect(windowSurface, RED, (x*blockWidth, y*blockWidth, blockWidth, blockWidth))
            pygame.display.update()
    


createRandom()
pygame.display.update()
#Run the game loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
