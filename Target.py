import random

from Snake import Snake

class Target:
    def __init__(self, game_board):
        self.game_board = game_board
        self.x = 3
        self.y = 4

    def check_collision(self, snake):
        for segment in snake.tails:
            if segment['current_x'] == self.x and segment['current_y'] == self.y:
                snake.extend(self.game_board)
                self.relocate(snake)

    def relocate(self, snake):
        new_x = random.randint(1, len(self.game_board)-1)
        new_y = random.randint(1, len(self.game_board[0])-1)
        self.x = new_x
        self.y = new_y
