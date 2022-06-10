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



screen = pygame.display.set_mode([500, 1000])

running = True
x = 200
y = 100
z = 1000
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                if x != 0:
                    x = x - 50
            if event.key == K_RIGHT:
                if x != 450:
                    x = x + 50

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 50, 50))
    if y < 950:
        if z == 1000:
            y = y + 50
            z = 0
        z = z + 1
    
    pygame.display.flip()

pygame.quit()