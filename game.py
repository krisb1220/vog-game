###############################
#           Game.py           #
##############################

# from storylines import stories

class Storyline:
    def __init__(self, params, game):
        self.text = params["text"],
        self.prompt = params["prompt"]
        self.options = params["options"]
        self.step = params["step"]
        self.game = game
        self.conditions = params["conditions"]

    def pass_game(self, game):
        self.game = game

    def print_game(self):
        print(self.game.inventory)

    def set_condition(self, new):
        self.conditions = [new]

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"

class Game:
    """A class representing a generic room"""

    def __init__(self, player, rooms):

        self.stories = [
            {
                "text": """
                    Ghost: Eyes up, Guardian! You 0don't want to be late on your first day
                    with you0r new fireteam. What should I tell them to call you
                    """,
                "prompt": "What is your name?",
                "options": ["start"],
                "conditions": [],
                "step": 1,
            },

            {
                "text": """
                You have reached step 2
                """,
                "prompt": "what door would you like to take? 1",
                "options": ["left", "right"],
                "conditions": [],
                "step": 2,
            },
            {
                "text": """
                You have reached step 3
                """,
                "prompt": "what do2or would you like to take? 2",
                "options": ["left", "right"],
                "conditions": [],
                "step": 3,
            },
            {
                "text": """
                You have reached step 4
                """,
                "prompt": "what 3door would you like to take?3 ",
                "options": ["left", "right"],
                "conditions": [],
                "step": 4,
            },
            {
                "text": """
                You have reached step 5
                """,
                "prompt": "4what door would you like to take?4",
                "options": ["left", "right"],
                "conditions": [],
                "step": 5,
            },
            {
                "text": """
                You have reached step 6
                """,
                "prompt": "5what door would you like to take?5",
                "options": ["left", "right"],
                "conditions": [],
                "step": 6,
            }
        ]

        self.state = {
            "is_running": True,
            "win_condition": False,
            "current_room": 'Start',
            "current_step": 0,
            "move_on": False,
            "current_storyline": None
        }

        self.story = [Storyline(params, self) for params in self.stories]
        self.player_name = "Guardian"
        self.current_prompt = 'Press any keys to start..............'
        self.rooms = rooms
        self.player = player
        self.user_input = "start"
        self.command_count = 0
        self.step_cleared: False
        self.commands = ['start']
        self.valid_commands = [
            "goto",
            "take",
            "back",
            "showgame",
            "colors",
            "prog",
            "move"
        ]
        self.inventory = []

    def check_step_win(self, condition):
        if condition:
            self.step_cleared = True
    def set_state(self, new):
        self.state[new[0]] = new[1]

    def get_state(self):
        return self.state

    def do_side_effect(self, action):
        return self.state

    def start(self):
        self.state["isRunning"] = True

    def end(self, result):
        self.state["win_condition"] = result
        self.state["isRunning"] = False

    def change_room(self, new_room):
        self.set_state(["current_room", new_room])

    def set_conditions(self, q, target):
        questions = q

        for i, room in enumerate(target):
            room.conditions = questions[i]

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"







#
#
# class Storyline:
#     def __init__(self, text, prompt, options, conditions, step: int):
#         self.text = text,
#         self.prompt = prompt
#         self.options = options
#         self.step = step
#         self.conditions = []
#         self.game = {}
#
#         if not isinstance(self.text, tuple):
#             raise TypeError("Storyline.text must be of type int")
#
#         if not isinstance(self.prompt, str):
#             raise TypeError("Storyline.prompt must be of type int")
#
#         if not isinstance(self.options, list):
#             raise TypeError("Storyline.options must be of type list")
#
#         if not isinstance(self.step, int):
#             raise TypeError("Storyline.step must be of type int")
#
#         if not isinstance(self.conditions, list):
#             raise TypeError("Storyline.conditions must be of type int")
#
#     def pass_game(self, game):
#         self.game = game
#
#     def __str__(self):
#         class_name = self.__class__.__name__
#         attributes = vars(self)
#         formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
#         return f"{class_name} {{\n{formatted_attributes}\n}}"
#
#
#
# story = [
#     {
#         text:"""Ghost: Eyes up, Guardian! You 0don't want to be late on your first day with you0r new fireteam. What should I tell them to call you""",
#         prompt: "What is your name?",
#         options: ["start"],
#         conditions: [("penis" in game.inventory)],
#         step: 0,
#     },
#
#     Storyline(
#         text="""
#         You have reached step 2
#         """,
#         prompt="what door would you like to take? 1",
#         options=["left", "right"],
#         conditions=[],
#         step=1,
#     ),
#     Storyline(
#         text="""
#         You have reached step 3
#         """,
#         prompt="what do2or would you like to take? 2",
#         options=["left", "right"],
#         conditions=[],
#         step=2,
#     ),
#     Storyline(
#         text="""
#         You have reached step 4
#         """,
#         prompt="what 3door would you like to take?3 ",
#         options=["left", "right"],
#         conditions=[],
#         step=3,
#     ),
#     Storyline(
#         text="""
#         You have reached step 5
#         """,
#         prompt="4what door would you like to take?4",
#         options=["left", "right"],
#         conditions=[],
#         step=4,
#     ),
#     Storyline(
#         text="""
#         You have reached step 6
#         """,
#         prompt="5what door would you like to take?5",
#         options=["left", "right"],
#         conditions=[],
#         step=5,
#     ),
#     Storyline(
#         text="""
#         You have reached step 7
#         """,
#         prompt="6what door would you like to take?",
#         options=["left", "right"],
#         conditions=[],
#         step=6,
#     ),
#     Storyline(
#         text="""
#         You have reached step 8
#         """,
#         prompt="7what do7or would you like to take?",
#         options=["left", "right"],
#         conditions=[],
#         step=7,
#     ),
#     Storyline(
#         text="""
#         You have reached step 9
#         """,
#         prompt="8what door would you like to take?",
#         options=["left", "right"],
#         conditions=[],
#         step=8,
#     ),
#     Storyline(
#         text="""
#         You have reached step 10
#         """,
#         prompt="what door 9would you like to take?",
#         options=["left", "right"],
#         conditions=[],
#         step=9,
#     ),
#
# ]
#
