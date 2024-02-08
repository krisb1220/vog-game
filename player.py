###############################
#           Player.py        #
##############################


class Player:
    """A class representing a generic room"""

    def __init__(self, name):
        self._name = name
        # self._position = []
        self._inventory = []
        self.current_room = 0
        # self._count = 0

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"


