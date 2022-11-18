import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A virutal motorcycle leaving a solid trail behind it as it travels around the screen.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _units (int): The units of speed the power_up is worth.
    """
    def __init__(self, color, x, y, d):
        super().__init__()
        self._postion = Point(x,y)
        self._color = color
        self._segments = []
        self._prepare_cycle()
        self._velocity = Point(d * 1, 0)
        self._sheild = 0

    def get_segments(self):
        return self._segments

    def move_next(self):
        self._segments[0].move_next()
        self.grow_tail()
        

    def get_cycle(self):
        return self._segments[0]

    def grow_tail(self):

        tail = self._segments[0]
        position = tail.get_position() 
            
        segment = Actor()
        segment.set_position(position)
        segment.set_text("#")
        segment.set_color(constants.GREEN)
        self._segments.append(segment)

    def turn_cycle(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_cycle(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._color
             
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def get_sheild(self):
        return self._sheild
