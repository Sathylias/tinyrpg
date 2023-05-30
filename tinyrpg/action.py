from .player import PLAYER
from .constants import VALID_DIRECTIONS


class Action:
    commands = {}

    @classmethod
    def add(cls, func, *keywords):
        cls.commands.update({key: func for key in keywords})

    @staticmethod
    def go(args):
        args = [word for word in args if word in VALID_DIRECTIONS][0]
        if not args:
            print("Please specify a direction..")
        elif args in list(PLAYER.location.directions):
            PLAYER.move(args)
        else:
            print("Alas, you cannot go this way..")

    @staticmethod
    def talk(args):
        if not args:
            print(f'Please specify a person to talk to..\nNPC Available are: {list(PLAYER.location.npc)}')
        elif args[0] in list(PLAYER.location.npc):
            PLAYER.talk(args[0])
        else:
            print(f"There's no {args[0]} here..")

    @staticmethod
    def show(args):
        if args[0] in ['command', 'commands', 'action']:
            print(f'Available commands: {list(Action.commands)}')

Action.add(Action.go, 'go', 'move')
Action.add(Action.talk, 'talk', 'speak')
Action.add(Action.show, 'show',)