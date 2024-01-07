import pygame as pi
pi.init()
white = (150,0,0)
height = 1280
width = 720
window = pi.display.set_mode((height, width))
pi.display.set_caption('Image')
image = pi.image.load('abc.jpeg')
while True:
    window.fill(white)
    window.blit(image,(0,0))  #grid
    for event in pi.event.get():
        if event.type == pi.QUIT:
            pi.quit()
            quit()
        pi.display.update()