import pygame
import random
from math import *
from pygame import mixer

# calling pygame to start
pygame.init()

# setting the screen Dimensions
screen = pygame.display.set_mode((1000, 667))

# setting the Game window data
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player Initialization
playerImg = pygame.image.load('spaceship.png')
playerX = 470
playerY = 580
incrimentXminus = 0
incrimentXplus = 0
bcgrnd = pygame.image.load('background2.jpg')
score_value = 0
font =pygame.font.Font('freesansbold.ttf',18)
scoreX = 11
scoreY = 11

def disp_score():
    score = font.render("SCORE: "+ str(score_value), True, (0,255,0))
    screen.blit(score,(scoreX,scoreY))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
incriment_enemyX = []
incriment_enemyY = []

no_of_enemy = 8
for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(70, 940))
    enemyY.append(random.randint(30, 170))
    incriment_enemyX.append(0.8)
    incriment_enemyY.append(40)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = playerY
bullet_state = "ready"
game_overfont = pygame.font.Font("freesansbold.ttf",70)
def game_over():
    game_ovr = game_overfont.render("GAME OVER", True, (255,250,255))
    screen.blit(game_ovr,(250,300))


def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet(x, y):
    screen.blit(bulletImg, (x, y))


Running_status = True
while Running_status:
    screen.fill((0, 0, 0))
    screen.blit(bcgrnd, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running_status = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                incrimentXplus = 2
            if event.key == pygame.K_LEFT:
                incrimentXminus = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_state = "fire"
                    bulletX = playerX + 20
                    bulletY = playerY - 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                incrimentXplus = 0
            if event.key == pygame.K_LEFT:
                incrimentXminus = 0
    # enemy mechanics
    for i in range(no_of_enemy):
        if enemyX[i] <= 0:
            incriment_enemyX[i] = 0.8
            enemyY[i] += incriment_enemyY[i]
        if enemyX[i] >= 968:
            incriment_enemyX[i] = -0.8
            enemyY[i] += incriment_enemyY[i]
        enemyX[i] += incriment_enemyX[i]

        enemy(enemyX[i], enemyY[i], i)

        dist = sqrt(pow((enemyX[i] + 16) - (bulletX + 4), 2) + pow(enemyY[i] - bulletY, 2))
        if dist <= 25:
            blast = pygame.image.load('blast.png')
            screen.blit(blast, (enemyX[i], enemyY[i]))
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(70, 940)
            enemyY[i] = random.randint(30, 70)
            enemy(enemyX[i], enemyY[i], i)
        if enemyY[i]>=580:
           for j in range(no_of_enemy) :
               enemyY[j] = 1000
           game_over()
           break
    # player mechanics
    if playerX <= -64:
        playerX = 1000
    elif playerX >= 1000:
        playerX = -60
    playerX = playerX + incrimentXplus - incrimentXminus
    player(playerX, playerY)

    # bullet mechanics
    if bulletY == 0:
        bullet_state = "ready"
    if bullet_state == "fire":
        bulletY -= 4
        bullet(bulletX, bulletY)
    disp_score()
    pygame.display.update()
