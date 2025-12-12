import os
import shutil
import random
import string
import time
import math

blue = "\x1b[38;2;0;0;255m{}\x1b[0m"
blue_bg = "\x1b[48;2;0;0;255m{}\x1b[0m"
brown = "\x1b[38;2;140;70;20m{}\x1b[0m"
brown_bg = "\x1b[48;2;140;70;20m{}\x1b[0m"
cyan = "\x1b[38;2;0;255;255m{}\x1b[0m"
dark_grey = "\x1b[38;2;64;64;64m{}\x1b[0m"
dark_grey_bg = "\x1b[48;2;64;64;64m{}\x1b[0m"
dark_green = "\x1b[38;2;0;128;0m{}\x1b[0m"
gray = "\x1b[38;2;128;128;128m{}\x1b[0m"
gray_bg = "\x1b[48;2;128;128;128m{}\x1b[0m"
green = "\x1b[38;2;0;255;0m{}\x1b[0m"
green_bg = "\x1b[48;2;0;255;0m{}\x1b[0m"
magenta = "\x1b[38;2;255;0;255m{}\x1b[0m"
magenta_bg = "\x1b[48;2;255;0;255m{}\x1b[0m"
orange = "\x1b[38;2;255;100;0m{}\x1b[0m"
red = "\x1b[38;2;255;0;0m{}\x1b[0m"
red_bg = "\x1b[48;2;255;0;0m{}\x1b[0m"
royal_blue = "\x1b[38;2;65;105;225m{}\x1b[0m"
rosa = "\x1b[38;2;194;21;139m{}\x1b[0m"
rosa_bg = "\x1b[48;2;194;21;139m{}\x1b[0m"
white = "\x1b[38;2;255;255;255m{}\x1b[0m"
white_bg = "\x1b[48;2;255;255;255m{}\x1b[0m"
yellow = "\x1b[38;2;255;255;0m{}\x1b[0m"


# example: print(purple .format("purple"))
#-----------START OF FUNCTION----------------------

def __clear_terminal__():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

#--------------END OF FUNCTION----------------
        
#-----------START OF FUNCTION----------------------
def __get_terminal_width__():
    # Get the size of the terminal
    terminal_size = shutil.get_terminal_size()

    # Get the width
    return terminal_size.columns
#--------------END OF FUNCTION-----------------´


