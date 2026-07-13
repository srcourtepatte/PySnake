import pygame
from pygame.examples.music_drop_fade import starting_pos

from board import initiate_board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
game_board = initiate_board(screen)
current_x = 20
current_y = 12
player_pos = game_board[current_x][current_y]
starting_point = pygame.Vector2(player_pos)
snake = [{'current_x': current_x, 'current_y': current_y, 'last_x': 0, 'last_y': 0, 'starting_point': starting_point}]
direction = 0

MOVE_PLAYER = pygame.USEREVENT + 1
ADD_SEGMENT = pygame.USEREVENT + 2
pygame.time.set_timer(MOVE_PLAYER, 250)
pygame.time.set_timer(ADD_SEGMENT, 5000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOVE_PLAYER:
            # for segment in snake:
            for x in range(len(snake)):
                segment = snake[x]
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
                else:
                    segment['current_x'] = snake[x - 1]['last_x']
                    segment['current_y'] = snake[x - 1]['last_y']
                player_pos = game_board[segment['current_x']][segment['current_y']]
                segment['starting_point'] = pygame.Vector2(player_pos)
        elif event.type == ADD_SEGMENT:
            last_segment = snake[-1]
            player_pos = game_board[last_segment['current_x']][last_segment['current_y']]
            starting_point = pygame.Vector2(player_pos)
            snake.append({'current_x': last_segment['last_x'], 'current_y': last_segment['last_y'], 'last_x': 0, 'last_y': 0, 'starting_point': starting_point})
    screen.fill((0, 0, 0))

    for segment in snake:
        pygame.draw.circle(screen, "red", segment['starting_point'], 15)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = 1
    elif keys[pygame.K_s]:
        direction = 2
    elif keys[pygame.K_a]:
        direction = 3
    elif keys[pygame.K_d]:
        direction = 4

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
