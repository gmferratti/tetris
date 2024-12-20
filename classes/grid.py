import pygame
from classes.graphics import color_palette

class Grid:
    """
    Represents the game grid where blocks are placed and interact.

    Attributes:
        num_rows (int): Number of rows in the grid.
        num_cols (int): Number of columns in the grid.
        cell_size (int): Size of each cell in pixels.
        grid (list): 2D list representing the grid's state. Each cell contains a value corresponding to a color ID.
        colors (list): List of RGB color values for the grid cells.
    """
    def __init__(self):
        """
        Initializes the grid with a default size (20x10), empty cells, 
        and assigns colors from the color palette.
        """
        self.num_rows = 20  # Total number of rows in the grid
        self.num_cols = 10  # Total number of columns in the grid
        self.cell_size = 30  # Size of each cell in pixels
        # Creates a blank grid where all cells are initialized to 0 (background color)
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()  # Retrieve the color palette for the cells

    def print_grid(self):
        """
        Prints the current state of the grid to the console.
        Useful for debugging.
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")  # Print each cell value in the row
            print()  # Move to the next line after printing a row

    def is_inside(self, row, col):
        """
        Checks if a given cell position (row, col) is within the grid boundaries.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            bool: True if the cell is within the grid, False otherwise.
        """
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    def get_cell_colors(self):
        """
        Retrieves the list of RGB values for the grid cells from the color palette.

        Returns:
            list: List of RGB tuples representing cell colors.
        """
        return [rgb for rgb in color_palette.values()]

    def draw(self, screen):
        """
        Draws the grid on the given screen. Each cell is drawn as a rectangle 
        filled with the color corresponding to its value in the grid.

        Args:
            screen (pygame.Surface): The Pygame surface where the grid is drawn.
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                # Get the color ID from the grid
                cell_value = self.grid[row][col]
                # Define the rectangle representing the cell
                cell_rect = pygame.Rect(
                    col * self.cell_size,  # X position
                    row * self.cell_size,  # Y position
                    self.cell_size + 1,   # Width (with spacing)
                    self.cell_size + 1    # Height (with spacing)
                )
                # Draw the rectangle with the appropriate color
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