#-----------START OF FUNCTION----------------------
def __print_ASCII_art__(text, color0 = white, color1 = white, color2 = white):
    textList = list(text)

    line0 = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""


    for i in range(len(textList)):
        match textList[i]:
            #STANDARD height = 6, width = 8v
            case "a":
                line0 += "  _|_|   "
                line1 += "_|    _| "
                line2 += "_|_|_|_| "
                line3 += "_|    _| "
                line4 += "_|    _| "
                line5 += "_|    _| "
            case "b":
                line0 += "_|_|_|    "
                line1 += "_|    _|  "
                line2 += "_|_|_|    "
                line3 += "_|    _|  "
                line4 += "_|    _|  "
                line5 += "_|_|_|    "
            case "c":
                line0 += "  _|_|_|  "
                line1 += "_|        "
                line2 += "_|        "
                line3 += "_|        "
                line4 += "_|        "
                line5 += "  _|_|_|  "
            case "d":
                line0 += "_|_|_|_|  "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|     _| "
                line4 += "_|     _| "
                line5 += "_|_|_|_|  "
            case "e":
                line0 += "_|_|_|_| "
                line1 += "_|       "
                line2 += "_|_|_|_| "
                line3 += "_|       "
                line4 += "_|       "
                line5 += "_|_|_|_| "
            case "f":
                line0 += "_|_|_|_| "
                line1 += "_|       "
                line2 += "_|_|_|_| "
                line3 += "_|       "
                line4 += "_|       "
                line5 += "_|       "
            case "g":
                line0 += "  _|_|_| "
                line1 += "_|       "
                line2 += "_|       "
                line3 += "_|  _|_| "
                line4 += "_|    _| "
                line5 += "  _|_|_| "
            case "h":
                line0 += "_|    _| "
                line1 += "_|    _| "
                line2 += "_|_|_|_| "
                line3 += "_|    _| "
                line4 += "_|    _| "
                line5 += "_|    _| "
            case "i":
                line0 += "_|_|_| "
                line1 += "  _|   "
                line2 += "  _|   "
                line3 += "  _|   "
                line4 += "  _|   "
                line5 += "_|_|_| "
            case "j":
                line0 += "  _|_|_|   "
                line1 += "    _|     "
                line2 += "    _|     "
                line3 += "    _|     "
                line4 += "_|  _|     "
                line5 += "  _|_|     "
            case "k":
                line0 += "_|    _|  "
                line1 += "_|    _|  "
                line2 += "_|_|_|    "
                line3 += "_|    _|  "
                line4 += "_|    _|  "
                line5 += "_|    _|  "
            case "l":
                line0 += "_|        "
                line1 += "_|        "
                line2 += "_|        "
                line3 += "_|        "
                line4 += "_|        "
                line5 += "_|_|_|_|  "
            case "m":
                line0 += "_|      _| "
                line1 += "_|_|  _|_| "
                line2 += "_|  _|  _| "
                line3 += "_|      _| "
                line4 += "_|      _| "
                line5 += "_|      _| "
            case "n":
                line0 += "_|      _| "
                line1 += "_|_|    _| "
                line2 += "_|  _|  _| "
                line3 += "_|   _| _| "
                line4 += "_|    _|_| "
                line5 += "_|      _| "
            case "o":
                line0 += "  _|_|_|  "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|     _| "
                line4 += "_|     _| "
                line5 += "  _|_|_|  "
            case "p":
                line0 += "_|_|_|_|  "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|_|_|_|  "
                line4 += "_|        "
                line5 += "_|        "
            case "q":
                line0 += "  _|_|_|  "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|     _| "
                line4 += "  _|_|_|  "
                line5 += "       _| "
            case "r":
                line0 += "_|_|_|_|  "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|_|_|_|  "
                line4 += "_|   _|   "
                line5 += "_|     _| "
            case "s":
                line0 += "  _|_|_|  "
                line1 += "_|     _| "
                line2 += "  _|      "
                line3 += "    _|_|  "
                line4 += "_|      _|"
                line5 += "  _|_|_|  "
            case "t":
                line0 += "_|_|_|_|_| "
                line1 += "    _|     "
                line2 += "    _|     "
                line3 += "    _|     "
                line4 += "    _|     "
                line5 += "    _|     "
            case "u":
                line0 += "_|     _| "
                line1 += "_|     _| "
                line2 += "_|     _| "
                line3 += "_|     _| "
                line4 += "_|     _| "
                line5 += "  _|_|_|  "
            case "v":
                line0 += "_|      _| "
                line1 += "_|      _| "
                line2 += "_|      _| "
                line3 += "_|      _| "
                line4 += " _|    _|  "
                line5 += "   _|_|    "
            case "w":
                line0 += "_|    _|    _| "
                line1 += "_|    _|    _| "
                line2 += "_|    _|    _| "
                line3 += "_|    _|    _| "
                line4 += " _|  _| _|  _| "
                line5 += "   _|     _|   "
            case "x":
                line0 += "_|      _|"
                line1 += " _|    _| "
                line2 += "  _|_|_|  "
                line3 += " _|    _| "
                line4 += "_|      _|"
                line5 += "_|      _|"
            case "y":
                line0 += "_|      _|"
                line1 += " _|    _| "
                line2 += "  _|_|_|  "
                line3 += "    _|    "
                line4 += "    _|    "
                line5 += "    _|    "
            case "z":
                line0 += "_|_|_|_|_| "
                line1 += "      _|_| "
                line2 += "    _|_|   "
                line3 += "   _|_|    "
                line4 += "_|_|       "
                line5 += "_|_|_|_|_| "
            case "-":
                line0 += "           "
                line1 += "           "
                line2 += "  _|_|_|_| "
                line3 += "           "
                line4 += "           "
                line5 += "           "
            case " ":
                line0 += "           "
                line1 += "           "
                line2 += "           "
                line3 += "           "
                line4 += "           "
                line5 += "           "
            case "A":
                line0 += "     /\    "
                line1 += "    /  \   "
                line2 += "   /    \  "
                line3 += "     ||    "
                line4 += "     ||    "
                line5 += "     ||    "
            case "B":
                line0 += "           "
                line1 += "< I > < I >"
                line2 += "           "
                line3 += "           "
                line4 += "           "
                line5 += "           "
            case "C":
                line0 += "   ________  "
                line1 += "  |        | "
                line2 += "__|        | "
                line3 += "| |        | "
                line4 += "|_|        | "
                line5 += "  |________| "
            case "D":
                line0 += "  ________ "
                line1 += " /_______/|"
                line2 += "| O     | |"
                line3 += "|   O   | |"
                line4 += "|_____O_|/ "
                line5 += "           "
            case "E":
                line0 += "       ___ "
                line1 += "     _/ _/ "
                line2 += "   _/ _/   "
                line3 += "  / _/     "
                line4 += " /_/       "
                line5 += "           "
    print()

    print(color0 .format(line0))
    print(color0 .format(line1))
    print(color1 .format(line2))
    print(color1 .format(line3))
    print(color2 .format(line4))
    print(color2 .format(line5))

