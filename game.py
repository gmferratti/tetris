import sys
import pygame
from graphics import color_palette
from grid import Grid
from blocks import *

# Config
pygame.init()
pygame.mixer.init()

# Sound
pygame.mixer.music.load("bgm/main_theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Screen
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris 3000")

# Clock
clock = pygame.time.Clock()

# Grid
game_grid = Grid()
block = IBlock()
game_grid.print_grid()

# Main Loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.music.stop()
            game_over = True
        
        # Drawing Grid
        screen.fill(color_palette["BG"])
        game_grid.draw(screen)
        block.draw(screen)

        pygame.display.update()
        clock.tick(60)