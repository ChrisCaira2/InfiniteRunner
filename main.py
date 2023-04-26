import random
import pygame, sys
import math
import pygame.event as EVENTS

winWidth = 700
winHeight = 500

pygame.init()

window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("INFINITE RUNNER")

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (700, 500))

# cloud = pygame.image.load('cloud.png')
# coin = pygame.transform.scale(cloud, (50, 50))

#
# COINS
#
coin = pygame.image.load('coin1.png')
coin = pygame.transform.scale(coin, (30, 30))
coin1 = coin.get_rect()
coin2 = coin.get_rect()

#
# COLORS 
#
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0) 
purple = (221, 160, 221)
black = (0, 0, 0)
grey = (100, 100, 100)
green = (0,128,0)
sky = (0,191,255)

# OB1 = pygame.image.load('OB1.png')
# OBSTACLE = OB1.get_rect()
# OB_X = [random.randint(0, 200), random.randint(200, 400), random.randint(500, 700), 
#                 random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
# OB_Y = [0,0,0, -400, -400, -400]

obstaclesX = [random.randint(0, 200), random.randint(200, 400), random.randint(500, 620), 
                random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
obstaclesY = [0,0,0, -400, -400, -400]
obstacles_speed = .3
score = 0

#
# FONTS
#
font = pygame.font.Font('freesansbold.ttf', 16)
my_font_start = pygame.font.SysFont('copperplate', 30)
my_font = pygame.font.SysFont('copperplate', 35)

avatar_title = my_font.render('Avatar', False, (255, 255, 255))
start_esc = my_font_start.render('ESC', False, (255, 255, 255))

active = False
avatar_screen = False

rectSize = 20
rectX = winWidth / 2
rectY = 425
rectSpeed = .40

leftDown = False
rightDown = False

def gameExit():
    pygame.quit()
    sys.exit()

def move():
    global rectX

    # move left
    if leftDown:
        # check shape not exit window to left
        if rectX > 0.0:
            rectX -= rectSpeed
    # move right
    if rightDown:
        # check shape not exit window to right
        if rectX + rectSize < winWidth:
            rectX += rectSpeed

red_alien = pygame.image.load('red_alien.png')
blue_alien = pygame.image.load('blue_alien.png')
green_alien = pygame.image.load('green_alien.png')
orange_alien = pygame.image.load('orange_alien.png')
purple_alien = pygame.image.load('purple_alien.png')
grey_alien = pygame.image.load('grey_alien.png')
current_alien = red_alien

class avatar_Select():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        action = False

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))
        return action


red_alien_button = avatar_Select(140, 260, red_alien)
blue_alien_button = avatar_Select(300, 260, blue_alien)
green_alien_button = avatar_Select(460, 260, green_alien)
orange_alien_button = avatar_Select(140, 400, orange_alien)
purple_alien_button = avatar_Select(300, 400, purple_alien)
grey_alien_button = avatar_Select(460, 400, grey_alien)


def avatar():
    global current_alien
    global avatar_screen

    pygame.draw.rect(window, black, pygame.Rect(250, 30, 160, 50))
    pygame.draw.rect(window, purple, pygame.Rect(250, 30, 160, 50), 3)
    window.blit(avatar_title, (270, 40))

    pygame.draw.rect(window, black, pygame.Rect(50, 30, 70, 40))
    pygame.draw.rect(window, purple, pygame.Rect(50, 30, 70, 40), 3)
    window.blit(start_esc, (55, 30))

    pygame.draw.rect(window, grey, pygame.Rect(85, 230, 500, 250))
    pygame.draw.rect(window, purple, pygame.Rect(85, 230, 500, 250), 5)

    pygame.draw.rect(window, grey, pygame.Rect(180, 100, 300, 100))
    pygame.draw.rect(window, purple, pygame.Rect(180, 100, 300, 100), 2)
    window.blit(current_alien, (300, 125))

    if red_alien_button.draw():
        current_alien = red_alien

    if blue_alien_button.draw():
        current_alien = blue_alien

    if green_alien_button.draw():
        current_alien = green_alien

    if orange_alien_button.draw():
        current_alien = orange_alien

    if purple_alien_button.draw():
        current_alien = purple_alien

    if grey_alien_button.draw():
        current_alien = grey_alien

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            avatar_screen = False

def startScreen():
        global score
        global coin_count
        global active 
        global avatar_screen
        score = 0
        coin_count = 0
        window.blit(bg, (0, 0))

        game_font = pygame.font.Font('freesansbold.ttf', 24)
        title_font = pygame.font.Font('freesansbold.ttf', 32)

        TITLE = title_font.render("INFINITE RUNNER", True ,"White")
        pygame.draw.rect(window, sky, pygame.Rect(150, 225, 380, 150))
        pygame.draw.rect(window, black, pygame.Rect(150, 225, 380, 150), 5)
        start_game = game_font.render("Press Space to start the game", True ,"White")
        choose_avatar = game_font.render("Press A to select avatar", True ,"White")
        
            
        window.blit(TITLE, (195, 170))
        window.blit(start_game, (170,250))
        window.blit(choose_avatar, (205, 320))
        if event.type == pygame.KEYUP and avatar_screen == False:
            if event.key == pygame.K_SPACE:
                avatar_screen = False
                active = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                active = False
                avatar_screen = True

def player():
    user = window.blit(current_alien, (rectX, rectY))
            
