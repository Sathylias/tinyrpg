#!/usr/bin/env python3

from tinyrpg.parser import Parser
from tinyrpg.utils import get_version
from tinyrpg.game import Game

def main():

    print(get_version())

    Game.initialize()

    # Main Game loop
    while True:
        cmd = input("=> ")
        Parser.execute(cmd)


if __name__ == "__main__":
    main()
