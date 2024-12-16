import sys
import pygame
from graphics import color_palette
from grid import Grid

# Config
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Tetris 3000")

clock = pygame.time.Clock()

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[0][1] = 2
game_grid.print_grid()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Drawing Grid
        screen.fill(color_palette["Deep Ocean Blue"])
        game_grid.draw(screen)

        pygame.display.update()
        clock.tick(60)