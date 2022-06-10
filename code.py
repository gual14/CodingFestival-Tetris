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
mat = [
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
]
def placematrix(i,j):
  #insx = round(x//100)
  #insy = round(y//100)
  mat[i][j] = 1

def cube_draw(i, j):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(j*100+5, i*100+5, 90, 90))

def print_matrix(matrix):
  for i in matrix:
    print(*i)
  print()
pygame.init()

def isStop(i,j):
    return i >= 5 or mat[i + 1][j] == 1
def contgame(i,j):
    placematrix(i,j)
    print_matrix(mat)
    #shuld summon new block

screen = pygame.display.set_mode([600, 600])
i = 0
j = 2
running = True
x = 200
y = 100
z = 0
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                if j > 0:
                    #x = x - 100
                    j = j - 1
            if event.key == K_RIGHT:
                if j < 4:
                    #x = x + 100
                    j = j + 1
    screen.fill((0, 0, 0))

    for temp_i in range(len(mat)):
        for temp_j in range(len(mat[temp_i])):
            if mat[temp_i][temp_j] == 1:
                cube_draw(temp_i, temp_j)
                
    cube_draw(i, j)
    if i < 9:
        if z == 750:
            if isStop(i,j):
                contgame(i,j)
                #running = False
                i = 0
                j = 2
            #y = y + 100
            i = i + 1
            z = 0
        z = z + 1

    pygame.display.flip()

pygame.quit()