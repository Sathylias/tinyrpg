from dataclasses import dataclass
from .utils import read_json


@dataclass
class WorldNode:
    name: str
    description: str
    directions: str


class World:

    WORLDMAP = read_json("worldmap")["node"]

    def __init__(self):
        self.nodes = self.construct_nodes()

    def construct_nodes(self):
        nodes = {}
        for key, val in self.WORLDMAP.items():
            nodes[key] = WorldNode(*val.values())
        return nodes


WORLD = World()
