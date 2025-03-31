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
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode in ["rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"] and start_pos:
                end_pos = event.pos
                if mode == "rectangle":
                    pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                elif mode == "circle":
                    radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, int(radius), 2)
                elif mode == "square":
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, (*start_pos, side, side), 2)
                elif mode == "right_triangle":
                    pygame.draw.polygon(screen, color, [start_pos, (start_pos[0], end_pos[1]), (end_pos[0], end_pos[1])], 2)
                elif mode == "equilateral_triangle":
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, color, [start_pos, (start_pos[0] + height, end_pos[1]), (start_pos[0] - height, end_pos[1])], 2)
                elif mode == "rhombus":
                    width = abs(end_pos[0] - start_pos[0]) // 2
                    height = abs(end_pos[1] - start_pos[1]) // 2
                    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1] - height), (start_pos[0] + width, start_pos[1]), (start_pos[0], start_pos[1] + height), (start_pos[0] - width, start_pos[1])], 2)
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
            elif event.key == pygame.K_5:
                mode = "square"
            elif event.key == pygame.K_6:
                mode = "right_triangle"
            elif event.key == pygame.K_7:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_8:
                mode = "rhombus"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
        
    if drawing:
        if mode == "pen":
            pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 3)
        elif mode == "eraser":
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)  # Рисует белыми точками

    pygame.display.update()
    clock.tick(60)
