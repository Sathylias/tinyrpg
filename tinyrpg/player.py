from .world import WORLD


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = WORLD.nodes.get(location)
        self.display_location()

    def move(self, direction: str):
        if direction in self.location.directions:
            self.location = WORLD.nodes.get(self.location.directions[direction])
            self.display_location()
        else:
            print("Alas, you cannot go this way..")

    def display_exits(self):
        print(f'Possible exits => {list(self.location.directions)}')

    def display_location(self):
        print(f"{self.location.name}\n{self.location.description}\n")
