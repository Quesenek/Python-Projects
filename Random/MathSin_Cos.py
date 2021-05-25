import pygame, sys
import math
import random
import time

def main():
    screen_width = 640
    screen_height = 480

    FPS = 60
    fpsClock = pygame.time.Clock()

    x_bounds_lower = 0
    x_bounds_upper = screen_width

    cycles = 5
    scale = 20

    trigOp = [math.sin, math.cos, math.tan]

    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill([0, 0, 0])

    while True:

        drawLogic(screen, trigOp, cycles, scale, screen_height, x_bounds_lower, x_bounds_upper)
        x_bounds_upper += 1
        x_bounds_lower += 1
            
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)


def drawLogic(screen, trigOp, cycles, scale, screen_height, x_bounds_lower, x_bounds_upper):
    plotPoints0 = []
    plotPoints1 = []
    plotPoints2 = []
    
    for x in range(x_bounds_lower, x_bounds_upper):
        y = int(trigOp[0]((x/640 * cycles * math.pi)/((math.floor(x/640 * cycles * math.pi)+1))) * scale + ((screen_height/2))-180)#-200
        plotPoints0.append([x, y])

    for x in range(x_bounds_lower, x_bounds_upper):
        y = int(trigOp[1]((x/640 * cycles * math.pi)/((math.floor(x/640* cycles * math.pi)+1))) * scale + ((screen_height/2))-80)#-100
        plotPoints1.append([x, y])

    for x in range(x_bounds_lower, x_bounds_upper):
        y = int(trigOp[2]((x/640 * cycles * math.pi)+((math.floor(x/640 * cycles * math.pi)*2))) * scale + ((screen_height/2))+80)#+80
        plotPoints2.append([x, y])

    for i, x in enumerate(plotPoints0):
        plotPoints0[i][0] = i
    for i, x in enumerate(plotPoints1):
        plotPoints1[i][0] = i
    for i, x in enumerate(plotPoints2):
        plotPoints2[i][0] = i

    screen.fill([0, 0, 0])

    # pygame.draw.lines(screen, [255, 255, 255], False, plotPoints0, 2)
    # pygame.draw.lines(screen, [255, 255, 255], False, plotPoints1, 2)
    pygame.draw.lines(screen, [255, 255, 255], False, plotPoints2, 2)


if __name__ == "__main__":
    main()



