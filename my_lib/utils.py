#!/usr/bin/env python3
import os, subprocess, re

import re

from my_lib.costant import NUSMV_EXEC, MODEL_OUTPUT


def launch_nusmv():
    return str(subprocess.check_output([NUSMV_EXEC, MODEL_OUTPUT]))


def get_path(result):
    steps = re.split("-> State: \d+\.\d+ <-", result)[1:]
    if len(steps) == 0:
        return None

    last_x = int(re.search("\d+", re.search("game.x = \d+", steps[0]).group()).group())
    last_y = int(re.search("\d+", re.search("game.y = \d+", steps[0]).group()).group())
    states = [(last_x, last_y)]
    for i in range(1, len(steps)):
        x = re.findall("game.x = \d+", steps[i])
        y = re.findall("game.y = \d+", steps[i])
        if (len(x)) > 0:
            x = int(re.search("\d+", x[0]).group())
        else:
            x = last_x
        if (len(y)) > 0:
            y = int(re.search("\d+", y[0]).group())
        else:
            y = last_y
        states.append((x, y))
        last_x, last_y = x, y
    return states


def pretty_print_move(move):
    def top():
        return "↑"

    def bottom():
        return "↓"

    def left():
        return "←"

    def right():
        return "→"

    def top_right():
        return "↗"

    def top_left():
        return "↖"

    def bottom_right():
        return "↘"

    def bottom_left():
        return "↙"

    switcher = {
        "TOP": top,
        "BOTTOM": bottom,
        "LEFT": left,
        "RIGHT": right,
        "TOPRIGHT": top_right,
        "TOPLEFT": top_left,
        "BOTTOMRIGHT": bottom_right,
        "BOTTOMLEFT": bottom_left,
    }
    # Get the function from switcher dictionary
    move = move.replace(" ", "")
    func = switcher.get(move, lambda: "Invalid moove " + str(move))
    string_result = func()
    return string_result


def interpret_move(old, new, pretty_print=True):
    diff = [new[i] - old[i] for i in range(len(old))]
    move = ""
    if diff[0] == -1:
        move += "TOP "
    elif diff[0] == 1:
        move += "BOTTOM "
    if diff[1] == 1:
        move += "RIGHT"
    elif diff[1] == -1:
        move += "LEFT"
    if move == "":
        move = "NO MOVE"
    if pretty_print:
        move = pretty_print_move(move)
    return move


def interpret_path(path):
    interp = "Start point: " + str(path[0]) + "\n"
    for i in range(1, len(path)):
        interp += "Move " + str(i) + ": " + interpret_move(path[i - 1], path[i]) + "\n"
    interp += "Goal point: " + str(path[-1]) + "\n"
    return interp
