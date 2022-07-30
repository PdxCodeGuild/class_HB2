import pygame
import random

pygame.init()
#creats screen and size
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('images/scene.png')

#Title and icon
pygame.display.set_caption('New Game BOI')
icon = pygame.image.load('images/strong.png')
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load('images/mma.png')
player_x = 100 #location of player on screen
player_y = 500
player_x_change = 0

#enemy
enemy_img = pygame.image.load('images/karate(1).png')
enemy_x = 700 #location of player on screen
enemy_y = 500
enemy_x_change = -0.3
enemy_y_change = 0

def player(x, y):
    screen.blit(player_img, (x, y)) #blit means to draw

def enemy(x, y):
    screen.blit(enemy_img, (x, y)) #blit means to draw


running = True
#infinte game loop to keep screen up
while running:

    #((R,G,B))0-255
    screen.fill((0, 0, 255))

    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checks if keystroke is right or left
        if event.type == pygame.KEYDOWN: #any key is pressed
            if event.key == pygame.K_LEFT:
                player_x_change = -0.4
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.4  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change #creates the movement
    enemy_x += enemy_x_change

    if player_x <= 0:  # this sets the boundaries for movement 
        player_x = 0
    elif player_x >= 736: #736 is 800 -64 to account for object size
        player_x = 736
    # enemy boundaries
    if enemy_x <= 0:  # this sets the boundaries for movement 
        enemy_x_change = 0.3

    elif enemy_x >= 736: #736 is 800 -64 to account for object size
        enemy_x_change = -0.3


    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update() #always have to use this when updating the screen