#------------manual---------------
# Use A for arrow art
# Use B for beast art
# Use C for cup art
# Use D for dice art
# Use E for electricity art
#* Please take in consideration the width of your terminal
#--------------END OF FUNCTION-----------------
    

#--------------START OF FUNCTION---------------
def __print_stat_bar__(stat_name, value, max_value, show_value = False, separeted = False, type = "square", color = red, blocks = 10):
    percentage = value / (max_value / 100)

    print(color .format(stat_name) + " [", end="")
    for i in range(blocks):            
        if(i < percentage / (10 / (blocks / 10))):
            if(separeted == True):
                print(" ", end="")
            match type:
                case "square":
                    print(color .format("■"), end="")
                case "round":
                    print(color .format("●"), end="")
                case "heart":
                    print(color .format("❤"), end="")
                case "rectangle":
                    print(color .format("▬"), end="")
                case "rectangle-dotted":
                    print(color .format("░"), end="")
                case "rectangle-dotted-dark":
                    print(color .format("▓"), end="")
                case "dot":
                    print(color .format("."), end="")
                case "rib":
                    print(color .format("╬"), end="")
                case "long":
                    print(color .format("▬▬▬"), end="")
                case _:
                    print(color. format(type), end="")
        else: 
            print(color .format(" "), end="")
            if(separeted == True):
                print(color .format(" "), end="")
            if(type == "long"):
                print(color .format("  "), end="")
    print("]", end="")
    if(show_value == True):
        print(" ", color .format(value), end="")
        print(" /", color. format(max_value))
#--------------END OF FUNCTION-----------------    

#--------------START OF FUNCTION---------------
def __print_separator__(character = "-", color = white, length = 40):
    for i in range(length):
        print(color .format(character), end="")
    print()
#------------manual----------
#styles: single, double, single-double, dotted, crossed
#--------------END OF FUNCTION-----------------    


#---------------sub-function-------------------
def __print_menu_line__(number, text, length, number_color, options_color, type = "single", title_length = 0):
    if(type == "main"):
        for i in range((title_length * 4) + __get_terminal_width__()):
            print(" ", end="")
        print(number_color. format(number), options_color .format(text), end="")
    else:
        if(type == "square"):
            print("█  ", number_color. format(number), options_color .format(text), end="")
        else:
            print("|  ", number_color. format(number), options_color .format(text), end="")

    #We are doing this to adjust the width according to the option number
    if (len(str(number)) < 2):
        for i in range(length - len(text) + 3):
            print(" ", end="")
    elif (len(str(number)) < 3):
        for i in range(length - len(text) + 2):
            print(" ", end="")
    else:
        for i in range(length - len(text) + 1):
            print(" ", end="")
    if(type == "main"):
        print()
    else:
        if(type == "square"):
            print(" █")
        else:
            print(" |")

