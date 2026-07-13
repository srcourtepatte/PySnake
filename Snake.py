import pygame

class Snake:
    def __init__(self, current_x, current_y):
        self.tails = [{'current_x': current_x, 'current_y': current_y}]

    def move(self, game_board: list, direction: int):


