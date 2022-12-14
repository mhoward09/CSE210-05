from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, is_game_over, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        #print(f'MoveActorsAction class actors = {actors}')
        for actor in actors:
            actor.move_next()








"""
from game.scripting.action import action
from game.scripting.Script import script

class MoveActorsAction(Action):
    
     def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

"""