

import pygame
import random
import math
import time
from queue import PriorityQueue

# ========== SETTINGS ==========
CELL_SIZE = 25
ROWS = 20
COLS = 20
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE
FPS = 60

# ========== COLORS ==========
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)   # Start
PURPLE = (128, 0, 128)   # Goal
BLUE = (0, 0, 255)       # Visited
YELLOW = (255, 255, 0)   # Frontier
GREEN = (0, 255, 0)      # Final Path
GRAY = (200, 200, 200)

# ========== INITIAL GRID ==========
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start = (0, 0)
goal = (ROWS-1, COLS-1)
grid[start[0]][start[1]] = 2
grid[goal[0]][goal[1]] = 3

dynamic_mode = True
algorithm_choice = "A*"        # Options: "A*" or "GBFS"
heuristic_choice = "Manhattan" # Options: "Manhattan" or "Euclidean"
density = 0.3                  # 30% obstacles

nodes_expanded = 0
path_cost = 0
exec_time = 0
