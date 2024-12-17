import sys
import pygame
from graphics import color_palette
from game import Game

# Config
pygame.init()
pygame.mixer.init()

# Sound
pygame.mixer.music.load("bgm/main_theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Screen
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris Pythonic 3000")

# Clock
clock = pygame.time.Clock()

game = Game()

# Main Loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.music.stop()
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_SPACE:
                pass
                #game.rotate()
        
        # Drawing Grid
        screen.fill(color_palette["BG"])
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)