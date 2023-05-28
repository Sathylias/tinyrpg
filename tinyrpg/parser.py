from .constants import VALID_DIRECTIONS

class Action:

    commands = {}

    @classmethod
    def add(cls, keyword, func):
        cls.commands[keyword] = func

    @staticmethod
    def go(player, args):
        valid = [item for item in args if item in VALID_DIRECTIONS][0]
        if len(valid) > 0:
            player.move(valid)
        elif not args:
            print('Please specify a direction..')
        else:
            print('Alas, you cannot go there')

Action.add('go', Action.go)
Action.add('move', Action.go)

class Parser:
    def __init__(self, player):
        self.action = None
        self.player = player

    def execute(self, cmd: str):
        words = list(cmd.strip().split(' '))
        self.action = words[0]
        if self.action in Action.commands:
            Action.commands[self.action](self.player, words[1:])
        elif not self.action:
            print('At least, give me a command..')
        else:
            print(f'I do not understand the command <{self.action}>')
