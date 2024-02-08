###############################
#           Room.py          #
##############################

class Room:
    """A class representing a generic room"""

    def __init__(self, room_name, objective, item, number, portals):
        self.room_name = room_name
        self.objective = objective
        self.is_occupied = False
        self.is_discovered = False
        self.item = item
        self.portals = portals
        self.minigame = []
        self.room_number = number

        def __str__(self):
            class_name = self.__class__.__name__
            attributes = vars(self)
            formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
            return f"{class_name} {{\n{formatted_attributes}\n}}"

rooms_list = [

    Room(
        room_name="Start",
        objective="Begin your journey into the Vault of Glass",
        item="NOT REQUIRED: Jumpship",
        number=0,
        portals=["The Descent"],
    ),

    Room(
        room_name="Descent",
        objective="Descend into the Vault of Glass",
        item="Safe passage",
        number=1,
        portals=["The Confluxes", "Loser"],
    ),

    Room(
        room_name="The Confluxes",
        objective="Defend the Confluxes from Vex sacrifices",
        item="Praedyth's Revenge",
        number=2,
        portals=["The Oracles", "Gorgon's Labyrinth"],
    ),
    Room(
        room_name="The Oracles",
        objective="Destroy the Oracles",
        item="Vision of Confluence",
        number=3,
        portals=["The Confluxes", "Templar's Well"],
    ),

    Room(
        room_name="Templar's Well",
        objective="MINI BOSS: Defeat the Templar",
        item="Corrective Measure",
        number=4,
        portals=["The Oracles"],
    ),

    Room(
        room_name="Gorgon's Labyrinth",
        objective="Quietly move through the Gorgon's Labyrinth without being detected by the Gorgons",
        item="Hezen's Vengeance",
        number=5,
        portals=["The Confluxes", "The Gatekeepers", "The Vault of Glass"],
    ),

    Room(
        room_name="The Gatekeeepers",
        objective="Defend the portal plates, then defeat the Gatekeepers",
        item="Found Verdict",
        number=6,
        portals=["The Oracles", "Gorgon's Labyrinth", "The Vault of Glass"],
    ),

    Room(
        room_name="The Vault of Glass",
        objective="Defeat Atheon, Time's Conflux",
        item="NOT REQUIRED: Vex Mythoclast",
        number=7,
        portals=[],
    ),
]