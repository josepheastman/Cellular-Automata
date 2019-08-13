import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. Create a set of initial states with simple pattern (Ex. Blinker)
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
next_states = []

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # 3. Work on rules that i) look at all neighbors, ii) save new state in next_states[]

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    x = 5
    while x < 500:
        y = 5
        while y < 500:
            # 2. Draw based on the values cur_states
            state = cur_states[cur_index]
            # 4. Draw based on values in next_states
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            cur_index += 1
            y += 25
        x += 25
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
