# (c) Rabenstern 2024
from tkinter import Tk  # for screen resolution
import time
import os
import pygame
# import random
# import numpy as np
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
root = Tk()  # create tkinter root to determin resolution

height = root.winfo_screenheight()  # getting screen's height in pixels
width = root.winfo_screenwidth()  # getting screen's width in pixels
# width, height = 1920, 1080
size = (width, height)
print(size)

# init pygame
pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30

# define colors
black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

# generate grid
SCALER = 30
OFFSET = 1

Grid = grid.Grid(width, height, SCALER, OFFSET)
Grid.random2d_array()

# driver loop
PAUSE = False
RUN = True
while RUN:
    clock.tick(FPS)
    screen.fill(black)

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                RUN = False
            if event.key == pygame.K_SPACE:
                PAUSE = not PAUSE

    # generate grid
    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=PAUSE)

    # check mouse event
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    # update display
    pygame.display.update()
    time.sleep(0.5)  # delay


pygame.quit()
