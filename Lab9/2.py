import pygame
import random
import sys
import os

# Добавляем путь к папке Lab10 в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lab10')))

# Импортируем функцию save_score из snake.py
from snake import save_score

# Инициализация pygame
pygame.init()

# Настройки экрана и игры
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20

# Функция для запуска игры
def run_game(username):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    snake = [(300, 300)]
    direction = (GRID_SIZE, 0)
    food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    food_weight = random.choice([1, 2, 3])
    food_timer = 200
    score = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
            direction = (0, -GRID_SIZE)
        if keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
            direction = (0, GRID_SIZE)
        if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
            direction = (-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
            direction = (GRID_SIZE, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
            running = False

        snake.insert(0, new_head)

        if new_head == food:
            score += food_weight
            food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
            food_weight = random.choice([1, 2, 3])
            food_timer = 200
        else:
            snake.pop()

        food_timer -= 1
        if food_timer <= 0:
            food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
            food_weight = random.choice([1, 2, 3])
            food_timer = 200

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, BLUE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(10)

    # Сохраняем рекорд после завершения игры
    save_score(username, score)
    pygame.quit()

# Спрашиваем никнейм перед началом игры
username = input("Enter your username: ")
run_game(username)
