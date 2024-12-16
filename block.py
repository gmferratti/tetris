from graphics import color_palette
import pygame

class Block:
    def __init__(self, id=0):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = self.get_cell_colors()
    
    def get_cell_colors(self):
        rgb_values = [rgb for rgb in color_palette.values()]
        return rgb_values
    
    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.col * self.cell_size +1,
                tile.row * self.cell_size+1,
                self.cell_size -1,
                self.cell_size -1,
            )
            pygame.draw.rect(
                screen,
                self.colors[self.id],
                tile_rect)
