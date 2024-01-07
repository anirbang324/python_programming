import pygame #module
pygame.init() #intialize pygame
screen = pygame.display.set_mode((640, 480))
done = False

# load the fonts
font = pygame.font.SysFont("Times new Roman", 72)
# Render the text in new surface
text = font.render("Hello, Pygame", True, (158, 16, 16)) #RGB = 255,255,255
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            done = True
    screen.fill((255, 255, 255))
    # We will discuss blit() in the next topic
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()