import pygame
from pygame.locals import *

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

pygame.init()
key_dict = {K_r:red, K_b: black, K_g: green}
print(key_dict)

pygame.quit()

