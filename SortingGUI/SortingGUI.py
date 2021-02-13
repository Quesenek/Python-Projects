import pygame, sys, math, random, time
from pygame.locals import *

#Set up pygame
pygame.init()

windowHeight = 512
windowWidth = 800
numAmount = 8
barSize = int(math.floor(windowWidth / numAmount))

background = (125, 180, 200)

frameLimit = 0.1

#Set up the window
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0 , 32)
pygame.display.set_caption('Playing Around')

def generateRectangles():

    tempArray = {}
    barArray1 = {}
    barArray2 = {}

    for i in range(0, (numAmount*barSize), barSize):
        if(i == 0):
            i2=0.5
            barArray1[(i/barSize)] = (math.floor(i), (windowHeight-((i2)/numAmount)*windowHeight), barSize, (windowHeight-((((i2)/numAmount)*windowHeight)-windowHeight)*-1))
        else:
            barArray1[(i/barSize)] = (math.floor(i), (windowHeight-((i/barSize)/numAmount)*windowHeight), barSize, (windowHeight-((((i/barSize)/numAmount)*windowHeight)-windowHeight)*-1))

    for i in range(0, numAmount, 1):
        tempArray[i] = barArray1[math.floor((numAmount-1)-i)][0]
        
    for i in range(0, numAmount, 1):
        barArray2[i] = (tempArray[i], barArray1[i][1], barArray1[i][2], barArray1[i][3])

    random.shuffle(barArray2)
    
    return barArray2

# bar = {}
# bar[0] = (int(windowHeight-(10/100)*windowHeight), 8, int(windowHeight-(((10/100)*windowHeight)-windowHeight)*-1)) #number working

barArray = generateRectangles()

def display():
    global barArray
        
    windowSurface.fill(background)
    for i in range(0, numAmount, 1):
        pygame.draw.rect(windowSurface, (100, 0, random.randint(0,254)), (i*barSize, barArray[i][1], barArray[i][2], barArray[i][3]))
    
    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(frameLimit)

display()
#Run the game loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()