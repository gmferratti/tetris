from classes.grid import Grid
from classes.blocks import *
import random
import pygame
import sys

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
        if self.can_move_block(self.current_block, 0, -1):
            self.current_block.move(0, -1)

    def move_right(self):
        """
        Moves the current block one step to the right. If the move results in 
        the block being outside the grid, it is undone.
        """
        if self.can_move_block(self.current_block, 0, 1):
            self.current_block.move(0, 1)

    def move_down(self):
        """
        Moves the current block one step downward. If the move results in 
        the block being outside the grid, it is undone.
        """
        if self.can_move_block(self.current_block, 1, 0):
            self.current_block.move(1, 0)
        else:
            # If the block cannot move down, it has landed
            self.lock_block()
            self.spawn_new_block()
    
    def rotate(self):
        """
        Rotates the current block clockwise. If the rotation results in the block 
        being outside the grid, it is undone.
        """
        self.current_block.rotate()

    

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
    
    def can_move_block(self, block, row_offset, col_offset):
        """
        Checks if the current block can move to a new position.

        Args:
            block (Block): The block to check.
            row_offset (int): The row offset to apply.
            col_offset (int): The column offset to apply.

        Returns:
            bool: True if the block can move, False otherwise.
        """
        for cell in block.get_cell_positions():
            # Calculate the new position of each cell after the offset
            new_row = cell.row + row_offset
            new_col = cell.col + col_offset

            # Check if the new position is outside the grid boundaries
            if not self.grid.is_inside(new_row, new_col):
                return False

            # Check if the new position collides with an occupied cell in the grid
            if self.grid.grid[new_row][new_col] != 0:
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

    def lock_block(self):
        """
        Locks the current block into the grid and updates the grid state.
        """
        for cell in self.current_block.get_cell_positions():
            self.grid.grid[cell.row][cell.col] = self.current_block.id
    
    def spawn_new_block(self):
        """
        Spawns a new block at the top of the grid. If the new block collides immediately,
        the game is over.
        """
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        if not self.can_move_block(self.current_block, 0, 0):
            self.game_over()

    def game_over(self):
        """
        Handles the game-over state.
        """
        print("Game Over!")
        pygame.quit()
        sys.exit()