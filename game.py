import pygame
from grid import Grid

surface = pygame.display.set_mode((600, 600))  # setting window height and width
pygame.display.set_caption("8-puzzle")
grid = Grid()  # grid object to draw the GUI

running = True

while running:
    for event in pygame.event.get():  # program is not responding without this block fa sebo :D
        if event.type == pygame.QUIT:
            running = False

    surface.fill((0, 0, 0))

    grid.draw(surface)

    pygame.display.flip()               # to fill all the window
