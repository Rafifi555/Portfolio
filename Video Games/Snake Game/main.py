import pygame
import time
import random

pygame.init()

# set up the display
WIDTH = 640
HEIGHT = 480
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# set up the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# set up the snake and food
snake_pos = [[100, 100], [90, 100], [80, 100]]
snake_speed = [10, 0]
food_pos = [random.randrange(1, WIDTH//10) * 10, random.randrange(1, HEIGHT//10) * 10]
food_spawn = True

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, RED)
    DISPLAY.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def draw():
    DISPLAY.fill(WHITE)

    for pos in snake_pos:
        pygame.draw.rect(DISPLAY, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(DISPLAY, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()

# set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_UP]:
            snake_speed = [0, -10]
        if keys[pygame.K_DOWN]:
            snake_speed = [0, 10]
        if keys[pygame.K_LEFT]:
            snake_speed = [-10, 0]
        if keys[pygame.K_RIGHT]:
            snake_speed = [10, 0]

    snake_pos.insert(0, list([snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]))

    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH//10) * 10, random.randrange(1, HEIGHT//10) * 10]
    food_spawn = True

    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT) or (snake_pos[0] in snake_pos[1:]):
        game_over()

    draw()
    clock.tick(10)
