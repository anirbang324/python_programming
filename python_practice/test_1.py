import pygame
import random

pygame.init()

# Define colors
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]

# Set the size of the window
SIZE = [400, 400]

# Create the window
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Programming World of GFG")

# Create a list to store the coordinates of snowflakes
snowFall = []
for i in range(50):
	x = random.randrange(0, 400)
	y = random.randrange(0, 400)
	snowFall.append([x, y])

clock = pygame.time.Clock()
done = False

# Main game loop
while not done:
	# Check for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# Fill the screen with white color
	screen.fill(WHITE)

	# Draw snowflakes on the screen
	for i in range(len(snowFall)):
		pygame.draw.circle(screen, GREEN, snowFall[i], 2)

		# Move the snowflake down by incrementing its y-coordinate
		snowFall[i][1] += 1

		# If the snowflake reaches the bottom of the screen, reposition it to the top
		if snowFall[i][1] > 400:
			y = random.randrange(-50, -10)
			snowFall[i][1] = y

			x = random.randrange(0, 400)
			snowFall[i][0] = x

	# Update the display
	pygame.display.flip()

	# Set the frame rate to 20 frames per second
	clock.tick(20)

# Quit the game
pygame.quit()
