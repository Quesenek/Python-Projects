import pygame, sys, math, random, time
from pygame.locals import *
import pygame.gfxdraw



def pyMain():
    windowHeight = 512
    windowWidth = 800
    numAmount = 10
    barSize = int(math.floor(windowWidth / numAmount))
    
    background = (125, 180, 200) # (125, 180, 200) (0, 0, 0)
    barColor = [100, 0, None] #[100, 0, None] [69, 69, 69]
    borderColor = [80, 80, 80] #[100, 0, None] [255, 255, 255]
    frameLimit = 0.1

    shuffleArray = False
    border = False
    looping = True

    windowSurface = pyInit(windowWidth, windowHeight)

    barArray = generateRectangles(numAmount, barSize, windowHeight, shuffleArray)
    display(windowSurface, background, numAmount, barSize, barArray, frameLimit, barColor, borderColor, border)
    displayParams = [windowSurface, background, numAmount, barSize, barArray, frameLimit , barColor, borderColor, border]
    startLoop(looping, displayParams)

def pyInit(windowWidth, windowHeight):
    #Set up pygame
    pygame.init()

    #Set up the window
    windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0 , 32)
    pygame.display.set_caption('Playing Around')

    return windowSurface
    


def generateRectangles(numAmount, barSize, windowHeight, shuffleArray):

    barArray = []

    for i in range(0, (numAmount*barSize), barSize):
        if(i == 0):
            i2=0.5
            barArray.append([0, (windowHeight-((i2)/numAmount)*windowHeight), barSize, (windowHeight-((((i2)/numAmount)*windowHeight)-windowHeight)*-1)])
        else:
            barArray.append([0, (windowHeight-((i/barSize)/numAmount)*windowHeight), barSize, (windowHeight-((((i/barSize)/numAmount)*windowHeight)-windowHeight)*-1)])

    if(shuffleArray):
        random.shuffle(barArray)
    
    for i in range(0, numAmount, 1):
        barArray[i][0] = i*barSize

    return barArray

# bar = {}
# bar[0] = (int(windowHeight-(10/100)*windowHeight), 8, int(windowHeight-(((10/100)*windowHeight)-windowHeight)*-1)) #number working

def display(windowSurface, background, numAmount, barSize, barArray, frameLimit, barColor, borderColor, border):
            
    windowSurface.fill(background)
    for i in range(0, numAmount, 1):
        pygame.draw.rect(windowSurface, 
                                        ((barColor[0] if barColor[0] != None else random.randint(0,254)), 
                                         (barColor[1] if barColor[1] != None else random.randint(0,254)), 
                                         (barColor[2] if barColor[2] != None else random.randint(0,254))), 
                                                                                                           (barArray[i][0], barArray[i][1], barArray[i][2], barArray[i][3]))
        if(border):
            pygame.draw.rect(windowSurface, 
                                        ((borderColor[0] if borderColor[0] != None else random.randint(0,254)), 
                                         (borderColor[1] if borderColor[1] != None else random.randint(0,254)), 
                                         (borderColor[2] if borderColor[2] != None else random.randint(0,254))), 
                                                                                                           (barArray[i][0], barArray[i][1], barArray[i][2], barArray[i][3]), 1)
        
    #Draw the window onto the screen
    pygame.display.update()
    time.sleep(frameLimit)

def endGameLoop():
    pygame.quit()
    sys.exit()

def startLoop(looped, displayParams):
    #Run the game loop
    while True:
        if (looped == True):
            display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], displayParams[4], displayParams[5], displayParams[6], displayParams[7], displayParams[8])
        for event in pygame.event.get():
            if event.type == QUIT:
                endGameLoop()


if __name__ == "__main__":
    pyMain()