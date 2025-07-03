import pygame
import random
import math


pygame.init()


# Display settings
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('player.png')
playerX = 218
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))


# Bullet
bulletImg = pygame.image.load('player_bullet.png')
bulletY = playerY
bulletX = playerX
bulletY_change = 3
bullet_state = "ready"
def fire(img, x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(img, (x+20, y))


# Collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    if distance < 27:
        return True
    else:
        return False


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
no_of_enemies = 6
for num in range(no_of_enemies):
    enemyImg.append(pygame.image.load('enemy1.png'))
    enemyX.append(random.randint(50, 450))
    enemyY.append(random.randrange(35, 70, 15))
    enemyX_change.append(0.2)
    enemyY_change.append(15)
def enemy(x, y):
    for iss in range(no_of_enemies):
        screen.blit(enemyImg[iss], (x, y))


# Blaster
blasterImg = pygame.image.load('enemy_bullet.png')
blasterX = enemyX
blasterY = enemyY
blasterY_change = 0.25
blaster_state = "ready"
def blast(x, y):
    global blaster_state
    blaster_state = "fire"
    screen.blit(blasterImg, (x + 20, y))


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 15)
textX = 7
textY = 10
def scoring(x, y):
    score = font.render("Score: " + str(score_value), True, (200, 200, 250))
    screen.blit(score, (x, y))

# Health
health_value = 5
fonth = pygame.font.Font('freesansbold.ttf', 15)
textXh = 430
textYh= 10
def healthy(x, y):
    health = fonth.render("Health: " + str(health_value), True, (250, 250, 250))
    if health_value == 5:
        health = fonth.render("Health: " + str(health_value), True, (250, 250, 250))
    elif health_value == 4:
        health = fonth.render("Health: " + str(health_value), True, (250, 200, 200))
    elif health_value == 3:
        health = fonth.render("Health: " + str(health_value), True, (250, 150, 150))
    elif health_value == 2:
        health = fonth.render("Health: " + str(health_value), True, (250, 100, 100))
    elif health_value == 1:
        health = fonth.render("Health: " + str(health_value), True, (250, 50, 50))
    screen.blit(health, (x, y))

# Game menu
def mainmenu():
    main = True
    while main:
        screen.fill((0, 0, 0))
        font1 = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        main_text = font1.render("Main Menu", True, (100, 100, 100))
        main_play_text = font2.render("Press SPACE To Play", True, (100, 100, 100))
        screen.blit(main_text, (150, 100))
        screen.blit(main_play_text, (155, 200))
        for event_main in pygame.event.get():
            if event_main.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_main.type == pygame.KEYDOWN:
                if event_main.key == pygame.K_SPACE:
                    main = False
        pygame.display.update()

# Game run
def run():
    global playerY
    global playerX
    global playerY_change
    global playerX_change
    global bulletX
    global bulletY
    global score_value
    global bullet_state
    global blaster_state
    global blasterX
    global blasterY
    global health_value
    global no_of_enemies
    running = True
    while running:
        screen.fill((0, 0, 0))
        playerX += playerX_change
        playerY += playerY_change
        if playerX < 0:
            playerX = 0
        if playerX > 436:
            playerX = 436
        if playerY < 0:
            playerY = 0
        if playerY > 536:
            playerY = 536
        for i in range(no_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] > 450:
                enemyX_change[i] = -0.2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] < 50:
                enemyX_change[i] = 0.2
                enemyY[i] += enemyY_change[i]
            enemy(enemyX[i], enemyY[i])
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = playerY
                bullet_state = "ready"
                score_value += 5
                enemyX[i] = random.randint(50, 450)
                enemyY[i] = random.randrange(35, 70, 15)
            if blaster_state == "ready":
                blast(enemyX[i], enemyY[i])
                blasterY = enemyY[i]
                blasterX = enemyX[i]
            if blaster_state == "fire":
                blast(blasterX, blasterY)
                blasterY += blasterY_change
            if blasterY >= 600:
                blaster_state = "ready"
            collision = is_collision(playerX, playerY, blasterX, blasterY)
            if collision:
                health_value -= 1
                blaster_state = "ready"
        player(playerX, playerY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change -= 0.5
                if event.key == pygame.K_RIGHT:
                    playerX_change += 0.5
                if event.key == pygame.K_UP:
                    playerY_change -= 0.5
                if event.key == pygame.K_DOWN:
                    playerY_change += 0.5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire(bulletImg, bulletX, playerY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        if bullet_state == "fire":
            fire(bulletImg, bulletX, bulletY)
            bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"
        healthy(textXh, textYh)
        if health_value == 0:
            ending = True
            while ending:
                screen.fill((0,0,0))
                score_value = 0
                font1 = pygame.font.Font('freesansbold.ttf', 40)
                font2 = pygame.font.Font('freesansbold.ttf', 20)
                over_text = font1.render("GAME OVER", True, (250, 30, 30))
                main_play_text = font2.render("Press SPACE To Try Again", True, (100, 100, 100))
                screen.blit(main_play_text, (125, 200))
                screen.blit(over_text, (125, 100))
                for event_main in pygame.event.get():
                    if event_main.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event_main.type == pygame.KEYDOWN:
                        if event_main.key == pygame.K_SPACE:
                            health_value = 5
                            run()
                        if event_main.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                pygame.display.update()
        scoring(textX, textY)
        pygame.display.update()

mainmenu()
run()