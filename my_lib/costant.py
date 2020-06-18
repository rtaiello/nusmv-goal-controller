#!/usr/bin/env python3
import platform

NUSMV_EXEC = "NuSMV"
if platform.system() == 'Darwin':
    NUSMV_EXEC = "./mac-os/" + NUSMV_EXEC
else:
    NUSMV_EXEC = "./linux/" + NUSMV_EXEC
GRID_MODEL_DIR = "./resources/goal.smv"
MODEL_OUTPUT = "./resources/main.smv"
GRID_FILE_NAME = "./resources/grid.txt"

START_POINT = 'S'
GOAL_POINT = 'G'
OBS_POINT = '#'
PASS_POINT = 'o'