import pygame
import math
import random
import time

WIDTH = 1200
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
arr = []

pygame.display.set_caption("Quicksort visualizer")

RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
PURPLE = (128, 0 ,128)
ORANGE =  (255, 165, 0)
GREY = (128, 128, 128)
TURK = (64, 224, 208)

class Sort:
    def __init__(self, xPos, randY, width):
        self.x = xPos
        self.y = WIDTH - randY
        self.width = width
        self.color = (0, 0, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.color,(self.x+0.005, WIDTH-self.y, self.width-0.01, WIDTH))


def swap_columns(grid, start, end):

    for loc1 in grid[start]:
        for loc2 in grid[end]:
            temp = loc1.y
            loc1.y = loc2.y
            loc2.y = temp

def make_random_columns(columns, width, colWidth):
    grid = []
    for i in range(columns):
        grid.append([])
        rand = random.randint(0, HEIGHT)
        yAxis = HEIGHT-rand
        col = Sort(i*colWidth,yAxis,colWidth)
        grid[i].append(col)
        arr.append(rand)
    return grid

def draw_columns(win,grid):
    win.fill(WHITE)
    for spot in grid:
        spot[0].draw(win)

    pygame.display.update()


def draw(win,grid):
    draw_columns(win,grid)


def quickSort(grid, arr, start, end):
    if start < end:
        partitionIndex = partition(grid, arr, start, end)
        quickSort(grid, arr, start, partitionIndex-1)
        quickSort(grid, arr, partitionIndex+1, end)

def partition(grid, arr, start, end):
    pivot = arr[end]
    i = (start-1)
    for j in range(start, end):
        if arr[j] < pivot:
            #time.sleep(0.0005)
            i = i+1

            tempSwap = arr[i]
            arr[i] = arr[j]
            arr[j] = tempSwap
            swap_columns(grid, i, j)
            #time.sleep(0.01)
            draw(WIN,grid)

    tempSwap = arr[i+1]
    arr[i+1] = arr[end]
    arr[end] = tempSwap
    swap_columns(grid, i+1, end)
    #time.sleep(0.01)
    draw(WIN,grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    return i+1


def main(win, num, colWidth):
    tempArr =[]
    grid2 = make_random_columns(num, HEIGHT, colWidth)
    run = True
    quickSort(grid2, arr, 0, len(arr) -1)
    while run:
        draw(win, grid2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

num = 400
colWidth = WIDTH / num

main(WIN, num, colWidth)
print(num)
print(colWidth)