def game():
        global score
        global coin_count
        global obstaclesX
        global obstaclesY
        global obstacles_speed
        global active 
        global rectSpeed
        # global OB_Y
        # global OB_X

        user = window.blit(current_alien, (rectX, rectY))
        player()
        #pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
        score_text = font.render(f'{score}', True, white)
        coin_text = font.render(f'{math.floor(coin_count/1200)}', True, white)
        title_font = pygame.font.Font('freesansbold.ttf', 32)
        show_score = font.render('Score:', True, white)
        show_coins = font.render('Coins:', True, white)
        menu = font.render('Press M to go back to Main Menu', True, white)
        FAIL = title_font.render("YOU DIED", True ,"White")

        window.blit(score_text, (340, 15))
        window.blit(coin, (0,0))
        window.blit(coin_text, (40,5))

        # window.blit(OB1, (OB_X[0],OB_Y[0]))
        # window.blit(OB1, (OB_X[1],OB_Y[1]))
        # window.blit(OB1, (OB_X[2],OB_Y[2]))
        # window.blit(OB1, (OB_X[3],OB_Y[3]))
        # window.blit(OB1, (OB_X[4],OB_Y[4]))
        # window.blit(OB1, (OB_X[5],OB_Y[5]))
   

        # obstacle0 = (OB1, (OBSTACLE.x,OBSTACLE.y))
        # obstacle1 = (OB1, (OBSTACLE.x,OBSTACLE.y))
        # obstacle2 = (OB1, (OBSTACLE.x,OBSTACLE.y))
        # obstacle3 = (OB1, (OBSTACLE.x,OBSTACLE.y))
        # obstacle4 = (OB1, (OBSTACLE.x,OBSTACLE.y))
        # obstacle5 = (OB1, (OBSTACLE.x,OBSTACLE.y))

        obstacle0 = pygame.draw.rect(window, red, (obstaclesX[0], obstaclesY[0], 45, 20))
        obstacle1 = pygame.draw.rect(window, orange, (obstaclesX[1], obstaclesY[1], 75, 20))
        obstacle2 = pygame.draw.rect(window, yellow, (obstaclesX[2], obstaclesY[2], 90, 20))
        obstacle3 = pygame.draw.rect(window, red, (obstaclesX[3], obstaclesY[3], 90, 20))
        obstacle4 = pygame.draw.rect(window, orange, (obstaclesX[4], obstaclesY[4], 30, 20))
        obstacle5 = pygame.draw.rect(window, red, (obstaclesX[5], obstaclesY[5], 40, 20))
        obstacles = [obstacle0, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]

        for i in range(len(obstacles)):
            
            coin1.x = obstaclesX[1] + 100
            coin1.y = obstaclesY[1] + 75

            coin2.x = obstaclesX[3] - 85
            coin2.y = obstaclesY[3] - 50

            window.blit(coin, coin1)
            window.blit(coin, coin2)

            obstaclesY[i] += obstacles_speed
            # OB_Y[i] += obstacles_speed

            coin1.y += obstacles_speed
            coin2.y += obstacles_speed

            if obstaclesY[i] > 500:
                score += 1
                if score > 200:
                    obstacles_speed = .50
                elif score > 150:
                    obstacles_speed = .45
                elif score > 100:
                    obstacles_speed = .40
                elif score > 60:
                    obstacles_speed = .35
                elif score > 30:
                    obstacles_speed = .30
                else:
                    obstacles_speed = obstacles_speed

                rand = [random.randint(0, 200), random.randint(200, 400), random.randint(450, 620-rectSize), random.randint(100, 300), random.randint(390, 490), random.randint(510, 640)]
                
                obstaclesY[i] = random.randint(-200, -75)
                if obstaclesY[i] == obstaclesY[3]:
                    obstaclesY[i] = obstaclesY[1]-random.randint(200, 350)
                if obstaclesY[i] == obstaclesY[4]:
                    obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
                if obstaclesY[i] == obstaclesY[5]:
                    obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
                obstaclesX[i] = rand[i]

                # OB_Y[i] = random.randint(-200, -75)
                # if OB_Y[i] == OB_Y[3]:
                #     OB_Y[i] = OB_Y[1]-random.randint(200, 350)
                # if OB_Y[i] == OB_Y[4]:
                #     OB_Y[i] = OB_Y[2]-random.randint(200, 350)
                # if OB_Y[i] == OB_Y[5]:
                #     OB_Y[i] = OB_Y[2]-random.randint(200, 350)
                # OB_X[i] = rand[i]
            
            if coin1.colliderect(user) and coin1.y < 500:
                pygame.draw.rect(window, sky, (coin1.x, coin1.y, 30, 30))
                coin_count += 1
            
            if coin2.colliderect(user) and coin2.y < 500:
                pygame.draw.rect(window, sky, (coin2.x, coin2.y, 30, 30))
                coin_count += 1

            if user.colliderect(obstacle0) or user.colliderect(obstacle1) or user.colliderect(obstacle2) or user.colliderect(obstacle3) or user.colliderect(obstacle4) or user.colliderect(obstacle5):
                obstacles_speed = 0 
                rectSpeed = 0

                window.blit(FAIL, (260, 120))
                window.blit(show_score, (300, 190))
                window.blit(score_text, (360, 190))
                window.blit(show_coins, (300, 240))
                window.blit(coin_text, (360, 240))
                window.blit(menu, (220, 290))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        active = False
                        rectSpeed = .40
                        obstacles_speed = .30
                        obstaclesX = [random.randint(-10, 160), random.randint(200, 400), random.randint(500, 620), random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
                        obstaclesY = [0,0,0, -400, -400, -400]
        
                

ingame = True
while ingame:
    
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True

        # check keyboard events - keyup
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
            if event.key == pygame.K_RIGHT:
                rightDown = False
                

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()  
    
    move()

    window.fill(white)
    if active == False:
        startScreen()

    if avatar_screen:
        avatar()

    if active:
        pygame.draw.rect(window, sky, (0, 0, 700, 500))
        pygame.draw.rect(window, green, (0, 480, 700, 20))
        game()
        
    # update the display window...
    pygame.display.update()
