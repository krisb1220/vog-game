###############################
#           MAIN FILE        #
##############################


from room import Room
from player import Player
from game import Game
from _utils import printc, make_colorful, get_colors
from room import rooms_list





rooms = rooms_list
player = Player("Kris")
game = Game(player, rooms)
print(game)
state = game.get_state()
debug=False
steps = game.story


print(steps[0].conditions)


room_keys = {
    0: rooms_list[0],
    1: rooms_list[1],
    2: rooms_list[2],
    3: rooms_list[3],
    4: rooms_list[4],
    5: rooms_list[5],
    6: rooms_list[6],
    7: rooms_list[7],
}

the_room = room_keys[state["current_step"]]

def get_step():
    if debug: print("get step)")  # debug-----------------------------------
    return state["current_step"]

def get_options(step) -> list:
    if debug: print("get ops")  # debug-----------------------------------
    return steps[step].options


def get_line(step) -> str:
    if debug: print("get ln")  # debug-----------------------------------
    return steps[step].text[0]


def get_prompt(step:int) -> str:
    if debug: print("get prompt")  # debug-----------------------------------
    return steps[step].prompt


def take_item(the_item):
    printc(f"You have taken the {the_item} from {state['current_room']}!", ["f"])



def start(current_step):
    game.set_state(["current_storyline",  steps[0]])
    game.command_current = input(get_prompt(0) + " > ")
    game.player_name = game.command_current
    game.set_state(["current_step", current_step + 1])
    printc(f"Welcome {game.player_name}", ["f"])
    print("game started")

start(0)
while state["is_running"]:

    """This is the main gameplay loop and it dispatches all actions to their respective blocks"""

    game.set_conditions([["Safe passage" in game.inventory], ["Safe passage" in game.inventory],
                         ["dagger" in game.inventory], ["dagger" in game.inventory],
                         ["dagger" in game.inventory], ["dagger" in game.inventory],
                         ["dagger" in game.inventory], ["dagger" in game.inventory]], game.rooms)

    step = game.state["current_step"] # what step the user is currently at
    room = rooms_list[step]    #the list of all rooms that exist
    game.user_input = input(make_colorful(get_prompt(step), ["h"]) + " > ") #the most recent user input
    actions = game.user_input.split(" ") #an array of every word in the user input
    context = ' '.join(actions[1:]) if len(actions) > 1 else '' #if input context, this is it (ie -> take "context")
    print(game.valid_commands)
    print("condition: ", room.conditions)



    if actions[0] in game.valid_commands and step != 0:
        "If action user chooses is a base commands like 'take', dispatch cmd "


        print(actions[0])


        if len(context) == 0 and actions[0] not in ["inv", "prog"]:
            print("You're going to have to be a little more specific")

        elif actions[0] == "inv":
            print("Your inventory:", game.inventory)

        elif actions[0] == "take":

            if context == room.item:
                game.inventory.append(room.item)
                print(f"You have taken the {context} from {state['current_room']}!")
                print("Your inventory now includes:")
                print(game.inventory)
            else:
                print("It was a valiant effort")

            for item in game.inventory:
                printc(f"-{item}", ["d"])

        elif actions[0] == "showgame":
            print(game)

        elif actions[0] == "colors":
            print(context)
            get_colors(context)

        elif actions[0] == "prog":

            prog = [f"Inventory:{game.inventory}", f"Encounter: {room.room_name}",
                    f"Current Objective: {room.objective}", f"Current Item: {room.item}"
                    ]

            print(prog)

            print(context)

        elif actions[0] == "goto":
            print(context)
            print(len(context))
            if rooms_list[int(context)].is_discovered  and len(context):
                game.set_state(["current_step", int(context)])
            else:
                print("Locked. Damn.")

# ====================================================================================================

    elif actions[0] == "next" and step != 0 and room.conditions[0] == True:
        "If not base command and the action is in the **steps** win-condition"

        rooms_list[step].is_discovered = True
        printc("You have discovered a new room!", ["d"])
        printc(f"You are now in room: {room.room_name}", ["c", "h"])
        printc(f"Room objective: {room.objective}", ["f"])
        printc(f"Room reward: {room.item}", ["f"])
        printc(get_line(step), ["c"])
        game.set_state(["current_step", step+1])

    else:
        printc("You should check your input for errors.. Then check your head idiot", ["f", "h"])
        printc(f"You are still in room: {room.room_name} (Discovered)", "c")
        printc(get_line(step), ["c"])
        game.set_state(["current_step", step])












# def run_command(runner, *args):
#     if debug: print("run()")  # debug-----------------------------------
#
#     print(game)
#     print(state)
#     data = args[0]
#
#     if len(args):
#         if debug: print("run() args[]") #debug-----------------------------------
#         data = args[0]
#
#     game.commands.insert(0, runner)
#
#     if runner == "end":
#         game.end(False)
#
#     elif runner == "start": #DO NOT CHANGE
#         if debug: print("run() start") #debug-----------------------------------
#         start(0)
#
#     elif runner == 'goto':  # takes an argument (int) and updates the room state with it
#         if debug: print("run() goto") #debug-----------------------------------
#         game.set_state(["current_room", data])
#         printc(f"You are currently located in the: {state['current_room']} encounter. Please select an action:", "f")
#
#     elif runner == 'bk':
#         if debug: print("run() bk") #debug-----------------------------------
#         process_inputs(state["current_step"], "lines") #DO NOT CHANGE
#         if debug: print("bk proc_inp") #debug-----------------------------------
#         state["move_on"] = False
#         if debug: print("move on = f") #debug-----------------------------------
#         prev_step(state["current_step"], True) #DO NOT CHANGE
#         if debug: print("prev_step(current)") #debug-----------------------------------
#         run_command("goto", room_keys[state["current_step"]].room_name)
#         if debug: print("goto(room_name)") #debug-----------------------------------
#         printc(f"You are currently located in the: {state['current_room']} encounter. Please select an action:", "f")
#
#     else:
#         reject_command()


# while not state["current_step"] == len(storylines.steps):
#
#     if debug: print("while") #debug-----------------------------------
#
#     cmds = game.commands
#     print(game, "--------------game")
#     print(state, "-------------state")
#
#     if state["win_condition"]:
#         game.end(True)
#
#     elif cmds[0] in game.valid_commands and cmds[0] != "start":
#         if debug: print("while regular command")#debug-----------------------------------
#         run_command(game.user_input)
#
#     elif state["move_on"]:
#         if debug: print("while move_on")#debug-----------------------------------
#
#         if game.user_input == "bk":
#             if debug: print("bk entered")#debug-----------------------------------
#             prev_step(state["current_step"])  # DO NOT CHANGE
#
#         if game.user_input in the_room.allowed_inputs:
#             if debug: print("room cmd")#debug-----------------------------------
#             print("room command")
#
#
#         else:
#             if debug: print("while move on and not bk and room")
#
#             print(state["current_step"],
#                   "=====================================================================================================")
#             # run_command("goto", room_keys[state["current_step"]].room_name) #doesn't do anything... maybe?
#             process_inputs(state["current_step"], "lines")  # DO NOT CHANGE
#             if debug: print("process_inputs called") #debug-----------------------------------
#             state["move_on"] = False
#             if debug: print("move_on=false") #debug-----------------------------------
#             next_step(state["current_step"])  # DO NOT CHANGE
#             if debug: print("next_step(current)") #debug-----------------------------------
# printc("Thanks for playing", "b")