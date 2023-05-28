#!/usr/bin/env python3

from tinyrpg.player import Player
from tinyrpg.parser import Parser

def main():
    player = Player("Slayne", "001")
    parser = Parser(player)

    player.display_exits()

    while True:
        cmd = input('> ')
        parser.execute(cmd)

    # player.move("north")
    # player.move("south")
    # player.move("east")


if __name__ == "__main__":
    main()
