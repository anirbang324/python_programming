import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 500

#FPS
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Define Font
font = pygame.font.SysFont('z003', 30) #Constantia

#Define Game Variables
margin = 50
cpu_score = 0
player_score = 0
fps = 60
winner = 0 #winner is 1 if the player scores a point, -1 if the CPU does
live_ball=False
speed_increase = 0

simulation = False

# Define Colors
bg = (50, 25, 50)
white = (255, 255, 255)
orange = (220, 80, 20)
yellow = (240, 240, 0)


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))


# PADDLE Class
class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed) #move in place
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed) #move in place

    def ai(self):
        #ai to move the paddle automatically
        #move down
        if self.rect.centery < pong_ball.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
        #move up
        if self.rect.centery > pong_ball.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)


    def draw(self, color=white):
        pygame.draw.rect(screen, color, self.rect)


#BALL Class
class ball():
    def __init__(self, x, y):
        self.reset(x,y)

    def move(self):

        #add collision detection
        #check top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check bottom screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        #check collisions with paddles
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1
        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    #SIMULATION
    def autoplay(self):
        #add collision detection
        #check top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check bottom screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        #check collisions with paddles
        if self.rect.colliderect(cpu_paddle2) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1
        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner


    def draw(self):
        pygame.draw.circle(screen, orange, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 10
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0


#Create Paddles
player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)

cpu_paddle2 = paddle(screen_width - 40, screen_height // 2)


#Create Pong Ball
pong_ball = ball(screen_width - 60, screen_height // 2 +50)

run = True

#print(pygame.font.get_fonts())

#Game Loop
while run:

    fpsClock.tick(fps)

    draw_board()
    draw_text('CPU: ' + str(cpu_score), font, orange, 20, 15)
    draw_text('PLAYER: ' + str(player_score), font, orange, screen_width - 120, 15)
    draw_text('BALL SPEED: ' + str(abs(pong_ball.speed_x)), font, orange, screen_width // 2 -100, 15)



    if simulation == False:
        #Draw Paddles
        player_paddle.draw()
        cpu_paddle.draw()
        if live_ball == True:
            speed_increase += 1
            #move ball
            winner = pong_ball.move()
            if winner == 0:
                #Move Paddle
                player_paddle.move()
                cpu_paddle.ai()
                #Draw the Ball
                pong_ball.draw()
            else:
                live_ball=False
                if winner == 1:
                    player_score += 1
                elif winner == -1:
                    cpu_score += 1

    else:
        #Draw Paddles
        cpu_paddle2.draw(yellow)
        cpu_paddle.draw(yellow)
        if live_ball == True:
            speed_increase += 1
            #move ball
            winner = pong_ball.autoplay()
            if winner == 0:
                #Move Paddle
                cpu_paddle2.ai()
                cpu_paddle.ai()
                #Draw the Ball
                pong_ball.draw()
            else:
                live_ball=False
                simulation = False


    #prompt player instructions
    if live_ball == False:
        if winner == 0:
            draw_text('CLICK ANYWHERE TO START', font, orange, 100, screen_height // 1 - 100)

            draw_text('CLICK "S" FOR SIMULATION', font, yellow, 100, screen_height // 2 - 50)
        if winner == 1:
            draw_text('YOU SCORED!', font, orange, 220, screen_height // 2 - 100)
            draw_text('CLICK ANYWHERE TO START!', font, orange, 100, screen_height // 2 - 50)
        if winner == -1:
            draw_text('CPU SCORED!', font, orange, 220, screen_height // 2 - 100)
            draw_text('CLICK ANYWHERE TO START!', font, orange, 100, screen_height // 2 - 50)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball=True
            pong_ball.reset(screen_width - 60, screen_height // 2 + 50)


        if event.type == pygame.KEYDOWN and live_ball == False:
            if event.key == pygame.K_s:
                simulation = True
                live_ball = True
                pong_ball.reset(screen_width - 60, screen_height // 2 +50)


    if speed_increase > 500:
        speed_increase = 0
        if pong_ball.speed_x < 0:
            pong_ball.speed_x -= 1
        if pong_ball.speed_x > 0:
            pong_ball.speed_x += 1
        if pong_ball.speed_y < 0:
            pong_ball.speed_y -= 1
        if pong_ball.speed_y > 0:
            pong_ball.speed_y += 1
    


    pygame.display.update()


pygame.quit()
