import pygame, sys, math, random, time
from pygame.locals import *
import pygame.gfxdraw


barArray = []

def pyMain():
    windowHeight = 256
    windowWidth = 1024
    numAmount = 1024
    barSize = int(math.floor(windowWidth / numAmount))
    
    background = (0, 0, 0) # (125, 180, 200) (0, 0, 0)
    barColor = [255, 255, 0] #[100, 0, None] [69, 69, 69]
    borderColor = [0, 127, 127] #[100, 0, None] [255, 255, 255]
    frameLimit = 0.00

    shuffleArray = True
    border = False
    looping = False

    direction = "up"

    windowSurface = pyInit(windowWidth, windowHeight)

    global barArray
    barArray = generateRectangles(numAmount, barSize, windowHeight, shuffleArray)
    # display(windowSurface, background, numAmount, barSize, barArray, frameLimit, barColor, borderColor, border)
    displayParams = [windowSurface, background, numAmount, barSize, barArray, frameLimit , barColor, borderColor, border, direction]
    bubbleSort(barArray, displayParams[9], displayParams)
    #bSortMain(barArray, displayParams)
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
    # barArray [index or location, top location, width, height of bar, bar value]
    for i in range(0, (numAmount*barSize), barSize):
        x = random.randint(1, numAmount)
        # if(i == 0):
        #     i2=0.5
        #     barArray.append([0, (windowHeight-((i2)/numAmount)*windowHeight), barSize, (windowHeight-((((i2)/numAmount)*windowHeight)-windowHeight)*-1), 0])
        # else:
        #     barArray.append([0, (windowHeight-((i/barSize)/numAmount)*windowHeight), barSize, (windowHeight-((((i/barSize)/numAmount)*windowHeight)-windowHeight)*-1), int(i/barSize)])

        if(i == 0):
            i2=0.5
            barArray.append([0, (windowHeight-((x)/numAmount)*windowHeight), barSize, (windowHeight-((((x)/numAmount)*windowHeight)-windowHeight)*-1), x])
        else:
            barArray.append([0, (windowHeight-((x)/numAmount)*windowHeight), barSize, (windowHeight-((((x)/numAmount)*windowHeight)-windowHeight)*-1), int(x)])

    if(shuffleArray):
        random.shuffle(barArray)
    
    for i in range(0, numAmount, 1):
        barArray[i][0] = i*barSize

    

    return barArray

# bar = {}
# bar[0] = (int(windowHeight-(10/100)*windowHeight), 8, int(windowHeight-(((10/100)*windowHeight)-windowHeight)*-1)) #number working

def display(windowSurface, background, numAmount, barSize, barArray, frameLimit, barColor, borderColor, border, value):
    
    
    windowSurface.fill(background)
    for i in range(0, numAmount, 1):
        if(i == value):
            pygame.draw.rect(windowSurface, 
                                        (255, 
                                         0, 
                                         0), 
                                                                                                           (barArray[i][0], barArray[i][1], barArray[i][2], barArray[i][3]))
        else:        
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

def bubbleSort(array, direction, displayParams):
    value = 0
    print(value)

    barsArray = displayParams[4]
    display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], barsArray, displayParams[5], displayParams[6], displayParams[7], displayParams[8], None)

    time.sleep(2)

    while(True):
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT:
                endGameLoop()
        stillSorting = True
        for i in range (0, displayParams[2]-1, 1):
            print(barsArray[i][4])
            
            if(barsArray[i][4] > barsArray[i+1][4]):
                stillSorting = False
                barsArray[i], barsArray[i+1] = barsArray[i+1], barsArray[i]

                for j in range(0, displayParams[2], 1):
                    barsArray[j][0] = j*displayParams[3]

                displayParams[4] = barsArray
                display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], displayParams[4], displayParams[5], displayParams[6], displayParams[7], displayParams[8], i)
        if stillSorting == True:
            display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], displayParams[4], displayParams[5], displayParams[6], displayParams[7], displayParams[8], None)
            break
            
def partition(arr, low, high, displayParams):
    i = (low-1)
    pivot = arr[high][4]

    for j in range(low, high):
        print(arr[j][4])
        temp = arr[j][4]
        if temp <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
            pygame.event.get()
            display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], arr, displayParams[5], displayParams[6], displayParams[7], displayParams[8], None)
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    arr[i+1][0], arr[high][0] = arr[high][0], arr[i+1][0]
    
    # for x in range(0, len(arr)):
    #     arr[x][0] = x*displayParams[3]

    returnArr = [(i+1)]

    return returnArr

def quickSort(arr, low, high, displayParams):
    pygame.event.get()
    time.sleep(displayParams[5])
    if len(arr) == 1:
        return arr
    if low < high:

        retPi = partition(arr, low, high, displayParams)

        pi = retPi[0]
        
        display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], arr, displayParams[5], displayParams[6], displayParams[7], displayParams[8], pi)
        
        quickSort(arr, low, pi-1, displayParams)
        quickSort(arr, pi+1, high, displayParams)
    display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], arr, displayParams[5], displayParams[6], displayParams[7], displayParams[8], None)

def bSortMain(array, displayParams):
    time.sleep(3)

    arr = displayParams[4]
    n = len(arr)
    display(displayParams[0], displayParams[1], displayParams[2], displayParams[3], arr, displayParams[5], displayParams[6], displayParams[7], displayParams[8], None)
    quickSort(arr, 0, n-1, displayParams)
    


def endGameLoop():
    pygame.quit()
    sys.exit()

def startLoop(looped, displayParams):

    global barArray

    #Run the game loop
    while True:
        if (looped == True):
            pass
            
        for event in pygame.event.get():
            if event.type == QUIT:
                endGameLoop()


if __name__ == "__main__":
    pyMain()