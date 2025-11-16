# Генерира се лабиринт с dfs алгоритъм - https://en.wikipedia.org/wiki/Maze_generation_algorithm (Iterative implementation (with stack))

import pygame
import sys
import random

# constanti
WIDTH, HEIGHT = 800, 600
W = 50
ROWS = HEIGHT // W
COLS = WIDTH // W
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
outlineThickness = 3

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = [True, True, True, True]  # gore, dqsno, dolu, lqvo
        self.visited = False
    
    def draw(self):
        x = self.col * W
        y = self.row * W

        if self.walls[0]:  # gore
            pygame.draw.line(SCREEN, GREEN, (x, y), (x + W, y), outlineThickness)
        if self.walls[1]:  # dqsno
            pygame.draw.line(SCREEN, GREEN, (x + W, y), (x + W, y + W), outlineThickness)
        if self.walls[2]:  # dolu
            pygame.draw.line(SCREEN, GREEN, (x, y + W), (x + W, y + W), outlineThickness)
        if self.walls[3]:  # lqvo
            pygame.draw.line(SCREEN, GREEN, (x, y), (x, y + W), outlineThickness)

# 2d list (grid)
grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]

# dfs algoritum
def getNeighbours(cell):
    neighbours = []
    row, col = cell.row, cell.col
    # gore
    if row > 0 and not grid[row-1][col].visited:
        neighbours.append(grid[row-1][col])
    # dqsno
    if col < COLS - 1 and not grid[row][col+1].visited:
        neighbours.append(grid[row][col+1])
    # dolu
    if row < ROWS - 1 and not grid[row+1][col].visited:
        neighbours.append(grid[row+1][col])
    # lqvo
    if col > 0 and not grid[row][col-1].visited:
        neighbours.append(grid[row][col-1])
    return neighbours

def removeWalls(current, nextCell):
    dx = nextCell.col - current.col
    dy = nextCell.row - current.row
    if dx == 1: # sledvashtoto e nadqsno
        current.walls[1] = False
        nextCell.walls[3] = False
    elif dx == -1: # sledvashtoto e nalqvo
        current.walls[3] = False
        nextCell.walls[1] = False
    if dy == 1: # sledvashtoto e nadolu
        current.walls[2] = False
        nextCell.walls[0] = False
    elif dy == -1: # sledvashtoto e nagore
        current.walls[0] = False
        nextCell.walls[2] = False

def generateMaze():
    stack = []
    current = grid[0][0]
    current.visited = True
    stack.append(current)

    while stack:
        current = stack.pop()
        neighbours = getNeighbours(current)
        if neighbours:
            stack.append(current)
            nextCell = random.choice(neighbours)
            removeWalls(current, nextCell)
            nextCell.visited = True
            stack.append(nextCell)

def setEntranceAndExit():
    grid[0][0].walls[3] = False #vhod
    grid[ROWS-1][COLS-1].walls[1] = False #izhod

def main():
    generateMaze()
    setEntranceAndExit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        SCREEN.fill(BLACK)
        for row in grid:
            for cell in row:
                cell.draw()
        pygame.display.flip()   
    
main()
