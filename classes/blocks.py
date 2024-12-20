from classes.block import Block
from classes.position import Position

class IBlock(Block):
    """
    Represents the 'I' shaped block. This block consists of 4 cells arranged
    in a straight line, either horizontally or vertically.
    """
    def __init__(self):
        super().__init__(id=1)  # ID used for color
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],  # Vertical
            1: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],  # Horizontal
            2: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],  # Vertical
            3: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],  # Horizontal
        }
        self.move(0, 3)  # Initial position

class OBlock(Block):
    """
    Represents the 'O' shaped block (a square). This block does not rotate.
    """
    def __init__(self):
        super().__init__(id=2)  # ID used for color
        shape = [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]  # Square shape
        self.cells = {0: shape, 1: shape, 2: shape, 3: shape}  # Same shape for all rotations
        self.move(0, 4)  # Initial position

class TBlock(Block):
    """
    Represents the 'T' shaped block. This block has 4 rotation states.
    """
    def __init__(self):
        super().__init__(id=3)  # ID used for color
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],  # Base with top center
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 2)],  # Vertical
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],  # Upside-down T
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 0)],  # Vertical flipped
        }
        self.move(0, 3)  # Initial position

class JBlock(Block):
    """
    Represents the 'J' shaped block. This block has 4 rotation states.
    """
    def __init__(self):
        super().__init__(id=4)  # ID used for color
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],  # L flipped
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 0)],  # Upside-down J
            2: [Position(1, 2), Position(1, 1), Position(1, 0), Position(2, 2)],  # Reverse L
            3: [Position(0, 2), Position(0, 1), Position(1, 1), Position(2, 1)],  # J flipped
        }
        self.move(0, 3)  # Initial position

class LBlock(Block):
    """
    Represents the 'L' shaped block. This block has 4 rotation states.
    """
    def __init__(self):
        super().__init__(id=5)  # ID used for color
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],  # Normal L
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],  # Vertical L
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],  # L flipped horizontally
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],  # Vertical flipped
        }
        self.move(0, 3)  # Initial position

class SBlock(Block):
    """
    Represents the 'S' shaped block. This block has 4 rotation states.
    """
    def __init__(self):
        super().__init__(id=6)  # ID used for color
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],  # S shape
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],  # Vertical flipped
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],  # S flipped horizontally
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],  # Reverse S
        }
        self.move(0, 3)  # Initial position

class ZBlock(Block):
    """
    Represents the 'Z' shaped block. This block has 4 rotation states.
    """
    def __init__(self):
        super().__init__(id=7)  # ID used for color
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],  # Z shape
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],  # Vertical Z
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],  # Z flipped horizontally
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)],  # Reverse Z
        }
        self.move(0, 3)  # Initial position
