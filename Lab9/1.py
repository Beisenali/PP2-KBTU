import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

player = pygame.Rect(WIDTH // 2, HEIGHT - 80, 50, 70)
enemy = pygame.Rect(random.randint(50, WIDTH - 50), -100, 50, 70)
coins = []

speed = 5
enemy_speed = 5
score = 0

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += 5
    
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(50, WIDTH - 50)
    
    if random.randint(1, 50) == 1:
        coins.append([random.randint(50, WIDTH - 50), -50, random.choice([1, 2, 3])])
    
    for coin in coins[:]:
        coin[1] += 5
        if coin[1] > HEIGHT:
            coins.remove(coin)
        if player.colliderect(pygame.Rect(coin[0], coin[1], 20, 20)):
            score += coin[2]
            coins.remove(coin)
    
    if score >= 10:
        enemy_speed = 7
    
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLACK, enemy)
    for coin in coins:
        pygame.draw.circle(screen, GOLD, (coin[0], coin[1]), 10)
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
