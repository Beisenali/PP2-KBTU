import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

dx, dy = CELL_SIZE, 0

snake = [[100, 100]]
snake_length = 1

food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]

score = 0
level = 1
speed = 10

def generate_food():
    while True:
        new_food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        if new_food not in snake:
            return new_food

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL_SIZE, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL_SIZE, 0
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL_SIZE
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL_SIZE
    
    new_head = [snake[0][0] + dx, snake[0][1] + dy]
    
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    if len(snake) > snake_length:
        snake.pop()
    
    if new_head == food:
        score += 1
        snake_length += 1
        food = generate_food()
        
        if score % 3 == 0:
            level += 1
            speed += 2
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
