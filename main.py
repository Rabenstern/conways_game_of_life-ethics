import pygame
# import time
# import random
# import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

SCALER = 30
OFFSET = 1

Grid = grid.Grid(width, height, SCALER, OFFSET)
Grid.random2d_array()

PAUSE = False
RUN = True
while RUN:
    clock.tick(FPS)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                RUN = False
            if event.key == pygame.K_SPACE:
                PAUSE = not PAUSE

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=PAUSE)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    pygame.display.update()

pygame.quit()
