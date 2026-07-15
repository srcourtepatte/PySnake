import pygame

from board import initiate_board, set_tiles
from Snake import Snake
from Target import Target

pygame.init()
screen = pygame.display.set_mode((30*8, 30*9))
tile_surface = pygame.Surface((screen.get_width(), screen.get_height()))
clock = pygame.time.Clock()

dt = 0
game_board = initiate_board(screen)
player_pos = game_board[4][4]
starting_point = pygame.Vector2(player_pos)
snake = Snake(4, 4, starting_point)
target = Target(game_board)
direction = 0

MOVE_PLAYER = pygame.USEREVENT + 1
ADD_SEGMENT = pygame.USEREVENT + 2
GAME_OVER = pygame.USEREVENT + 3
pygame.time.set_timer(MOVE_PLAYER, 250)
pygame.time.set_timer(ADD_SEGMENT, 5000)

running = True
paused = False
ended = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        elif event.type == MOVE_PLAYER:
            if not paused and not ended:
                success = snake.move(game_board, direction)
                if success == "GAME OVER":
                    pygame.event.post(pygame.event.Event(GAME_OVER))
                    break
                target.check_collision(snake)

        elif event.type == GAME_OVER:
            print("GAME OVER")
            running = False
        screen.fill((0, 0, 0))

    if not paused and not ended:
        set_tiles(tile_surface)
        screen.blit(tile_surface, (0,0))

        for segment in snake.tails:
            pygame.draw.circle(screen, "green", segment['starting_point'], 15)
        target_start = pygame.Vector2(game_board[target.x][target.y])
        pygame.draw.circle(screen, "yellow", target_start, 15)

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
