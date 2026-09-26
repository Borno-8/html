import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HIEGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_START_X_SPEED = 4
ENEMY_START_Y_SPEED = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))

pygame.display.set_caption("Space Invador")
icon = pygame.image.load('space shooter icon.jpg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player space shooter.jpg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy space shooter.jpeg'))
    enemyX.append(random.randit(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randit(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_START_X_SPEED)
    enemyY_change.append(ENEMY_START_Y_SPEED)

    bulletImg = pygame.image.load('bullet space shooter.png')
    bulletX = 0
    bulletY = PLAYER_START_Y
    bulletX_change = 0
    bulletY_change = BULLET_SPEED_Y
    bullet_state = "ready"

    score_value = 0
    font = pygame.fontFont('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    over_font = pygame.fontFont('freesansbold.ttf', 64)

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (225, 255, 255))
        screen.blit(score, (x, y))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
        return distance < COLLISION_DISTANCE

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0,0))