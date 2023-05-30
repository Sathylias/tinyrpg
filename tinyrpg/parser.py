import sys
from .action import Action
from .constants import IGNORED_TERMS

class Parser:

    action = None

    @classmethod
    def execute(cls, cmd: str):
        words = Parser.sanitize_args(list(cmd.lower().strip().split(" ")))
        cls.action = words[0]
        if cls.action in Action.commands:
            Action.commands[cls.action](words[1:])
        elif cls.action == "exit":
            sys.exit(0)
        elif not cls.action:
            print("At least, give me a command..")
        else:
            print(f"I do not understand the command <{cls.action}>")

    @staticmethod
    def sanitize_args(args):
        return [word for word in args if word not in IGNORED_TERMS]
