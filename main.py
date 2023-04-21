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
rect = coin.get_rect()

WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0) 

obstaclesX = [random.randint(0, 200), random.randint(200, 400), random.randint(500, 700), 
                random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
obstaclesY = [0,0,0, -400, -400, -400]
obstacles_speed = .3
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)

active = False

rectSize = 20
rectX = winWidth / 2
rectY = 450
rectSpeed = .25

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

# create game loop
while True:
    
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

    player = pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
    
    move()

    window.fill(WHITE)
    if active == False:
        score = 0
        coin_count = 0
        game_font = pygame.font.Font('freesansbold.ttf', 24)
        TITLE = game_font.render("INFINITE RUNNER", True ,"White")
        game_font_surface = game_font.render("Press space to start the game", True ,"White")
        
        window.blit(bg, (0, 0))
        window.blit(TITLE, (230, 170))
        window.blit(game_font_surface, (170,230))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                active = True

    if active:
        pygame.draw.rect(window, MAGENTA, (rectX, rectY, rectSize, rectSize))
        score_text = font.render(f'{score}', True, (0, 0, 0))
        coin_text = font.render(f'{math.floor(coin_count/900)}', True, (0, 0, 0))

        window.blit(score_text, (340, 15))
        window.blit(coin, (0,0))
        window.blit(coin_text, (40,5))

        obstacle0 = pygame.draw.rect(window, RED, (obstaclesX[0], obstaclesY[0], 45, 20))
        obstacle1 = pygame.draw.rect(window, ORANGE, (obstaclesX[1], obstaclesY[1], 75, 20))
        obstacle2 = pygame.draw.rect(window, YELLOW, (obstaclesX[2], obstaclesY[2], 100, 20))
        obstacle3 = pygame.draw.rect(window, RED, (obstaclesX[3], obstaclesY[3], 100, 20))
        obstacle4 = pygame.draw.rect(window, RED, (obstaclesX[4], obstaclesY[4], 30, 20))
        obstacle5 = pygame.draw.rect(window, RED, (obstaclesX[5], obstaclesY[5], 40, 20))
        obstacles = [obstacle0, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]

        for i in range(len(obstacles)):
            rect.x = obstaclesX[1] + 100
            rect.y = obstaclesY[1]
            temp = pygame.draw.rect(window, WHITE, (rect.x, rect.y, 30, 30))
            window.blit(coin, rect)
            obstaclesY[i] += obstacles_speed
            rect.y += obstacles_speed
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

                rand = [random.randint(10, 200), random.randint(200, 400), random.randint(450, 650-rectSize), random.randint(100, 300), random.randint(390, 490), random.randint(510, 640)]
                
                obstaclesY[i] = random.randint(-200, -75)
                if obstaclesY[i] == obstaclesY[3]:
                    obstaclesY[i] = obstaclesY[1]-random.randint(200, 350)
                if obstaclesY[i] == obstaclesY[4]:
                    obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
                if obstaclesY[i] == obstaclesY[5]:
                    obstaclesY[i] = obstaclesY[2]-random.randint(200, 350)
                obstaclesX[i] = rand[i]
            
            if rect.colliderect(player):
                pygame.draw.rect(window, WHITE, (rect.x, rect.y, 30, 30))
                coin_count += 1

            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2) or player.colliderect(obstacle3) or player.colliderect(obstacle4) or player.colliderect(obstacle5):
                    obstaclesX = [random.randint(0, 200), random.randint(200, 400), random.randint(500, 700), random.randint(100, 350), random.randint(400, 500), random.randint(550, 650)]
                    obstaclesY = [0,0,0, -400, -400, -400]
                    active = False

    # update the display window...
    pygame.display.update()
