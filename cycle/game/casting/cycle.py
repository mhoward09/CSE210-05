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
    def __init__(self, color):
        super().__init__()
        self._color = color
        self._segments = []
        self._prepare_cycle()
        self._speed = 1

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_cycle(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_cycle(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        cycle = Actor()
        cycle.set_position(Point(x,y))
        cycle.set_velocity(Point(1 * constants.CELL_SIZE, 0))
        cycle.set_text("8")
        cycle.set_color(self.color)
        self._segments.append(cycle)

    def get_speed(self):
        return self._speed
        
    def update_velocity(self):
        speed = self._speed + 1
        self.set_velocity(Point(speed * constants.CELL_SIZE, 0))