# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
x = 20
z = 1
y = 250
# Run until the user asks to quit
running = True
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_LEFT:
                if z == 0:
                    x -= 50
                elif z == 1:
                    z = 0
            if event.key == K_RIGHT:
                if z == 1:
                    x += 50
                elif z == 0:
                    z = 1
            if event.key == K_ESCAPE:
                running = False

    

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (5, 239, 86), (x, y), 50)
    if x<450 and z == 1 and y < 450:
        x = x +.1
 
    elif x>50 and y < 450:
        x = x - .1
        z = 0

    else:
        z = 1


   
    

    # Flip the display
    pygame.display.flip()

    

# Done! Time to quit.
pygame.quit()