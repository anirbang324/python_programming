import pygame

pygame.init()
pygame.font.init()

#Basic Colors
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

#Set up window
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Pong Game")
time = pygame.time.Clock()

#Ball
def ball(ball_x,ball_y,radius):
    pygame.draw.circle(screen,Red,(ball_x,ball_y),radius)
ball_x = int(resolution[0]/2)-2
ball_y = int(resolution[1]/2)-2
radius = 15

#Moving speed
ball_x_move = 2
ball_y_move = 4

#Player
def player(player_x,player_y,width,height):
    pygame.draw.rect(screen,White,(player_x,player_y,width,height))
player_x = 15
player_y = resolution[1]/2-25
width = 10
height = 50

#Second Player
def Splayer(Splayer_x,Splayer_y,width,height):
    pygame.draw.rect(screen,White,(Splayer_x,Splayer_y,width,height))
Splayer_x = resolution[0]-25
Splayer_y = resolution[1]/2-25

#Moving speed
player_y_change = 0
Splayer_y_change = 0

#Points
points = 0
Spoints = 0
font = pygame.font.SysFont("Courier New",15)

#Game loop
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_y_change -= 3
            if event.key == pygame.K_s:
                player_y_change += 3
            if event.key == pygame.K_UP:
                Splayer_y_change -= 3
            if event.key == pygame.K_DOWN:
                Splayer_y_change += 3
        if event.type == pygame.KEYUP:
            player_y_change = 0
            Splayer_y_change = 0

    #Background and points
    screen.fill(Black)
    textsurf = font.render("Point: "+str(points),False,(255,255,255))
    screen.blit(textsurf,(0,0))
    textsurf = font.render("Point: "+str(Spoints),False,(255,255,255))
    screen.blit(textsurf,(resolution[0]-75,0))

    #Drawing and moving the ball
    ball(ball_x,ball_y,radius)
    
        #Actual moving
    ball_y += ball_y_move
    ball_x += ball_x_move
    
        #Check for Colliding with walls
    if ball_y+15 >= resolution[1]:
        ball_y_move = ball_y_move*-1
    if ball_x+15 >= resolution[0]:
        ball_x_move = ball_x_move*-1
        points += 1
    if ball_x-15 <= 0:
        ball_x_move = ball_x_move*-1
        Spoints += 1
    if ball_y-15 <= 0:
        ball_y_move = ball_y_move*-1

    #Drawing Player and moving
    player(player_x,player_y,width,height)
        #Moving part
    player_y += player_y_change
        #Player collide
    if player_y <= 0:
        player_y_change = 0
    if player_y+50 >= resolution[1]:
        player_y_change = 0

    #Drawing second player and moving ETC...
    Splayer(Splayer_x,Splayer_y,width,height)
        #Moving
    Splayer_y += Splayer_y_change
        #Second player collide
    if Splayer_y <= 0:
        Splayer_y_change = 0
    if Splayer_y+50 >= resolution[1]:
        Splayer_y_change = 0

    #Ball colliding with player
    if (ball_x-player_x+35)**2+(ball_y-player_y)**2 <= ((radius+height)**2):
        ball_x_move = ball_x_move*-1
    if (ball_x-Splayer_x-30)**2+(ball_y-Splayer_y)**2 <= ((radius+height)**2):
        ball_x_move = ball_x_move*-1
    
    #Just to make the game working
    pygame.display.update()

    time.tick(60)

pygame.quit()
