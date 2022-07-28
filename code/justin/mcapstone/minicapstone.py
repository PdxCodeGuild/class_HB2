import pygame

pygame.init()
#creats screen and size
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption('New Game BOI')
icon = pygame.image.load('strong.png')
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load('karate(1).png')
player_x = 100 #location of player on screen
player_y = 500

def player():
    screen.blit(player_img, (player_x, player_y)) #blit means to draw


running = True
#infinte game loop to keep screen up
while running:

    #((R,G,B))0-255
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update() #always have to use this when updating the screen
