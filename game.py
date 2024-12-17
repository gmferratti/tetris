import sys
import pygame
from graphics import color_palette
from grid import Grid
from blocks import *

# Config
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris 3000")

clock = pygame.time.Clock()

game_grid = Grid()

block = IBlock()
game_grid.print_grid()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Drawing Grid
        screen.fill(color_palette["BG"])
        game_grid.draw(screen)
        block.draw(screen)

        pygame.display.update()
        clock.tick(60)