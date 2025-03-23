import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)
clock = pygame.time.Clock()

drawing = False
mode = "pen"
color = BLACK
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if mode == "eraser":
                color = WHITE
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode in ["rectangle", "circle"] and start_pos:
                end_pos = event.pos
                if mode == "rectangle":
                    pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                elif mode == "circle":
                    radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, int(radius), 2)
            start_pos = None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "pen"
            elif event.key == pygame.K_2:
                mode = "rectangle"
            elif event.key == pygame.K_3:
                mode = "circle"
            elif event.key == pygame.K_4:
                mode = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
        
    if drawing and mode == "pen":
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 3)
    
    pygame.display.update()
    clock.tick(60)
