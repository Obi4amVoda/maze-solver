import pygame
import sys
import random
import time
# constanti
WIDTH, HEIGHT = 800, 600
W = 50
ROWS = HEIGHT // W
COLS = WIDTH // W
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
outlineThickness = 3

cells = []

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")

class Cell:
    def __init__(self, row, col, lines):
        self.row = row
        self.col = col
        self.lines = lines
    
    def draw(self):
        rect = pygame.Rect(100, 100, 200, 150)

        x = self.col * W
        y = self.row * W

        if self.lines[0]:  # top
            pygame.draw.line(SCREEN, GREEN, (x, y), (x + W, y), outlineThickness)
        if self.lines[1]:  # right
            pygame.draw.line(SCREEN, GREEN, (x + W, y), (x + W, y + W), outlineThickness)
        if self.lines[2]:  # bottom
            pygame.draw.line(SCREEN, GREEN, (x, y + W), (x + W, y + W), outlineThickness)
        if self.lines[3]:  # left
            pygame.draw.line(SCREEN, GREEN, (x, y), (x, y + W), outlineThickness)


def setUp():
    #print("")
    for i in range(ROWS):
        for j in range(COLS):
            cells.append(Cell(i, j, [True, True, True, True]))

def main():
    setUp()

    for cell in cells:
        cell.draw()
    pygame.display.flip()   
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
main()