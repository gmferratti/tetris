import pygame
from graphics import color_palette

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Creates a blank grid
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        # shows up the grid state
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

    def is_inside(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    def get_cell_colors(self):
        rgb_values = [rgb for rgb in color_palette.values()]
        return rgb_values

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col*self.cell_size,
                    row*self.cell_size,
                    self.cell_size + 1,
                    self.cell_size + 1
                )

                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)





