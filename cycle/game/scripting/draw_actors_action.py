from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, is_game_over, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        score1, score2 = cast.get_actors("scores")
        sheild = cast.get_first_actor("power_up")
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        # we are already growing tails in the cycle class so we'll just comment this out for now
        #if not is_game_over:
            #cycle1.grow_tail()
            #cycle2.grow_tail()
        cycle1_segments = cycle1.get_segments()
        cycle2_segments = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(sheild)
        self._video_service.draw_actors(cycle1_segments)
        self._video_service.draw_actors(cycle2_segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()