from .player import PLAYER

class Game:

    @staticmethod
    def initialize():
        PLAYER.display_location()
        PLAYER.display_exits()
