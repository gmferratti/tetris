import sys
import pygame
from classes.graphics import color_palette
from classes.game import Game

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

# Drop interval in miliseconds
drop_interval = 500
drop_timer = 0

while not game_over:
    dt = clock.tick(60)
    drop_timer += dt

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
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_SPACE:
                game.rotate()
                
    
    # Check for key presses to allow continuous movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game.move_left()
    if keys[pygame.K_RIGHT]:
        game.move_right()
    if keys[pygame.K_DOWN]:
        game.move_down()   

    # automatic drop movement
    if drop_timer >= drop_interval:
        game.move_down()
        drop_timer = 0

    # Drawing Grid
    screen.fill(color_palette["BG"])
    game.draw(screen)

    pygame.display.update()