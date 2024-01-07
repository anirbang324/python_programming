import pygame
from pygame.locals import *

size = 500, 500

width, height = size

black = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(size)

running = True

ball = pygame.image.load("ball.jpg")

rect = ball.get_rect()

speed = [2, 2]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        rect = rect.move(speed)

    pygame.draw.rect(screen, black, rect, 1)
    screen.blit(rect)
    pygame.display.update()
pygame.quit()
