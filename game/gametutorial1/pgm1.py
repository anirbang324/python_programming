import pygame
x=pygame.init() #here we have used to initialize pygame
#Game window creation
gameWindow = pygame.display.set_mode((1200,500))  #here 1200 and 500 is the weidth and size of the window
pygame.display.set_caption("This is the title")  #set_caption method is used to add a title
#Game specific variables
exit_game = False #to close a game this variable is used
game_over = False #game_over is used when there is game over

#Creating a game loop that controls the events
while not exit_game: #untill the exit_game is false this while loop will be executing
    for event in pygame.event.get(): #pygame.event.get provides all the events which is occuring in a game
            if event.type==pygame.QUIT: #QUIT is used to stop the for loop execution and quit the game
                exit_game = True
            if event.type == pygame.KEYDOWN:  #KEYDOWN function is used to control game events using different keys
                if event.key == pygame.K_RIGHT: #K_Right is used to check if the pressed key is RIGHT_ARROW key
                    print("You have pressed right arrow key")
                if event.key == pygame.K_LEFT:
                    print("You have pressed right arrow key")


pygame.quit()
quit()