import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        #move up direction
        self._direction1 = Point(0, constants.CELL_SIZE)
        #move down direction
        self._direction2 = Point(0, -1 * constants.CELL_SIZE)
        self._is_game_over = False

    def execute(self, cast, is_game_over, script):

        cycles = cast.get_actors("cycles")

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)

        cycle1 = cycles[0]
        cycle1.turn_cycle(self._direction1)

        cycles = cast.get_actors("cycles")

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

        cycle2 = cycles[1]
        cycle2.turn_cycle(self._direction2)

    def set_is_game_over(self, is_game_over):
        self._is_game_over = is_game_over