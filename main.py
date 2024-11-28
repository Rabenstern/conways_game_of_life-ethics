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
red = (255, 0, 0)
teal = (0, 171, 187)

# generate grid
SCALER = 30
OFFSET = 1

Grid = grid.Grid(width, height, SCALER, OFFSET)
Grid.random2d_array()


class Player:
    """
    This is the documentation for MyClass.

    Attributes:
        x (int): x position of Player
        y (int): y position of Player

    Methods:
        draw(): color Player's position
        updatePos(): update the Player's position
    """

    x = 0
    y = 0

    def __init__(self, w, h):
        """
        place Player in center of screen

        Args:
            w (int): screen width in pixels
            h (int): screen height in pixels

        Returns:
            void

        Examples:
            >>> p = Player(w, h)
        """
        self.x = round(w/2/Grid.scale)
        self.y = round(h/2/Grid.scale)

    # color a specific field
    def draw(self, s):
        """
        color the field where Player is

        Args:
            s (): pyame surface to draw to

        Returns:
            void

        Examples:
            >>> p.draw(surface)
        """
        pygame.draw.rect(
            s,
            teal,
            [
                self.x * Grid.scale,
                self.y * Grid.scale,
                Grid.scale-Grid.offset,
                Grid.scale-Grid.offset
            ]
        )

    def updatePos(self, x, y):
        """
        update the position of Player by activating Player's new
        field and deactivating Player's old one

        Args:
            x (int): Player new x position
            y (int): Player new y position

        Returns:
            void

        Examples:
            >>> p.updatePos(x, y)
        """
        if Grid.grid_array[self.x][self.y] is not None:
            Grid.grid_array[self.x][self.y] = 0
        self.x = x
        self.y = y
        if Grid.grid_array[x][y] is not None:
            Grid.grid_array[x][y] = 1


p = Player(width, height)

# driver loop
PAUSE = False
RUN = True
while RUN:
    clock.tick(FPS)
    screen.fill(black)

    x = p.x
    y = p.y

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                RUN = False
            if event.key == pygame.K_SPACE:
                PAUSE = not PAUSE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
            if event.key == pygame.K_RIGHT:
                x += 1
            if event.key == pygame.K_UP:
                y -= 1
            if event.key == pygame.K_DOWN:
                y += 1

    # generate grid
    p.updatePos(x, y)
    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=PAUSE)
    p.draw(screen)

    # check mouse event
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    # update display
    pygame.display.update()
    time.sleep(0.5)  # delay


pygame.quit()