#--------------START OF FUNCTION---------------
def __print_option_menu__(title, options, type = "single", title_color0 = white, number_color = white, options_color = white, title_color1 = white, title_color2 = white):
    #We are doing this to determine the width of the menu
    greatest_length = len(title)

    for i in range(len(options)):
        if (len(options[i]) > greatest_length):
            greatest_length = len(options[i])

    #We are doing this to print the frame (according to the greatest length)
    if(type == "single"):
        print("-", end="")
        for i in range(9 + greatest_length):
            print("-", end="")
        print("-")
    elif(type == "square"):
        print("▄", end="")
        for i in range(9 + greatest_length):
            print("■", end="")
        print("▄")  
    elif(type == "double"):
        for i in range(10 + greatest_length):
            print("=", end="")
        print("=")

    #Title printing
    if(type == "main"):
        for i in range(__get_terminal_width__()):
            print(" ", end="")
        __print_ASCII_art__(title, title_color0, title_color1, title_color2)
    else:
        __print_menu_line__(" ", title, greatest_length, number_color, title_color0, type)

    if(type == "single"):
        print("-", end="")
        for i in range(9 + greatest_length):
            print("-", end="")
        print("-")
    elif(type == "square"):
        print("█", end="")
        for i in range(9 + greatest_length):
            print("■", end="")
        print("█")
    elif(type == "double"):
        for i in range(10 + greatest_length):
            print("=", end="")
        print("=")
    elif(type == "main"):
        print()
        print()
    
    #Option printing
    if(type == "main"):
        for i in range(len(options)):
            __print_menu_line__(i+1, options[i], greatest_length, number_color, options_color, "main", len(title))
    else:
        for i in range(len(options)):
            __print_menu_line__(i+1, options[i], greatest_length, number_color, options_color, type)

    #We are doing this to print the frame according to the greatest length
    if(type == "single"):
        print("|", end="")
        for i in range(9 + greatest_length):
            print("_", end="")
        print("|")
    elif(type == "square"):
        print("▀", end="")
        for i in range(9 + greatest_length):
            print("■", end="")
        print("▀")
    elif(type == "double"):
        for i in range(10 + greatest_length):
            print("=", end="")
        print("=")
#--------------END OF FUNCTION-----------------  
#--------------START OF FUNCTION---------------
def __print_setting_true_false__(name, value, type = "round", name_color = white, true_color = green, false_color = red):
    print(name_color .format(name), end="")
    match type:
        case "round":
            print(" (", end="")
            if(value == True):
                print(true_color .format("●--"), end="")
            else:
                print(false_color .format("--●"), end="")
            print(")")
        case "square":
            print(" [", end="")
            if(value == True):
                print(true_color .format("■--"), end="")
            else:
                print(false_color .format("--■"), end="")
            print("]")
        case "checkmark":
            print(" (", end="")
            if(value == True):
                print(true_color .format("🗸"), end="")
            else:
                print(false_color .format("x"), end="")
            print(")")
        case "text":
            print(": ", end="")
            if(value == True):
                print(true_color .format("on"), end="")
            else:
                print(false_color .format("off"), end="")
            print("")

#--------------END OF FUNCTION----------------- 
#--------------START OF FUNCTION---------------
def __get_ANSI_code__(is_background, rgb_or_hex_string):
    if(rgb_or_hex_string[0] == "#"): #if string is hex we convert it to rgb
        rgb_red = int(rgb_or_hex_string[1] + rgb_or_hex_string[2], 16)
        rgb_green = int(rgb_or_hex_string[3] + rgb_or_hex_string[4], 16)
        rgb_blue = int(rgb_or_hex_string[5] + rgb_or_hex_string[6], 16)

        if(is_background == True):
            return "\x1b[48;2;" + str(rgb_red) + ";" + str(rgb_green) + ";" + str(rgb_blue) + "m{}\x1b[0m"
        else:
            return "\x1b[38;2;" + str(rgb_red) + ";" + str(rgb_green) + ";" + str(rgb_blue) + "m{}\x1b[0m"
    else: 
        if(is_background == True):
            return "\x1b[48;2;" + rgb_or_hex_string + "m{}\x1b[0m"
        else:
            return "\x1b[38;2;" + rgb_or_hex_string + "m{}\x1b[0m"
#--------------END OF FUNCTION----------------- 
#--------------START OF FUNCTION---------------
def __print_rainbow__(text, is_horizontal = False):
    red = 255
    green = 0
    blue = 0
    for i in range(40):
        if(is_horizontal == True):
            print(__get_ANSI_code__(False, str(red) + ";" + str(green) + ";" + str(blue)) .format(text), end="")
        else:
            print(__get_ANSI_code__(False, str(red) + ";" + str(green) + ";" + str(blue)) .format(text))
        if(i < 10):
            green += 25
        elif(i < 20):
            red -= 25
        elif(i < 30):
            green -= 25
            blue += 25
        elif(i < 40):
            red += 25
    print("")
            
