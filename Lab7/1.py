import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

clock_face = pygame.image.load("mickeyclock.jpeg")
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

def draw_hand(angle, length, width, color):
    end_x = CENTER[0] + length * math.cos(math.radians(angle - 90))
    end_y = CENTER[1] + length * math.sin(math.radians(angle - 90))
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = time.localtime()
    minute_angle = (t.tm_min % 60) * 6
    second_angle = (t.tm_sec % 60) * 6
    
    screen.blit(clock_face, (0, 0))
    draw_hand(minute_angle, 120, 8, (0, 0, 255))
    draw_hand(second_angle, 140, 4, (255, 0, 0))
    
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
