import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A virutal motorcycle leaving a solid trail behind it as it travels around the screen.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _sheild (int): The counter to count how many sheild uses the cycle gets from the power-up.
    """
    def __init__(self, color, x, y):
        super().__init__()
        self._xpos = x
        self._ypos = y
        self._original_color = color
        self._color = color
        self._segments = []
        self._prepare_cycle()
        #we will just set the initial velocity at ControlActorsAction class just like snake
        #self._velocity = Point(d * 1, 0)
        self._sheild = 0
        
    def get_segments(self):
        return self._segments

    def move_next(self):
        self.grow_tail()
        self._segments[0].move_next()
        
    def get_cycle(self):
        return self._segments[0]

    def grow_tail(self):

        tail = self._segments[0]
        position = tail.get_position() 
            
        segment = Actor()
        segment.set_position(position)
        segment.set_text("#")
        segment.set_color(self._color)
        self._segments.append(segment)

    def turn_cycle(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_cycle(self):
        #x = int(constants.MAX_X / 2)
        #y = int(constants.MAX_Y / 2)
        #cycle will start with just the head for now -- we can change to the commented out for loop at the bottom if need be later
        position = Point(self._xpos, self._ypos)
        velocity = Point(constants.CELL_SIZE, 0)
        text = "8"
        color = self._original_color
            
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)

        """
        for i in range(constants.SNAKE_LENGTH):
            #snake created horizontally --will change this later
            position = Point(self._xpos - i * constants.CELL_SIZE, self._ypos)
            velocity = Point(constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._color
             
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
        """

    def add_sheild(self, units):
        """Adds units to the sheild attribute"""
        self._sheild += units

    def lose_sheild(self, units):
        """Removes units to the sheild attribute"""
        self._sheild -= units

    def get_sheild(self):
        return self._sheild

    def reset(self):
        #erase segments
        self._segments = []

        #reset cycle
        self._prepare_cycle()

        self._sheild = 0
