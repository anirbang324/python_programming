import pygame
import random
pygame.init() #here we have used init to initialize pygame
red = (255,0,0)  #RGB---RED,GREEN,BLUE
white = (255,255,255)
black = (0,0,0)
#game display
screen_weidth = 800
screen_height = 600
gameWindow =pygame.display.set_mode((screen_weidth,screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()
#game specific variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def text_score(text,color,x,y):
    screen_text = font.render(text,True, color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow, color, snake_list,snake_size):
    for x,y in snake_list:
      pygame.draw.rect(gameWindow, color,[x,y,snake_size, snake_size])
#game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(20, screen_weidth)  # random modle is imported to set any number for food location depending on screen weidth
    food_y = random.randint(20, screen_height)  # /2 is used to plot the food inside the screen with better location
    score = 0  # Because the initial score is 0
    init_velocity = 4
    snake_size = 10
    fps = 90
    clock = pygame.time.Clock()  # clock is used to update the framerate
    font = pygame.font.SysFont(None, 55)
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #used for snake's movement towards right dorection
                    velocity_x = init_velocity
                    velocity_y = 0
                if event.key == pygame.K_LEFT:  # used for snake's movement towards left dorection
                    velocity_x = -init_velocity
                    velocity_y = 0
                if event.key == pygame.K_UP:  # used for snake's movement towards up dorection
                    velocity_y = -init_velocity
                    velocity_x = 0
                if event.key == pygame.K_DOWN:  # used for snake's movement towards down dorection
                    velocity_y = init_velocity
                    velocity_x = 0
        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y
        if abs(snake_x-food_x)<5 and abs(snake_y-food_y)<5 : #used to plot score
            score +=1
            food_x = random.randint(20,screen_weidth / 2)  # to update the score
            food_y = random.randint(20,screen_height / 2)  # /2 is used to plot the food inside the screen with better location
            snake_length +=5
        gameWindow.fill(white)  #it is used to set the background color as white
        text_score("Score : " + str(score * 10), red, 5, 5)
        pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if len(snake_list)>snake_length:
            del snake_list[0]
        pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        plot_snake(gameWindow, black, snake_list,snake_size)
        pygame.display.update()  #this function is used to update the display
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()