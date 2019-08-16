import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (107, 54, 168)
GRAY = (25, 25, 25)
WIN_WIDTH = 500
WIN_HEIGHT = 550

# 1. Create a set of initial states with simple pattern (Ex. Blinker)
# cur_states = [0] * 400
# cur_states[10] = 1
# cur_states[30] = 1
# cur_states[50] = 1
generation = 0
is_paused = False

cur_states = [0] * 400
for i in range(len(cur_states)):
    cur_states[i] = random.randint(0, 1)

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode(size)


# Add a title
pygame.display.set_caption(
    "Conway's Game of Life, Generation: " + str(generation))

# Buttons
pause_button = pygame.draw.rect(screen, GRAY, pygame.Rect(200, 420, 100, 50))

restart_button = pygame.draw.rect(
    screen, PURPLE, pygame.Rect(140, 501, 100, 50))

speedUp_button = pygame.draw.rect(
    screen, PURPLE, pygame.Rect(260, 501, 100, 50))


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
    generation += 1
    pygame.display.set_caption(
        "Conway's Game of Life, Generation: " + str(generation))

    # PAUSE/PLAY
    if event.type == pygame.MOUSEBUTTONDOWN:

        click_pos = pygame.mouse.get_pos()
        if pause_button.collidepoint(click_pos):
            is_paused = not is_paused

    if not is_paused:
        new_states = [0] * 400

        for index in range(len(cur_states)):
            width = 20
            e = index + width
            w = index - width
            n = index - 1
            s = index + 1
            ne = n + width
            nw = n - width
            se = s + width
            sw = s - width

            live_neighbours = 0

            if e < len(cur_states) and cur_states[e] == 1:
                live_neighbours += 1
            if w > 0 and cur_states[w] == 1:
                live_neighbours += 1
            if n % width != width - 1 and cur_states[n] == 1:
                live_neighbours += 1
            if s % width != 0 and cur_states[s] == 1:
                live_neighbours += 1
            if ne < len(cur_states) and ne % width != width - 1 and cur_states[ne] == 1:
                live_neighbours += 1
            if se < len(cur_states) and se % width != 0 and cur_states[se] == 1:
                live_neighbours += 1
            if nw > 0 and nw % width != width - 1 and cur_states[nw] == 1:
                live_neighbours += 1
            if sw > 0 and sw % width != 0 and cur_states[sw] == 1:
                live_neighbours += 1

            if cur_states[index] == 1:
                if live_neighbours < 2:
                    new_states[index] = 0
                elif live_neighbours > 3:
                    new_states[index] = 0
                else:
                    new_states[index] = 1
            else:
                if live_neighbours == 3:
                    new_states[index] = 1
                else:
                    new_states[index] = 0

        cur_states = new_states

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

    # Button example
    # pause_button = pygame.draw.rect(
    #     screen, BLUE, pygame.Rect(200, 420, 100, 50))
    # font = pygame.font.Font('freesansbold.ttf', 16)
    # text = font.render('Play/Pause', True, (14, 28, 54))
    # screen.blit(text, pause_button)

    # Pause button
    pause_button = pygame.draw.rect(
        screen, PURPLE, pygame.Rect(20, 501, 100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16)
    pause_text = str('Play/Pause')
    text = font.render(pause_text, True, (175, 203, 255))
    pauseRect = text.get_rect()
    pauseRect.center = (
        pause_button.center[0], pause_button.center[1])
    screen.blit(text, pauseRect)

    # Restart button
    restart_button = pygame.draw.rect(
        screen, PURPLE, pygame.Rect(140, 501, 100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16)
    restart_text = str('Restart')
    text = font.render(restart_text, True, (175, 203, 255))
    restartRect = text.get_rect()
    restartRect.center = (
        restart_button.center[0], restart_button.center[1])
    screen.blit(text, restartRect)

    # Speed up
    speedUp_button = pygame.draw.rect(
        screen, PURPLE, pygame.Rect(260, 501, 100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16)
    speedUp_text = str('Speed Up')
    text = font.render(speedUp_text, True, (175, 203, 255))
    speedUpRect = text.get_rect()
    speedUpRect.center = (
        speedUp_button.center[0], speedUp_button.center[1])
    screen.blit(text, speedUpRect)

    # Slow down
    slowDown_button = pygame.draw.rect(
        screen, PURPLE, pygame.Rect(380, 501, 100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16)
    slowDown_text = str('Slow Down')
    text = font.render(slowDown_text, True, (175, 203, 255))
    slowDownRect = text.get_rect()
    slowDownRect.center = (
        slowDown_button.center[0], slowDown_button.center[1])
    screen.blit(text, slowDownRect)

    # Generations

    # font = pygame.font.Font('freesansbold.ttf', 16)
    # generation_display = pygame.draw.rect(
    #     screen, GRAY, pygame.Rect(5, 5, 150, 40))
    # gen_text = str(generation) + ' generations'
    # text = font.render(gen_text, True, (175, 203, 255))
    # textRect = text.get_rect()
    # textRect.center = (
    #     generation_display.center[0], generation_display.center[1])
    # screen.blit(text, textRect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
