#!/usr/bin/env python3

from tinyrpg.parser import Parser

def main():

    while True:
    # Main Game loop
        cmd = input("=> ")
        Parser.execute(cmd)


if __name__ == "__main__":
    main()
