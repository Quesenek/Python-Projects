import time
import os
import pathlib

def main():
    clear = lambda: os.system('cls')

    renderingAmount = 40
    
    x = readIn()
    displayList = []
    startIn = 0
    endIn = renderingAmount-1

    print(x)

    time.sleep(0.1)

    clear()
    # x.append(x[0])
    # x.remove(x[0])

    # print(x)
    displayList = moveDownList(startIn, endIn, x)
    displayText = ""
    for ix in displayList:
        displayText += ix
        time.sleep(0.005)
        clear()
        print(displayText)
    
    startIn += 1
    endIn += 1
    for i in range(0, 1000):
        displayText = ""
        for ix in range(startIn, endIn, 1):
            displayText += x[ix]
        time.sleep(0.005)
        clear()
        print(displayText)

        startIn += 1
        endIn += 1


def readIn():
    f = open(f"{pathlib.Path(__file__).parent.absolute()}\\textTest.txt", "r")

    textList = []

    for x in f:
        textList.append(x)

    return textList

def moveDownList(startIndex, endIndex, list):

    newList = []

    for i in range(startIndex, endIndex, 1):
        newList.append(list[i])

    return newList

if __name__ == "__main__":
    main()