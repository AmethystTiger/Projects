import pygame
import random
import shelve

pygame.init()

# Window screen
screen = pygame.display.set_mode((500, 650))
pygame.display.set_caption("F!@ppy_B1r\)")
icon = pygame.image.load('Images/icon.ico')
pygame.display.set_icon(icon)

# Bird
birdImg = [pygame.image.load('Images/birdu.png'), pygame.image.load('Images/birdm.png'),
           pygame.image.load('Images/birdd.png')]
birdX = 51
birdY = 309
birdY_change = 1
def bird(img, x, y):
    screen.blit(img, (x, y))

# Pipes
pipeImg = [pygame.image.load('Images/pipeu.png'), pygame.image.load('Images/piped.png')]
pipe1X = -40
pipe1Y = random.randint(-280, -80)
pipe2X = 250
pipe2Y = random.randint(-280, -80)
def pipes(x1, y1, x2, y2):
    screen.blit(pipeImg[0], (x1, y1))
    screen.blit(pipeImg[1], (x1, y1 + 500))
    screen.blit(pipeImg[0], (x2, y2))
    screen.blit(pipeImg[1], (x2, y2 + 500))

# Floor
floorImg = pygame.image.load('Images/floor.png')
floorX = 0
floorY = 570
floorX_change = 1
def floor(x, y):
    screen.blit(floorImg, (x, y))

# High score
high_score_value = shelve.open('highscore')
h_font = pygame.font.Font('Fluo Gums.ttf', 10)
h_textX, h_textY = 247, 40
def high_score_display(x, y):
    score = h_font.render(str(high_score_value['hs']), True, (100, 100, 100))
    screen.blit(score, (x, y))

# Score
score_value = 0
font = pygame.font.Font('Fluo Gums.ttf', 15)
textX, textY = 245, 0
def score_display(x, y):
    score = font.render(str(score_value), True, (100, 100, 100))
    screen.blit(score, (x, y))

# Collision
def is_collision(player_x, player_y, pipe_x, pipe_y):
    top_pipe_Y = (pipe_y + 500)
    for i in range(pipe_y + 400):
        if player_x+42 == pipe_x and int(player_y) == i:
            end_screen()
    for i in range(top_pipe_Y, 600):
        if player_x+42 == pipe_x and int(player_y) == i:
            end_screen()

# Bird Flap
vel = 2
mass = 6
def gravity():
    global birdY, birdX, mass, vel, birdY_change, pipe1X, pipe2X, pipe1Y, pipe2Y, floorX, floorX_change, score_value
    run2 = True
    while run2:
        screen.fill((255, 230, 230))
        F = 0.5 * mass * vel ** 2
        birdY -= F
        floorX -= floorX_change
        pipe1X -= 3
        pipe2X -= 3
        vel -= 0.1
        if vel < 0:
            mass = -6
            bird(birdImg[1], birdX, birdY)
        if vel <= -1:
            mass = 6
            vel = 2
            birdY_change = 2
            run2 = False

        # Adding to the final score
        if birdX == pipe1X or birdX == pipe2X:
            score_value += 1

        # Setting border
        if birdY >= 570:
            end_screen()
        if birdY <= 0:
            birdY = 0
        if floorX < -52:
            floorX = 0
        if pipe1X <= -40:
            pipe1X = 600
            pipe1Y = random.randint(-280, -80)
        if pipe2X <= -40:
            pipe2X = 600
            pipe2Y = random.randint(-280, -80)

        is_collision(birdX, birdY, pipe1X, pipe1Y)
        is_collision(birdX, birdY, pipe2X, pipe2Y)
        floor(floorX, floorY)
        pipes(pipe1X, pipe1Y, pipe2X, pipe2Y)
        bird(birdImg[0], birdX, birdY)
        high_score_display(h_textX, h_textY)
        score_display(textX, textY)
        pygame.time.delay(10)
        pygame.display.update()

# Main menu
def main_menu():
    main_run = True
    while main_run:
        screen.fill((255, 230, 230))
        font1 = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        main_text = font1.render("Main Menu", True, (100, 100, 100))
        main_play_text = font2.render("Press SPACE To Play", True, (100, 100, 100))
        main_play_text2 = font2.render("(Ignore the first pipe :)", True, (100, 100, 100))
        screen.blit(main_text, (150, 100))
        screen.blit(main_play_text, (155, 200))
        screen.blit(main_play_text2, (150, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_run = False
                if event.key == pygame.K_SPACE:
                    is_run()
        pygame.display.update()

# Running the game
def is_run():
    global birdY, birdX, birdY_change, pipe1X, pipe2X, pipe1Y, pipe2Y, floorX, floorX_change, score_value
    run = True
    jump = True
    while run:
        screen.fill((255, 230, 230))
        birdY += birdY_change
        floorX -= floorX_change
        pipe1X -= 3
        pipe2X -= 3
        birdY_change += 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True

        # Adding to the final score
        if birdX == pipe1X or birdX == pipe2X:
            score_value += 1


        # Bird Flap
        if jump:
            gravity()
            jump = False

        # Setting border
        if birdY >= 570:
            end_screen()
        if birdY <= 0:
            birdY = 0

        if floorX < -52:
            floorX = 0

        # Re-Calling pipes
        if pipe1X <= -40:
            pipe1X = 600
            pipe1Y = random.randint(-280, -80)
        if pipe2X <= -40:
            pipe2X = 600
            pipe2Y = random.randint(-280, -80)

        # Checking if bird is ded
        is_collision(birdX, birdY, pipe1X, pipe1Y)
        is_collision(birdX, birdY, pipe2X, pipe2Y)
        # Calling floor
        floor(floorX, floorY)
        # Calling pipes
        pipes(pipe1X, pipe1Y, pipe2X, pipe2Y)
        # Calling bird
        bird(birdImg[2], birdX, birdY)
        # Displaying score and high score
        high_score_display(h_textX, h_textY)
        score_display(textX, textY)
        # Creating delay of 10ms
        pygame.time.delay(10)
        # Updating the screen
        pygame.display.update()

# End screen
def end_screen():
    global score_value, birdY, birdX, birdY_change, pipe1X, pipe2X, pipe1Y, pipe2Y, floorX, floorX_change
    end = True
    while end:
        screen.fill((255, 230, 230))
        if score_value > high_score_value['hs']:
            high_score_value['hs'] = score_value
        score_value = 0
        birdX = 51
        birdY = 309
        birdY_change = 1
        pipe1X = -40
        pipe1Y = random.randint(-280, -80)
        pipe2X = 250
        pipe2Y = random.randint(-280, -80)
        font1 = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        over_text = font1.render("GAME OVER", True, (250, 30, 30))
        main_play_text = font2.render("Press SPACE To Try Again", True, (100, 100, 100))
        screen.blit(main_play_text, (125, 200))
        screen.blit(over_text, (125, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_SPACE:
                    is_run()


        pygame.display.update()

main_menu()
