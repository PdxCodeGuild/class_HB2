import pygame
from sys import exit


#Player running animations
def player_physics():
    global play_surf, player_running_index, player_jumping_index

    if play_rect.bottom >= 200:
        play_surf = player_jumping
        player_jumping_index += 0.5
        if player_jumping_index >= len(player_jumping):
            player_jumping_index = 0
        play_surf = player_jumping[int(player_jumping_index)]

    player_running_index += 0.15
    if player_running_index >= len(player_running):
        player_running_index = 0
    play_surf = player_running[int(player_running_index)]


#Starts pygame and initializes all sub parts
pygame.init()

background_music = pygame.mixer.Sound('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/music.wav')
background_music.set_volume(0.2)
background_music.play(-1)
jump_sound = pygame.mixer.Sound('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/mixkit-player-jumping-in-a-video-game-2043.wav')
jump_sound.set_volume(0.1)

#Display surface
#Taking the dimensions of the screen (x-axis = 384, and y-axis = 216) and storing them in a tuple
screen = pygame.display.set_mode((384, 216))


#Title that you'll see in the top left portion
pygame.display.set_caption("S2, Ep18, (8:31), Off")


#Framerate
clock = pygame.time.Clock()


#Font (Type and size)
font = pygame.font.Font('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/Pixeltype (1).ttf', 15)


#Regular Background surface. '''.convert()''' what this is doing is - Instead of python processing the imaga pixal by pixal, it uses a format that grabs the                     
back_drop_surf = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/plx-1.png').convert_alpha()
tree_drop_surf_1 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/plx-2.png').convert_alpha()
tree_drop_surf_2 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/plx-3.png').convert_alpha()
tree_drop_surf_3 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/plx-4.png').convert_alpha()
tree_drop_surf_4 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/plx-5.png').convert_alpha()


#Regular ground surface. The '''fill('grey')''' is taking the surface and filling it with a pre-defined-color
grnd_drop_surf = pygame.Surface((384, 216))
grnd_drop_surf.fill('grey')
grnd_drop_surf_2 = pygame.Surface((384, 216))
grnd_drop_surf_2.fill('gray55')


#Regular coin surface. '''midbottom''' lets you choose where you would like to place your 'rect' at 9 different points
coin_surf = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/parallax background/coin_01a.png").convert_alpha()
coin_rect = coin_surf.get_rect(midbottom = (300, 100))


#Regular player surface + physics
play_run_1 = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-01.png").convert_alpha()
play_run_2 = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-02.png").convert_alpha()
play_run_3 = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-03.png").convert_alpha()
play_run_4 = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-04.png").convert_alpha()
play_run_5 = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-05.png").convert_alpha()
player_running = [play_run_1, play_run_2, play_run_3, play_run_4, play_run_5]
player_running_index = 0
play_surf = player_running[player_running_index]

play_jump_1 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-jump-00.png').convert_alpha()
play_jump_2 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-jump-01.png').convert_alpha()
play_jump_3 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-jump-02.png').convert_alpha()
play_jump_4 = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-jump-03.png').convert_alpha()
player_jumping = [play_jump_1, play_jump_2, play_jump_3, play_jump_4]
player_jumping_index = 0
play_rect = play_surf.get_rect(midbottom = (90, 200))

#Regular enemy surface + physics
en_surf = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/Troll_Walk_1.png").convert_alpha()
en_surf = pygame.transform.flip(en_surf, True, False)
en_surf = pygame.transform.scale(en_surf, (20, 30))
en_rect = en_surf.get_rect(midbottom = (300, 200))


#Text (text, anti aliasing, pre-defined-color - (IF wanted, instead of 'black' I could put (0,0,0) in place of it))
title_surf = font.render('Mini-capstone', False, 'black')
title_rect = title_surf.get_rect(midtop = (384 / 2, 10))
score_surf = font.render('SCORE', False, 'gold')
score_rect = score_surf.get_rect(topleft = (10, 10))

menu_surf = font.render('Press the spacebar to start the game', False, 'white')
menu_rect = menu_surf.get_rect(midtop = (384 / 2, 10))


#Title
en_title_surf = pygame.image.load("C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/Troll_Walk_1.png").convert_alpha()
en_title_surf = pygame.transform.scale(en_title_surf, (200, 200))
en_title_rect = en_title_surf.get_rect(midbottom = (20, 216))
title_image = pygame.image.load('C:/Users/mudbo/pdx_code/programming_101/unit_2/Background layers/adventurer-run-04.png').convert()
title_image = pygame.transform.scale(title_image, (200, 200))
title_image_rect = title_image.get_rect(midbottom = (384 / 2, 216))
 

#Gravity is going to be used for my jumping
gravity = 0 

#Just for animation when not dead
game_running = False


#This allows the window to stay on until False
while True:


    #Now it's time to check for events (If you move your mouse, click an arrow key, space, etc...)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #SPACEBAR for jumping
        if game_running:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and play_rect.bottom == 200:
                    gravity = -15
                    jump_sound.play()
        

        #SPACEBAR for restarting game
        else:
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                    en_rect.left = 300


    if game_running:   
        
        
        #BACKGROUND
        screen.blit(back_drop_surf,(0,0))
        screen.blit(tree_drop_surf_1,(0,0))


        screen.blit(tree_drop_surf_2,(0,0))
        screen.blit(coin_surf, coin_rect)
        screen.blit(tree_drop_surf_3,(0,0))
        screen.blit(tree_drop_surf_4,(0,0))


        #GROUND
        screen.blit(grnd_drop_surf,(0,200))
        screen.blit(grnd_drop_surf_2,(0,202))
        

        #TEXT
        screen.blit(title_surf, title_rect)
        screen.blit(score_surf, score_rect)
        
        
        #PLAYER ACTION
        #How gravity works - if you +1 gravity on player pos(190) it adds 1 (1 + 190 = 191) on the next loop (1 + 1 + 191 = 193)
        gravity += 0.8
        play_rect.y += gravity
        if play_rect.bottom >= 200:
            play_rect.bottom = 200
        player_physics()
        screen.blit(play_surf,play_rect)
        

        #ENEMY ACTION
        en_rect.x -= 3
        screen.blit(en_surf, en_rect)
        if en_rect.right <= 0:
            en_rect.left = 384


        #END GAME
        if en_rect.colliderect(play_rect):
            game_running = False


    else:
        screen.fill('black')
        screen.blit(title_image, title_image_rect)
        screen.blit(menu_surf, menu_rect)
        screen.blit(en_title_surf, en_title_rect)
    
       
    #Continues to update the surface while running through the loop
    pygame.display.update()

    #Framerate
    clock.tick(60)