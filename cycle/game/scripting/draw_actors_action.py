from game.scripting.action import action

class DrawActorsAction(action):

    def __init__(self, video_service):self._video_service = video_service

    def execute(self, cast, is_game_over, script):

        score1, score2 = cast.get_actors("scores")
        food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        if not is_game_over:
            cycle1.grow_trail(1)
            cycle2.grow_trail(1)
        cycle1_segments = cycle1.get_segments()
        cycle2_segments = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(cycle1_segments)
        self._video_service.draw_actors(cycle2_segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()