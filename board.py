import math


def initiate_board(screen):
    print(screen.get_width(), screen.get_height()) ## 1280 x 720
    square_width = screen.get_width() // 30 ## 42
    square_height = screen.get_height() // 30 ## 24
    visual_grid = [[0 for _ in range(square_height)] for _ in range(square_width) ]
    print(len(visual_grid), len(visual_grid[0]))
    square_x = square_width
    square_y = square_height
    for x in range(len(visual_grid)):
        for y in range(len(visual_grid[x])):
            visual_grid[x][y] = (square_y, square_x)
            square_x += 30
        square_y += 30
        square_x = square_width
    return visual_grid

