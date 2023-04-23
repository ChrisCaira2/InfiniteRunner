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

coin = pygame.image.load('coin.jpg')
coin = pygame.transform.scale(coin, (30, 30))
coin1 = coin.get_rect()
coin2 = coin.get_rect()

white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0) 
purple = (221, 160, 221)
black = (0, 0, 0)
grey = (100, 100, 100)

obstaclesX = [random.randint(0, 200), random.randint(200, 400), random.randint(500, 700), 
                random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
obstaclesY = [0,0,0, -400, -400, -400]
obstacles_speed = .3
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)

my_font_start = pygame.font.SysFont('bahnschrift', 30)
my_font = pygame.font.SysFont('bahnschrift', 50)
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

    pygame.draw.rect(window, black, pygame.Rect(50, 30, 60, 40))
    pygame.draw.rect(window, purple, pygame.Rect(50, 30, 60, 40), 3)
    window.blit(start_esc, (60, 40))

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
        pygame.draw.rect(window, purple, pygame.Rect(150, 225, 380, 150))
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
        user = window.blit(current_alien, (rectX, rectY))
        player()
        #pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
        score_text = font.render(f'{score}', True, (0, 0, 0))
        coin_text = font.render(f'{math.floor(coin_count/1200)}', True, (0, 0, 0))

        window.blit(score_text, (340, 15))
        window.blit(coin, (0,0))
        window.blit(coin_text, (40,5))

        obstacle0 = pygame.draw.rect(window, red, (obstaclesX[0], obstaclesY[0], 45, 20))
        obstacle1 = pygame.draw.rect(window, orange, (obstaclesX[1], obstaclesY[1], 75, 20))
        obstacle2 = pygame.draw.rect(window, yellow, (obstaclesX[2], obstaclesY[2], 100, 20))
        obstacle3 = pygame.draw.rect(window, red, (obstaclesX[3], obstaclesY[3], 100, 20))
        obstacle4 = pygame.draw.rect(window, red, (obstaclesX[4], obstaclesY[4], 30, 20))
        obstacle5 = pygame.draw.rect(window, red, (obstaclesX[5], obstaclesY[5], 40, 20))
        obstacles = [obstacle0, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]

        for i in range(len(obstacles)):
            
            coin1.x = obstaclesX[1] + 100
            coin1.y = obstaclesY[1]

            coin2.x = obstaclesX[3] - 75
            coin2.y = obstaclesY[3]

            window.blit(coin, coin1)
            window.blit(coin, coin2)

            obstaclesY[i] += obstacles_speed

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
            
            if coin1.colliderect(user):
                pygame.draw.rect(window, white, (coin1.x, coin1.y, 30, 30))
                coin_count += 1
            
            if coin2.colliderect(user):
                pygame.draw.rect(window, white, (coin2.x, coin2.y, 30, 30))
                coin_count += 1

            if user.colliderect(obstacle0) or user.colliderect(obstacle1) or user.colliderect(obstacle2) or user.colliderect(obstacle3) or user.colliderect(obstacle4) or user.colliderect(obstacle5):
                obstaclesX = [random.randint(-10, 160), random.randint(200, 400), random.randint(500, 700), random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
                obstaclesY = [0,0,0, -400, -400, -400]
                active = False

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

    #player = pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
    
    move()

    window.fill(white)
    if active == False:
        startScreen()
        # score = 0
        # coin_count = 0
        # game_font = pygame.font.Font('freesansbold.ttf', 24)
        # TITLE = game_font.render("INFINITE RUNNER", True ,"White")
        # game_font_surface = game_font.render("Press space to start the game", True ,"White")
        
        # window.blit(bg, (0, 0))
        # window.blit(TITLE, (230, 170))
        # window.blit(game_font_surface, (170,230))
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         active = True

        #     if event.key == pygame.K_a:
        #         avatar_screen = True

        #     if event.key == pygame.K_ESCAPE:
        #         active = False

    # if avatar_screen:
    #     if red_car_button.draw():
    #         current_car = red_car

    #     if blue_car_button.draw():
    #         current_car = blue_car

    #     if green_car_button.draw():
    #         current_car = green_car

    #     if orange_car_button.draw():
    #         current_car = orange_car

    #     if purple_car_button.draw():
    #         current_car = purple_car

    #     if grey_car_button.draw():
    #         current_car = grey_car

    if avatar_screen:
        avatar()

    if active:
        game()
        # pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
        # score_text = font.render(f'{score}', True, (0, 0, 0))
        # coin_text = font.render(f'{math.floor(coin_count/800)}', True, (0, 0, 0))

        # window.blit(score_text, (340, 15))
        # window.blit(coin, (0,0))
        # window.blit(coin_text, (40,5))

        # obstacle0 = pygame.draw.rect(window, RED, (obstaclesX[0], obstaclesY[0], 45, 20))
        # obstacle1 = pygame.draw.rect(window, ORANGE, (obstaclesX[1], obstaclesY[1], 75, 20))
        # obstacle2 = pygame.draw.rect(window, YELLOW, (obstaclesX[2], obstaclesY[2], 100, 20))
        # obstacle3 = pygame.draw.rect(window, RED, (obstaclesX[3], obstaclesY[3], 100, 20))
        # obstacle4 = pygame.draw.rect(window, RED, (obstaclesX[4], obstaclesY[4], 30, 20))
        # obstacle5 = pygame.draw.rect(window, RED, (obstaclesX[5], obstaclesY[5], 40, 20))
        # obstacles = [obstacle0, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]

        # for i in range(len(obstacles)):
            
        #     coin1.x = obstaclesX[1] + 100
        #     coin1.y = obstaclesY[1]

        #     coin2.x = obstaclesX[3] - 75
        #     coin2.y = obstaclesY[3]

        #     window.blit(coin, coin1)
        #     window.blit(coin, coin2)

        #     obstaclesY[i] += obstacles_speed

        #     coin1.y += obstacles_speed
        #     coin2.y += obstacles_speed

        #     if obstaclesY[i] > 500:
        #         score += 1
        #         if score > 200:
        #             obstacles_speed = .50
        #         elif score > 150:
        #             obstacles_speed = .45
        #         elif score > 100:
        #             obstacles_speed = .40
        #         elif score > 60:
        #             obstacles_speed = .35
        #         elif score > 30:
        #             obstacles_speed = .30
        #         else:
        #             obstacles_speed = obstacles_speed

        #         rand = [random.randint(10, 200), random.randint(200, 400), random.randint(450, 650-rectSize), random.randint(100, 300), random.randint(390, 490), random.randint(510, 640)]
                
        #         obstaclesY[i] = random.randint(-200, -75)
        #         if obstaclesY[i] == obstaclesY[3]:
        #             obstaclesY[i] = obstaclesY[1]-random.randint(200, 350)
        #         if obstaclesY[i] == obstaclesY[4]:
        #             obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
        #         if obstaclesY[i] == obstaclesY[5]:
        #             obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
        #         obstaclesX[i] = rand[i]
            
        #     if coin1.colliderect(player):
        #         pygame.draw.rect(window, WHITE, (coin1.x, coin1.y, 30, 30))
        #         coin_count += 1
            
        #     if coin2.colliderect(player):
        #         pygame.draw.rect(window, WHITE, (coin2.x, coin2.y, 30, 30))
        #         coin_count += 1

        #     if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2) or player.colliderect(obstacle3) or player.colliderect(obstacle4) or player.colliderect(obstacle5):
        #             obstaclesX = [random.randint(-10, 160), random.randint(200, 400), random.randint(500, 700), random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
        #             obstaclesY = [0,0,0, -400, -400, -400]
        #             active = False

    # update the display window...
    pygame.display.update()
