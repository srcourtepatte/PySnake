import pygame

class Snake:
    def __init__(self, current_x, current_y, starting_point):
        initial_segment = {"current_x": current_x, "current_y": current_y, "starting_point": starting_point, "last_x": 0, "last_y": 0}
        self.tails = [initial_segment]

    def move(self, game_board: list, direction: int):
        for x in range(len(self.tails)):
            segment = self.tails[x]
            segment['last_y'] = segment['current_y']
            segment['last_x'] = segment['current_x']
            if x == 0:
                if direction == 1:
                    segment['current_y'] -= 1
                elif direction == 2:
                    segment['current_y'] += 1
                elif direction == 3:
                    segment['current_x'] -= 1
                elif direction == 4:
                    segment['current_x'] += 1
                print("segment.y: ", segment['current_y'], " segment.x: ", segment['current_x'], " ", len(game_board[0]), " ", len(game_board))
                if segment['current_y'] < 0 or segment['current_y'] > len(game_board[0]) - 1 or segment['current_x'] < 0 or segment['current_x'] > len(game_board) - 1:
                    print("GAME OVER IN move")
                    return "GAME OVER"
            else:
                if segment['current_y'] == self.tails[0]['current_y'] and segment['current_x'] == self.tails[0]['current_x']:
                    print("GAME OVER IN MOVE")
                    return "GAME OVER"
                segment['current_x'] = self.tails[x - 1]['last_x']
                segment['current_y'] = self.tails[x - 1]['last_y']
            player_pos = game_board[segment['current_x']][segment['current_y']]
            segment['starting_point'] = pygame.Vector2(player_pos)

    def extend(self, game_board):
        last_segment = self.tails[-1]
        player_pos = game_board[last_segment['current_x']][last_segment['current_y']]
        starting_point = pygame.Vector2(player_pos)
        self.tails.append({'current_x': last_segment['last_x'], 'current_y': last_segment['last_y'], 'last_x': 0, 'last_y': 0, 'starting_point': starting_point})


