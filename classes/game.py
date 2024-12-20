from classes.grid import Grid
from classes.blocks import *
import random

class Game:
    """
    Represents the main game logic, including the grid, current block, and block movement.
    """
    def __init__(self):
        """
        Initializes the game with a grid, a list of available blocks, 
        and randomly selects the current and next block.
        """
        self.grid = Grid()  # Game grid where blocks are placed
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock()
        ]  # List of block types
        self.current_block = self.get_random_block()  # Block currently being controlled by the player
        self.next_block = self.get_random_block()  # The next block to be used

    def get_random_block(self):
        """
        Randomly selects a block from the list of available blocks. If all blocks 
        have been used, it resets the block pool.

        Returns:
            Block: A randomly chosen block.
        """
        if len(self.blocks) == 0:  # Refill block pool if empty
            self.blocks = [
                IBlock(),
                JBlock(),
                LBlock(),
                OBlock(),
                SBlock(),
                TBlock(),
                ZBlock()
            ]
        block = random.choice(self.blocks)  # Randomly select a block
        self.blocks.remove(block)  # Remove the block from the list to avoid repetition
        return block
    
    def move_left(self):
        """
        Moves the current block one step to the left. If the move results in 
        the block being outside the grid, it is undone.
        """
        self.current_block.move(0, -1)  # Move left
        if not self.is_block_inside_grid():  # Undo if out of bounds
            self.current_block.move(0, 1)

    def move_right(self):
        """
        Moves the current block one step to the right. If the move results in 
        the block being outside the grid, it is undone.
        """
        self.current_block.move(0, 1)  # Move right
        if not self.is_block_inside_grid():  # Undo if out of bounds
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Moves the current block one step downward. If the move results in 
        the block being outside the grid, it is undone.
        """
        self.current_block.move(1, 0)  # Move down
        if not self.is_block_inside_grid():  # Undo if out of bounds
            self.current_block.move(-1, 0)

    def is_block_inside_grid(self):
        """
        Checks if the current block is entirely within the grid boundaries.

        Returns:
            bool: True if the block is within the grid, False otherwise.
        """
        tiles = self.current_block.get_cell_positions()  # Get all tile positions of the block
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):  # Check each tile's position
                return False
        return True

    def draw(self, screen):
        """
        Draws the grid and the current block on the given screen.

        Args:
            screen (pygame.Surface): The Pygame surface to draw on.
        """
        self.grid.draw(screen)  # Draw the grid
        self.current_block.draw(screen)  # Draw the current block
