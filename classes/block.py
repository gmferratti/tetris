from classes.graphics import color_palette
from classes.position import Position
import pygame

class Block:
    """
    Represents a block in Tetris.
    """
    def __init__(self, id=0):
        """
        Initializes a Block object.

        Args:
            id (int, optional): Block ID, default is 0.
        """
        self.id = id
        self.cells = {}  # Stores rotation states with positions of cells
        self.cell_size = 30  # Size of a single cell in pixels
        self.row_offset = 0  # Initial vertical position offset
        self.col_offset = 0  # Initial horizontal position offset
        self.rotation_state = 0  # Default rotation state
        self.colors = self.get_cell_colors()  # Load color palette for blocks
    
    def get_cell_positions(self):
        """
        Computes the positions of all cells in the block 
        considering the current offset and rotation.

        Returns:
            list: A list of `Position` objects with updated positions.
        """
        tiles = self.cells[self.rotation_state]  # Current rotation state
        moved_tiles = []
        for position in tiles:
            # Apply row and column offsets to each position
            position = Position(
                position.row + self.row_offset,
                position.col + self.col_offset
            )
            moved_tiles.append(position)
        return moved_tiles

    def get_cell_colors(self):
        """
        Retrieves the list of colors from the global color palette.

        Returns:
            list: A list of RGB tuples representing colors.
        """
        return [rgb for rgb in color_palette.values()]
    
    def move(self, rows, cols):
        """
        Moves the block by adjusting its row and column offsets.

        Args:
            rows (int): Number of rows to move.
            cols (int): Number of columns to move.
        """
        self.row_offset += rows
        self.col_offset += cols
    
    def draw(self, screen):
        """
        Draws the block on the given screen using its current state and color.

        Args:
            screen (pygame.Surface): The Pygame surface to draw on.
        """
        tiles = self.get_cell_positions()  # Get positions of all tiles
        for tile in tiles:
            # Create a rectangle for each tile in the block
            tile_rect = pygame.Rect(
                tile.col * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            # Draw the rectangle with the block's color
            pygame.draw.rect(
                screen,
                self.colors[self.id],  # Color based on block ID
                tile_rect
            )