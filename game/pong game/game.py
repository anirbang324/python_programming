import pygame
from pygame import rect
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 500

#FPs
fpsclock = pygame.time.Clock()

#fps

fpsclock = pygame.time.Clock()

#initilization of screen

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")

#font

font = pygame.font.SysFont('Andalus',30)

#game variables

margin = 50
cpu_score = 0
player_score = 0
fps = 60

#colors

bg = (50,25,60)
white = (255,255,255)
orange = (345,200,100)

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen,white,(0,margin),(screen_width,margin))

def draw_text(text, font,text_color,x,y):
    img = font.render(text,True,text_color)
    screen.blit(img,(x,y))

class paddle():
    def  __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,20,100)
        self.speed = 5
    
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top>margin: #for the up key
            self.rect.move_ip(0,-1*self.speed) #ip - inplace
        if key[pygame.K_DOWN] and self.rect.bottom<screen_height: #for the down key
            self.rect.move_ip(0,1*self.speed) #ip - inplace
    
    def draw(self):
        pygame.draw.rect(screen,white, self.rect)
    
class ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ball_rad = 10  #radius of the ball
        self.rect = Rect(self.x,self.y,self.ball_rad*2,self.ball_rad*2)
        self.speed_x = -4
        self.speed_y= 4

        def draw(self):
            pygame.draw.circle(screen, orange,(self.rect.x + self.ball_rad,self.rect.y +self.ball_rad),self.ball_rad)


        

#paddles creation
player_paddle = paddle(screen_width-40,screen_height//2)
cpu_paddle = paddle(20,screen_height//2)

#creation of pong ball
pong_ball = ball(screen_width - 60, screen_height//2 +50)

run = True
#game loop
while run:
    fpsclock.tick(fps)
    draw_board()
    draw_text('CPU: '+str(cpu_score),font,white,20,15)
    draw_text('PLAYER: '+str(player_score),font,white,screen_width-110,15)
    
    #draw paddles
    player_paddle.draw()
    cpu_paddle.draw()

    #draw the ball
    pong_ball.draw()
    
    #player paddle
    player_paddle.move()
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