#--------------END OF FUNCTION----------------- 
#--------------START OF FUNCTION--------------- 
#TODO fix short speeches cutting of last word
def __print_speech__(character_name, text, char_name_color = red, text_color = white):
    line_length = 40

    #this is done to figure out the line length according to the text length
    if(len(text) < 20):
        line_length = 10
    elif(len(text) < 40):
        line_length = 20

    line_count = int(len(text) / line_length)

    #because of the int() which rounds line_count down
    if(len(text) // line_length != 0):
        line_count += 1

    print(".", end="")
    for i in range(len(character_name) + 2):
        print("-", end="")
    print(".")
    print("| ", end="")
    print(char_name_color .format(character_name), end="")
    print(" |")

    print("|", end="")

    if(len(character_name) > line_length):
        for i in range(len(character_name) + 2):
            if(i == len(character_name) + 2):
                print("|", end="")
            else:
                print("_", end="")
        print("|", end="")
    else:
        for i in range(line_length + 1):
            if(i == len(character_name) + 2):
                print("|", end="")
            else:
                print("_", end="")
    print("")
    print("|", end="")
    for i in range(line_length + 1):
        print(" ", end="")
    print("|")

    current_index = 0
    char_written_this_line = 0
    this_line_broken = False
    break_the_cycle = False

    for i in range(line_count + 1): #? I have no idea what I am doing but it works. (O - O)
        if(break_the_cycle):
            break

        char_written_this_line = 0
        this_line_broken = False

        print("| ", end="")
        for j in range(line_length):
            print(text[current_index], end="")
            char_written_this_line += 1
            if(current_index < (len(text) - 1)):
                current_index += 1
                if(text[current_index] == " "): #we are doing this to break the line, when another word probably would not fit whole
                    if(current_index / (i + 1) + 10 > line_length):
                        if(this_line_broken == False):
                            this_line_broken = True

                            for i in range(line_length - char_written_this_line):
                                print(" ", end="")
                            print("|")
                            print("|", end="")
                            for i in range(line_length + 1):
                                print(" ", end="")
                            print("|")
                            break
                elif(current_index / (i + 1) + 1 == line_length): #we are doing this to break the line if the characters would not fit
                    if(this_line_broken == False):
                            this_line_broken = True

                            for i in range(line_length - char_written_this_line):
                                print(" ", end="")
                            print("|")
                            print("|", end="")
                            for i in range(line_length + 1):
                                print(" ", end="")
                            print("|")
                            break

            else:
                for i in range(line_length - char_written_this_line):
                    print(" ", end="")
                print("|")
                break_the_cycle = True
                break

    print("|", end="")
    for i in range(line_length + 1):
        print("_", end="")
    print("|")
#--------------END OF FUNCTION----------------- 
#made by Zdenek137
#====================================================================================================================================================

# def clear_console():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')

# def display(name):
#     for i in range(1, len(name)+1):
#         print(f"{i}. {name[i-1]}")

# NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# SUITS = ["♠", "♥", "♦", "♣"]
# MAX_HAND = 21

# class Player:
#     def __init__(self, chips):
#         self.chips = chips
#         self.cards = []

#     def hand_value(self):
#         value = 0
#         aces = 0
#         for card in self.cards:
#             if card[:-1] == "A":
#                 aces += 1
#                 value += 11
#             elif card[:-1] in ["K", "Q", "J"]:
#                 value += 10
#             else:
#                 value += int(card[:-1])
#         while value > MAX_HAND and aces > 0:
#             value -= 10
#             aces -= 1
#         return value
    
# class Dealer:
#     def __init__(self):
#         self.cards = []

#     def hand_value(self):
#         value = 0
#         aces = 0
#         for card in self.cards:
#             if card[:-1] == "A":
#                 aces += 1
#                 value += 11
#             elif card[:-1] in ["K", "Q", "J"]:
#                 value += 10
#             else:
#                 value += int(card[:-1])
#         while value > MAX_HAND and aces > 0:
#             value -= 10
#             aces -= 1
#         return value

# class Menu:
#     def main_menu(self):
#             clear_console()
#             if P1.chips <= 0:
#                 print("DEFEAT (u broke lmao)")
#                 time.sleep(2)
#                 quit()
#             while True:
#                 options = ["BONUSMAXWINSCATTERGOGOGO", "ur chips", "exit"]
#                 __print_speech__("Pablo", " dobry den   me jmeno je ROBBY TROUBLE", magenta)
#                 __print_option_menu__("BLACKJACK", options, "double", __get_ANSI_code__(False, "255;0;0"), red)
#                 print()
#                 choice = input(">: ")
#                 clear_console()
#                 if choice.isdigit():
#                     choice = int(choice)
#                     if 1 <= choice <= len(options):
#                         if options[choice - 1] == "BONUSMAXWINSCATTERGOGOGO":
#                             self.bet()
#                             self.pregame()
#                             quit()
#                         elif options[choice - 1] == "ur chips":
#                             clear_console()
#                             print(f"YOU HAVE {P1.chips} CHIPS")
#                             print()
#                             time.sleep(1)
#                             input("""type 𝐞⃥⃒̸ꞆᎽ𝐫⃥⃒̸ʜƚ𝔦𝔠y҉𝔯Ĭꕷᙁi҉ᴥᴄᴥᴛᴥ to exit
#                                         >: """)
#                             clear_console()
#                         elif options[choice - 1] == "exit":
#                             print("nuking the game...") 
#                             quit()

#     def bet(self):
#         self.bet_amount = 0
#         while True:
#             clear_console()
#             print(f"YOU HAVE {P1.chips} CHIPS")
#             self.bet_amount = input("Enter your bet amount: ")
#             if self.bet_amount.isdigit():
#                 self.bet_amount = int(self.bet_amount)
#                 if 0 < self.bet_amount <= P1.chips:
#                     P1.chips -= self.bet_amount
#                     print(f"You've bet {self.bet_amount} chips.")
#                     break
#                 elif self.bet_amount > P1.chips:
#                     print("brokie")
#                     time.sleep(1)

#     def gen_card(self):
#         r_num = random.choice(NUMS)
#         r_suit = random.choice(SUITS)
#         r_card = f"{r_num}{r_suit}"
#         return r_card

#     def pregame(self):
#         Pablo.cards.append(self.gen_card())
#         P1.cards.append(self.gen_card())
#         P1.cards.append(self.gen_card())
#         self.game()

#     def player_deal(self):
#         P1.cards.append(self.gen_card())

#     def game(self):
#         while True:
#             clear_console()
#             print(f"PABLO'S HAND: {' '.join(Pablo.cards)} XX")
#             print(f"YOUR HAND: {' '.join(P1.cards)}")
#             if P1.hand_value() > MAX_HAND:
#                 print("BUSTTTTTT")
#                 time.sleep(1)
#                 self.reset()
#             choice = input("HIT? >: ")
#             if choice in ["yes", "y", "YES"]:
#                 self.player_deal()
#                 if P1.hand_value() == MAX_HAND:
#                     print("BJ!")
#                     self.final_destination()
#             elif choice in ["no", "n", "NO"]:
#                 self.final_destination()
#                 break

#     def final_destination(self):
#         while Pablo.hand_value() < 17:
#             clear_console()
#             Pablo.cards.append(self.gen_card())
#             print(f"PABLO'S HAND: {' '.join(Pablo.cards)}")
#             print(f"YOUR HAND: {' '.join(P1.cards)}")
#             input("...press smth ok plz >: ")
#         pablo_hand = Pablo.hand_value()
#         player_hand = P1.hand_value()
#         if pablo_hand > MAX_HAND:
#             print("PABLO BUSTED! YOU WIN! XDXDX")
#             P1.chips += 2 * self.bet_amount
#         elif player_hand > pablo_hand:
#             print("YOU WIN! XDXDX")
#             P1.chips += 2 * self.bet_amount
#         elif player_hand < pablo_hand:
#             print("PABLO WINS! XDXDX")
#         else:
#             print("draw")
#             P1.chips += self.bet_amount
#         self.reset()

#     def reset(self):
#         P1.cards.clear()
#         Pablo.cards.clear()
#         print()
#         input("again? :3")
#         self.main_menu()

# P1 = Player(500)
# Pablo = Dealer()


# if __name__ == "__main__":
#     menu = Menu()
#     menu.main_menu()


