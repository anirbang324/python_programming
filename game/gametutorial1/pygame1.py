import pygame as p
def setup():
    global screen  #global
    global clock
    p.init() #initialization
    screen = p.display.set_mode((600,600)) #create a screen
    clock = p.time.Clock() #create a clock
def main():
    finished = False
    pushDown = True
    X = 300
    Y = 300
    WIDTH = 50
    HEIGHT = 50
    #Continuous Loop
    while not finished:
        screen.fill((0,0,0))  #color code for black
        #managing the events queue
        for event in p.event.get():
            if event.type == p.QUIT:
                #QUITTING the game
                finished = True
            if event.type == p.KEYDOWN and event.key == p.K_DOWN: #Down Arrow
                pushDown = not pushDown
        #print(pushDown)
        #DRAWING
        if pushDown:
            color = (255, 0, 0) #RGB coding
        else:
            color = (0, 255, 0)  #green
        #rectangle = p.Rect(100, 100, 400, 400) # (x, y, width, height)
        #p.draw.rect(screen, color, rectangle)
        for i in range(4):
            #rectangle = p.Rect(X + 25*i, Y + 25*i, WIDTH, HEIGHT)
            #p.draw.rect(screen, color, rectangle)
            p.draw.circle(screen, color, (X + 25*i, Y + 25*i), 30, 5)

        p.display.flip() #redraws the display (display update)
        clock.tick(30) #frames per second/30 times per second
setup()
main()