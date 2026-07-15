import pygame
from pygame import Surface

def initiate_board(screen):
    print(screen.get_width(), screen.get_height()) ## 1280 x 720
    square_width = screen.get_width() // 30 ## 42
    square_height = screen.get_height() // 30 ## 24
    visual_grid = [[0 for _ in range(square_height)] for _ in range(square_width) ]
    print(len(visual_grid), len(visual_grid[0]))
    square_x = 15
    square_y = 15
    for x in range(len(visual_grid)):
        for y in range(len(visual_grid[x])):
            visual_grid[x][y] = (square_y, square_x)
            square_x += 30
        square_y += 30
        square_x = 15
    return visual_grid

def set_tiles(screen: Surface):
    for y in range(0, screen.get_height(), 30):
        for x in range(0, screen.get_width(), 30):
            rect_color = (173,216,230) if ((x // 30) + (y // 30)) % 2 == 0 else (175,240,250)
            pygame.draw.rect(screen, rect_color, (x, y, 30, 30))