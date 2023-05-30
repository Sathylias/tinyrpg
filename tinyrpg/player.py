from .world import WORLD
from .constants import Color
from .utils import printformat


class Player:
    def __init__(self, location):
        self.location = WORLD.nodes.get(location)
        # self.display_location()
        # self.display_exits()

    def move(self, direction: str):
        self.location = WORLD.nodes.get(self.location.directions[direction])
        WORLD.clear_msg_counter()
        self.display_location()
        self.display_exits()

    def talk(self, npc):
        msg_counter = WORLD.msg_counter.setdefault(npc, 0)

        npc_msgs = self.location.npc[npc]["msg"]
        npc_name = self.location.npc[npc]['name']

        npc_msg = npc_msgs[WORLD.msg_counter[npc]]

        print(f"{Color.BLUE}{npc_name}{Color.ENDC}: {npc_msg}")

        WORLD.msg_counter[npc] = (msg_counter + 1) % len(npc_msgs)

    def display_exits(self):
        exits = list(self.location.directions)
        print(f"\n\nPossible exits => {exits}")

    def display_location(self):
        location_name = self.location.name
        location_desc = self.location.description
        printformat(f'\n{Color.BOLD}{Color.CYAN}{location_name}{Color.ENDC}\n{location_desc}', list(self.location.npc))


PLAYER = Player('001')
