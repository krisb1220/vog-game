###############################
#           Globals.py       #
##############################

class Globals:
    def __init__(self):
        self.command_current = "start"
        self.command_count = 0
        self.commands = ['start']
        self.valid_commands = [
            "test",
            "colors",
            "end",
            "start",
            "ERROR"
    ]

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"

