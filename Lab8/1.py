import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Размеры машины
car_width, car_height = 50, 100

# Позиция машины
car_x, car_y = WIDTH // 2 - car_width // 2, HEIGHT - 120
car_speed = 5

# Койны
coin_radius = 15
coins = []
coin_spawn_time = 30  # Интервал появления монет
coin_counter = 0
collected_coins = 0

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение машины
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed
    
    # Спавн койноыв
    coin_counter += 1
    if coin_counter >= coin_spawn_time:
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coins.append([coin_x, 0]) 
        coin_counter = 0
    
    # Обновление положения койнов
    for coin in coins[:]:
        coin[1] += 5
        if coin[1] > HEIGHT:
            coins.remove(coin)  # Удаление койнов которые не в экране
    
    # Проверка коллизий с койнами
    for coin in coins[:]:
        if (car_x < coin[0] < car_x + car_width or car_x < coin[0] + coin_radius * 2 < car_x + car_width) and \
           (car_y < coin[1] < car_y + car_height or car_y < coin[1] + coin_radius * 2 < car_y + car_height):
            coins.remove(coin)
            collected_coins += 1
    
    # Отрисовка машины (прямоугольник вместо машины)
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    
    # Отрисовка койнов (круги вместо койнов)
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_radius)
    
    # Отображение количества собранных койнов
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Coins: {collected_coins}", True, BLACK)
    screen.blit(text, (WIDTH - 120, 20))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
