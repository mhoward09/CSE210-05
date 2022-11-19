import constants

from game.casting.cast import Cast
from game.casting.power_up import Power_up
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    #create the cast
    cast = Cast()
    cast.add_actor("power_up", Power_up())
    cast.add_actor("cycles", Cycle(constants.GREEN, 100, y))
    cast.add_actor("cycles", Cycle(constants.BLUE, 800, y))
    cast.add_actor("scores", Score(constants.GREEN, 15, 15))
    cast.add_actor("scores", Score(constants.BLUE, 160, 15))
    #print(f'these are the cast: {cast._actors}')
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    #print(f'these are the scripts {script._actions}')
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()