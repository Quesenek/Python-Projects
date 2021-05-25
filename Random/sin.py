import math
import pygame

upperBounds = 12
lowerBounds = 0
pygame.init()
screen = pygame.display.set_mode([500, 500])
screen.fill((0, 0, 0))

for i in range(lowerBounds, upperBounds, 1):
    x = float("%0.5f" % math.cos(i/upperBounds * 3 * math.pi))
    print(f"{i}, {x}")
    pygame.draw.ellipse(screen, [255, 23, 240, 0], (250, 250, 30, 50), 2)

pygame.display.flip()

# Set up the drawing window





# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    

    # Draw a solid blue circle in the center

    # Flip the display
    

# Done! Time to quit.
pygame.quit()

