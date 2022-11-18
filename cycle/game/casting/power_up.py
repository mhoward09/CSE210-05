import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Power_up(Actor):
    """
    An item that will help a cycle driver win the game.
    
    The responsibility of Power_up is to select a random position and give the cycle an shield to protect it from a collision.

    Attributes:
        _units (int): The number of units the power_up adds to the cycle.
    """
    def __init__(self):
        "Constructs a new Power_up."
        super().__init__()
        self._units = 1
        self.set_text("@")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position for that the power_up is worth."""
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_units(self):
        """Gets the units of speed the power_up is worth.
        
        Returns:
            units (int): The units of speed the power_up is worth.
        """
        return self._units