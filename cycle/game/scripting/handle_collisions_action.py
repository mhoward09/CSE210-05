import constants
from game.casting.actor import actor
from game.scripting.action import action
from game.shared.point import point

class HandleCollisionsAction(action):
    
    def __init__(self):
        self._is_game_over = False

    def execute(self, cast, is_game_over, script):
        
         if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycles")
        if not self._is_game_over:
            cycle1 = cycles[0]
            cycle2 = cycles[1]
        head = cycle1.get_segments()[0]
        head2 = cycle2.get_segments()[0]
        
        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
        elif head2.get_position().equals(food.get_position()):
            points = food.get_points()
            score.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        head = cycle1.get_segments()[0]
        segments = cycle1.get_segments()[1:]

        cycle2 = cycles[1]
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
            for segment in segments2:
                if head.get_position().equals(segment.get_position()):
                    self._is_game_over = True

        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
            for segment in segments:
                if head2.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                    
    def _handle_game_over(self, cast):
        
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            cycle1 = cycles[0]
            segments = cycle1.get_segments()
            food = cast.get_first_actor("foods")

            cycle2 = cycles[1]
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            cast.add_actor("messages", message)

            for segment in segments:
                 segment.set_color(constants.WHITE)
            for segment in segments2:
                 segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)

    def get_is_game_over(self):
        return self._is_game_over