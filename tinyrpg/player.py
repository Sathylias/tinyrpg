# from .world import WORLD
# from .constants import Color
# from .utils import printformat


# class Player:
#     def __init__(self, location):
#         self.location = WORLD.nodes.get(location)
#         self.display_location()
#         self.display_exits()

#     def move(self, direction: str):
#         PLAYER.location = WORLD.nodes.get(PLAYER.location.directions[direction])
#         WORLD.clear_msg_counter()
#         self.display_location()
#         self.display_exits()

#     def talk(self, npc):
#         if not npc in WORLD.msg_counter:
#             WORLD.msg_counter[npc] = 0
#         elif WORLD.msg_counter[npc] < len(self.location.npc[npc]["msg"]) - 1:
#             WORLD.msg_counter[npc] += 1
#         else:
#             WORLD.msg_counter[npc] = 0

#         print(f"{Color.OKBLUE}{self.location.npc[npc]['name']}{Color.ENDC}: {self.location.npc[npc]['msg'][WORLD.msg_counter[npc]]}")

#         # if npc == "yourself":
#         #     print("You talked some sense into ya, felt pretty damn good..")

#     def display_exits(self):
#         print(f"\n\nPossible exits => {list(self.location.directions)}")

#     def display_location(self):
#         printformat(f'\n{Color.BOLD}{Color.OKCYAN}{self.location.name}{Color.ENDC}\n{self.location.description}')

# PLAYER = Player('001')

from .world import WORLD
from .constants import Color
from .utils import printformat


class Player:
    def __init__(self, location):
        self.location = WORLD.nodes.get(location)
        self.display_location()
        self.display_exits()

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
        printformat(f'\n{Color.BOLD}{Color.CYAN}{location_name}{Color.ENDC}\n{location_desc}')


PLAYER = Player('001')

