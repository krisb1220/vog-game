# import bcolors
# from room import Room
# from player import Player
# from game import Game
# from bcolors import colors
#
#
# def printc(msg, color_in):
#     """Pretty printing with colors"""
#
#     colors = bcolors.colors
#
#     print(f"{colors[color_in]}", f"{msg}", colors["g"])
#     # This section is for showing example text & it's key
#     if msg == "x":
#         for ex_color in colors:
#             print(f"{colors[ex_color]}", "EXAMPLE", "| ", ex_color, colors["g"])
#
#
# def get_colors(*args):  # add args
#     arr = []
#     for key in colors:
#         arr.append(key)
#
#     for i, color in enumerate(colors):
#         printc(f"{arr[i]}| EXAMPLE", color)
#
#     # for color in colors:
#     #     printc("EXAMPLE", color)
#     # if args:
#     #     for right in args:
#     #         if right == args[0]:
#     #             printc("EXAMPLE", arr[args[0]])

import bcolors
from room import Room
from player import Player
from game import Game
from bcolors import colors


def make_colorful(msg, color_in):

    combined = ''
    for color in color_in:
        combined += colors[color]

    return f"{combined}"+f"{msg}"+colors["g"]

def printc(msg, color_in=["c"]):
    """Pretty printing with colors"""
    colors = bcolors.colors
    encoded = make_colorful(msg, color_in)
    print(encoded)


    # This section is for showing example text & it's key


def get_colors(msg):  # add args
    arr = []
    for key in colors:
        arr.append(key)

    for i, color in enumerate(colors):
        printc(f"{arr[i]}| {msg}", color)

# print(get_colors("test"))








       # for color in color_in:
       #      formatted += make_colorful(f"{msg}", color)

#
# combined_files = [
#     "bcolors.py",
#     "game.py",
#     "globals.py",
#     "player.py",
#     "room.py",
#     "storylines.py",
#     "main.py",
# ]
#
# aggregated = ''
#
# for file in combined_files:
#     with open(file, 'r') as new_data:
#         aggregated+=new_data.read()
#
# with open("aggregated.py", 'w') as new_file:
#     new_file.write(aggregated)
#     print("Files combined", combined_files)