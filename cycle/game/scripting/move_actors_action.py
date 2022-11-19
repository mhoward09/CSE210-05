from game.scripting.action import action
from game.scripting.Script import script

class MoveActorsAction(Action):
    
     def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()