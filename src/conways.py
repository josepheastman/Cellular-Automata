import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (107, 54, 168)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. Create a set of initial states with simple pattern (Ex. Blinker)
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
next_states = []
is_paused = False

# cur_states = [0] * 400
# for i in range(len(cur_states)):
#     cur_states[i] = random.randint(0, 1)

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)


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

    # Add a title
    pygame.display.set_caption("Conway's Game of Life")

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        is_paused = not is_paused

        # --- Game logic should go here
        # width = 20
        # e = index + 1
        # w = index - 1
        # n = index - width
        # s = index + width
        # ne = n + 1
        # nw = n - 1
        # se = s + 1
        # sw = s - 1

        # live_neighbors = 0
        # if cur_states[e] == 1:
        #     live_neighbors += 1
        # if cur_states[w] == 1:
        #     live_neighbors += 1
        # if cur_states[n] == 1:
        #     live_neighbors += 1
        # if cur_states[s] == 1:
        #     live_neighbors += 1
        # 3. Work on rules that i) look at all neighbors, ii) save new state in next_states[]

        # --- Screen-clearing code goes here

        # Here, we clear the screen to gray. Don't put other drawing commands
        # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    cur_index = 0
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
                pygame.draw.rect(screen, PURPLE, pygame.Rect(x, y, 20, 20))
            cur_index += 1
            y += 25
        x += 25

    pause_button = pygame.draw.rect(
        screen, BLUE, pygame.Rect(200, 420, 100, 50))
    font = pygame.font.SysFont('Arial', 25)
    text = font.render('Play/Pause', True, (14, 28, 54))
    screen.blit(text, pause_button)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
