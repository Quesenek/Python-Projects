import pygame, sys, math, random, time
from pygame.locals import *

#Set up pygame
pygame.init()

windowHeight = 512
windowWidth = 400

barColorType = "Color" # Color for color and Grey for greyscale
background = (255, 255, 255)

frameLimit = 0.1

barHeight = 1
count = 0
countLimit = (10)
iteration = 0
iterationLimit = 9
iterationUp = True
transitionDown = False

iteratorList = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)


#Set up the window
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0 , 32)
pygame.display.set_caption('Playing Around')

#increase and then decrease the bar size
def barSize():
    global count
    global countLimit
    global iteration
    global iterationLimit
    global iterationUp
    global barHeight
    global transitionDown

    if(count < countLimit):
        count += 1
    elif (count >= countLimit):
        if((iteration + 1) > iterationLimit and transitionDown == False):
            iterationUp = False
            transitionDown = True
        elif((iteration - 1) < 0 and transitionDown == True):
            iterationUp = True
            transitionDown = False
        if(iterationUp):
            iteration += 1
        else:
            iteration -= 1
        
        count = 0
    
    barHeight = iteratorList[iteration]

def randColor():
    if(barColorType == "Color"):
        COLOR = (random.randint(0, 254),random.randint(0, 254),random.randint(0, 254))
    else:
        colo = random.randint(0, 254)
        COLOR = (colo,colo,colo)
    return COLOR

def randWidth():
    randomWidth =  windowWidth - random.randint(10, windowWidth)
    return randomWidth

#Draw the white background onto the surface
windowSurface.fill(background)

def circle():
    #Draw a red circle onto the surface
    circleWidth = 125
    # circle1 = pygame.draw.circle(windowSurface, randColorUpdate(), (0,(windowHeight/2)), circleWidth)
    # circle2 = pygame.draw.circle(windowSurface, randColorUpdate(), (windowWidth,(windowHeight/2)), circleWidth)
    # circle3 = pygame.draw.circle(windowSurface, randColorUpdate(), ((windowWidth/2),0), circleWidth)
    # circle4 = pygame.draw.circle(windowSurface, randColorUpdate(), ((windowWidth/2),windowHeight), circleWidth)

    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.1)


def square():
    windowSurface.fill(background)
    barSize()
    
    for i in range(0, windowHeight, barHeight):
        randomWidth = randWidth()
        rect1 = pygame.draw.rect(windowSurface, (0, 0, 0), (0, i, randomWidth, barHeight))
        rect2 = pygame.draw.rect(windowSurface, randColor(), (randomWidth, i, (windowWidth-randomWidth), barHeight))

    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(frameLimit)


#Run the game loop
while True:
    square()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()