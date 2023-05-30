from dataclasses import dataclass
from .utils import read_json


@dataclass
class WorldNode:
    name: str
    description: str
    directions: str
    npc: str


class World:
    def __init__(self):
        self.WORLDMAP = read_json("worldmap")["node"]
        self.nodes = self.construct_nodes()
        self.msg_counter = {}

    def construct_nodes(self):
        nodes = {}
        for key, val in self.WORLDMAP.items():
            nodes[key] = WorldNode(*val.values())
        return nodes

    def clear_msg_counter(self):
        self.msg_counter.clear()


WORLD = World()
