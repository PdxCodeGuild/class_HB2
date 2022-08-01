import pygame
from pygame.locals import *

pygame.init()


screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('HB2_MCAPSTONE')

walk_r = []
walk_l = []
for num in range(1, 9):
    run_r = pygame.image.load(f'images/c{num}.png')
    run_r = pygame.transform.scale(run_r, (90, 60))
    img_left = pygame.transform.flip(run_r, True, False)
    walk_r.append(run_r)
    walk_l.append(img_left)
pdx_logo = pygame.image.load('images/pdx_logo.png')
background = pygame.image.load('images/bg_star.png')
me = pygame.image.load('images/honey_b.png')
me = pygame.transform.scale(me, (90, 60))

clock = pygame.time.Clock()
pewpew = pygame.mixer.Sound('images/pew.wav')


bground_image = pygame.image.load('images/brk_bg.png')
bg_logo = pygame.image.load('images/pdx_logo.png')

class Honeybadger():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 20
        self.c_Jump = False
        self.jordan = 10
        self.left = False
        self.right = False
        self.w_count = 0
        self.standing = True


    def draw(self, screen):
        if self.w_count +1 >= 27:
            self.w_count = 0
        
        if not(self.standing):        
            if self.left:
                screen.blit(walk_l[self.w_count//6], (self.x, self.y))
                self.w_count += 1
            elif self.right:
                screen.blit(walk_r[self.w_count//6], (self.x, self.y))
                self.w_count += 1
        else:
            if self.right:
                screen.blit(me, (self.x, self.y))
            else:
                screen.blit(pygame.transform.flip(me, True, False), (self.x, self.y))



class Blast():
    def __init__(self, x, y, size, color, direction):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.direction = direction
        self.speed = 27 * direction
    
    def draw(self, screen):
        b = pygame.image.load('images/py.png')
        b = pygame.transform.scale(b, (50, 50))
        self.b = b
        screen.blit(self.b, (self.x, self.y))
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

class Badguy():
    s1 = pygame.image.load('images/s1.png')
    s1 = pygame.transform.scale(s1, (200, 300))
    s2 = pygame.image.load('images/s2.png')
    s2 = pygame.transform.scale(s1, (200, 300))
    fs1 = pygame.transform.flip(s1, True, False)
    fs2 = pygame.transform.flip(s2, True, False)
    m_l = [s1, s2]
    m_r = [fs1, fs2]   
    def __init__(self, x, y, width, height, ded):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.ded = ded
        self.path = [self.x, self.ded]
        self.w_count = 0
        self.speed = 8

    def draw(self, screen):
        self.move()
        if self.w_count + 1 <= 40:
            self.w_count = 0

        if  self.speed > 0:
            screen.blit(self.m_r[self.w_count//6], (self.x, self.y))
            self.w_count += 1
        else:
            screen.blit(self.m_l[self.w_count//3], (self.x, self.y))
            self.w_count += 1
        pass
    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.w_count = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.w_count = 0
     

def draw_gw():
    screen.blit(background, (0, 0))
    screen.blit(pdx_logo, (50, 50))
    hb.draw(screen)
    snek.draw(screen)
    for blast in blasts:
        blast.draw(screen)
    # pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
    screen.fill((0, 0, 0))


#mainLoop
blasts = []
snek = Badguy(200, 700, 500, 500, 800)
hb = Honeybadger(25, 900, 90, 60)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for blast in blasts:
        if blast.x < screen_width and blast.x > 0:
            blast.x += blast.speed
        else:
            blasts.pop(blasts.index(blast))    

    key = pygame.key.get_pressed()
    if key[pygame.K_f]:
        pewpew.play()
        if hb.left:
            dir = -1
        else:
            dir = 1
        if len(blasts) < 100:
            blasts.append(Blast((round(hb.x + hb.width // 2)), (round(hb.y + hb.height//2)), 10, (0, 255, 0), dir))

    if key[pygame.K_LEFT] and hb.x > hb.speed or key[pygame.K_a] and hb.x > hb.speed:
        hb.left = True
        hb.right = False
        hb.x -= hb.speed
        hb.standing = False
    elif key[pygame.K_RIGHT] and hb.x < screen_width - hb.width or key[pygame.K_d] and hb.x < screen_width - hb.width:
        hb.right = True
        hb.left = False
        hb.x += hb.speed
        hb.standing = False
    else:
        hb.standing = True
        hb.w_count = 0

    if not(hb.c_Jump):
        # if key[pygame.K_UP] and y > speed or key[pygame.K_w] and y > speed:
        #     y -= speed
        # if key[pygame.K_DOWN] and y < screen_height - height or key[pygame.K_s] and y < screen_height - height:
        #     y += speed
        if key[pygame.K_SPACE]:
            hb.c_Jump = True
            hb.right = False
            hb.left = False
            hb.w_count = 0
    else:
        if hb.jordan >= -10:
            neg = 1
            if hb.jordan < 0:
                neg = -1
            hb.y -= (hb.jordan ** 2) * 0.5 * neg
            hb.jordan -= 1

        else:
            hb.c_Jump = False
            hb.jordan = 10
    
    draw_gw()

pygame.quit()