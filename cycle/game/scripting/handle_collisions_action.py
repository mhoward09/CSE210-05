import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, is_game_over, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_shield_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_shield_collision(self, cast):
        
        shield = cast.get_first_actor("power_up")
        cycles = cast.get_actors("cycles")
        if not self._is_game_over:
            cycle1 = cycles[0]
            cycle2 = cycles[1]
        head = cycle1.get_segments()[0]
        head2 = cycle2.get_segments()[0]

        if head.get_position().equals(shield.get_position()):
            points = shield.get_units()
            cycle1.add_sheild(points)
            shield.reset()
        elif head2.get_position().equals(shield.get_position()):
            points = shield.get_units()
            cycle2.add_sheild(points)
            shield.reset()
    
    def _handle_segment_collision(self, cast):
        
        cycles = cast.get_actors("cycles")
        scores = cast.get_actors("scores")

        cycle1 = cycles[0]
        trail = cycle1.get_segments()
        head = trail[0]
        segments = trail[1:]
        shield1 = cycle1.get_sheild()
        score1 = scores[0]

        cycle2 = cycles[1]
        trail2 = cycle2.get_segments()
        head2 = trail2[0]
        segments2 = trail2[1:]
        shield2 = cycle2.get_sheild()
        score2 = scores[1]
        
        for segment in segments:
            #cycle 1 collides with it's own trail
            if head.get_position().equals(segment.get_position()):
                if shield1 < 1:
                    score2.add_points(1)
                    self._is_game_over = True
                else:
                    cycle1.lose_sheild(1)
        
        for segment in trail2:
            #cycle 1 collides with cycle 2 trail
            if head.get_position().equals(segment.get_position()):
                if shield1 < 1:
                    score2.add_points(1)
                    self._is_game_over = True
                else:
                    cycle1.lose_sheild(1)

        for segment in segments2:
            #cycle 2 collides with it's own trail
            if head2.get_position().equals(segment.get_position()):
                if shield2 < 1:
                    score1.add_points(1)
                    self._is_game_over = True
                else:
                    cycle2.lose_sheild(1)

        for segment in trail:
            #cycle 2 collides with cycle 1 trail
            if head2.get_position().equals(segment.get_position()):
                if shield2 < 1:
                    score1.add_points(1)
                    self._is_game_over = True
                else:
                    cycle2.lose_sheild(1)
                    
    def _handle_game_over(self, cast):
        
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            cycle1 = cycles[0]
            cycle2 = cycles[1]

            cycle1.get_segments()[0]._color = constants.WHITE
            cycle2.get_segments()[0]._color = constants.WHITE
            #cycle1.reset()
            #cycle2.reset()

            #self._is_game_over = False
            message = Actor()
            message.set_position(Point(int(constants.MAX_X/2), int(constants.MAX_Y/2)))
            message.set_text('Game over! Play Again?  Y/N')
            message.set_font_size(constants.FONT_SIZE)
            message.set_color(constants.WHITE)
            cast.add_actor("messages", message)

    def reset_game(self, cast, direction1, direction2):
        self._is_game_over = False

        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]

        cycle1.reset()
        cycle1.turn_cycle(direction1)
        cycle2.reset()
        cycle2.turn_cycle(direction2)

        cast.remove_actor("messages", cast.get_first_actor("messages"))

    def get_is_game_over(self):
        return self._is_game_over

