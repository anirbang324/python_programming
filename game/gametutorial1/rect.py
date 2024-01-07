import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 67, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(screen,(155,15,0), [60, 250], 40)
    #pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)
    pygame.display.flip()