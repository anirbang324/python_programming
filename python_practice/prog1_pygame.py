import pygame
pygame.init()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

background =GRAY
screen = pygame.display.set_mode((500,500))
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            if event.key == pygame.K_g:
                background = GREEN
        screen.fill(background)
        pygame.display.update()
pygame.quit()