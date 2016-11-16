import pygame
import time
import easygui 
import pickle
import os
import sys
from bisect import bisect
import random
import threading

highscores = []
highscores = pickle.load(open("highscores.p", "rb"))
highscores.sort(reverse=True)


def ScreenStuff():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()


    song = 'C:/Users/Austin Abate/Downloads/Gamesongs/Track1.wav'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)

    
    
    global displayWidth, displayHeight, clock, blockWidth, blockHeight, PlayerBlockWidth, PlayerBlockHeight
    global FPS, screen, white, black, red, AIMOVE
    displayWidth = 500
    displayHeight = 500

    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)

    FPS = 120
    clock = pygame.time.Clock()

    blockWidth = 50
    blockHeight = 50
    PlayerBlockWidth = 100
    PlayerBlockHeight = 100
    
    pygame.display.set_caption('Austins Game')
    screen = pygame.display.set_mode([displayWidth, displayHeight])
    background = pygame.Surface(screen.get_size())
    background.fill((white))
    background = background.convert()
    screen.blit(background, (0,0))

    AIMOVE = pygame.USEREVENT + 1
    pygame.time.set_timer(AIMOVE, 40)

    mainloop()

def mainloop():
    mainloop = True
    global score
    score = 0.0
    
    global xStart, yStart, yStart_Change, xStart_Change
    xStart = displayWidth / 2
    yStart = displayHeight / 2
    xStart_Change = 25
    yStart_Change = 25

    global AIxStart, AIyStart, AIyStart_Change, AIxStart_Change, AIxStart2, AIyStart2, AIxStart3, AIyStart3, AIxStart4, AIyStart4
    AIxStart = 0
    AIyStart = 0
    AIxStart2 = displayWidth - blockWidth
    AIyStart2 = 0
    AIxStart3 = displayWidth - blockWidth
    AIyStart3 = displayHeight - blockHeight
    AIxStart4 = 0
    AIyStart4 = displayHeight - blockHeight
    AIxStart_Change = 25
    AIyStart_Change = 25
    
    while mainloop == True:
        
        

        milliseconds = clock.tick(FPS)
        score += milliseconds / 1000.0
        if mainloop == True:
            screen.fill(white)
        enemy = pygame.draw.rect(screen, red, ([AIxStart,AIyStart,blockWidth,blockHeight]))
        enemy2 = pygame.draw.rect(screen, red, ([AIxStart2,AIyStart2,blockWidth,blockHeight]))
        enemy3 = pygame.draw.rect(screen, red, ([AIxStart3,AIyStart3,blockWidth,blockHeight]))
        enemy4 = pygame.draw.rect(screen, red, ([AIxStart4,AIyStart4,blockWidth,blockHeight]))
        global player
        player = pygame.draw.rect(screen, black, ([xStart,yStart,PlayerBlockWidth,PlayerBlockHeight]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == AIMOVE:


                global vWeight,bWeight,nWeight,mWeight, vWeight2,bWeight2,nWeight2,mWeight2    
                vWeight = 25
                bWeight = 25
                nWeight = 25
                mWeight = 25
                vWeight2 = 25
                bWeight2 = 25
                nWeight2 = 25
                mWeight2 = 25
                vWeight3 = 25
                bWeight3 = 25
                nWeight3 = 25
                mWeight3 = 25
                vWeight4 = 25
                bWeight4 = 25
                nWeight4 = 25
                mWeight4 = 25


                
                def weighted_choice(choices):
                    global total
                    values, weights = zip(*choices)
                    total = 0
                    num_weights = []
                    for w in weights:
                        total += w
                        num_weights.append(total)
                    x = random.random() * total
                    i = bisect(num_weights, x)
                    return values[i]

                

                

                

                u = weighted_choice([("v",vWeight), ("b",bWeight), ("n",nWeight), ("m",mWeight)])
                o = weighted_choice([("v",vWeight), ("b",bWeight), ("n",nWeight), ("m",mWeight)])
                
                if u=='v':
                    vWeight3 + random.randint(1,100)
                    bWeight3 - random.randint(1,100)
                    nWeight3 - random.randint(1,100)
                    mWeight3 - random.randint(1,100)
                    AIyStart3 -= AIyStart_Change #AI goes up
                if u=='b':
                    vWeight3 - random.randint(1,100)
                    bWeight3 + random.randint(1,100)
                    nWeight3 - random.randint(1,100)
                    mWeight3 - random.randint(1,100)
                    AIyStart3 += AIyStart_Change #AI goes down
                if u=='n':
                    vWeight3 - random.randint(1,100)
                    bWeight3 - random.randint(1,100)
                    nWeight3 + random.randint(1,100)
                    mWeight3 - random.randint(1,100)
                    AIxStart3 += AIxStart_Change #AI goes right
                if u=='m':
                    vWeight3 - random.randint(1,100)
                    bWeight3 - random.randint(1,100)
                    nWeight3 - random.randint(1,100)
                    mWeight3 + random.randint(1,100)
                    AIxStart3 -= AIxStart_Change #AI goes left
                if o=='v':
                    vWeight4 + random.randint(1,100)
                    bWeight4 - random.randint(1,100)
                    nWeight4 - random.randint(1,100)
                    mWeight4 - random.randint(1,100)
                    AIyStart4 -= AIyStart_Change #AI goes up
                if o=='b':
                    vWeight4 + random.randint(1,100)
                    bWeight4 - random.randint(1,100)
                    nWeight4 - random.randint(1,100)
                    mWeight4 - random.randint(1,100)
                    AIyStart4 += AIyStart_Change #AI goes down
                if o=='n':
                    vWeight4 + random.randint(1,100)
                    bWeight4 - random.randint(1,100)
                    nWeight4 - random.randint(1,100)
                    mWeight4 - random.randint(1,100)
                    AIxStart4 += AIxStart_Change #AI goes right
                if o=='m':
                    vWeight4 + random.randint(1,100)
                    bWeight4 - random.randint(1,100)
                    nWeight4 - random.randint(1,100)
                    mWeight4 - random.randint(1,100)
                    AIxStart4 -= AIxStart_Change #AI goes left

                if AIxStart3 < 0:
                    AIxStart3 += AIxStart_Change #Force AI goes right
                if AIxStart3 > displayWidth - blockWidth:
                    AIxStart3 -= AIxStart_Change #Force AI goes left
                if AIyStart3 < 0:
                    AIyStart3 += AIyStart_Change #Force AI goes down
                if AIyStart3 > displayHeight - blockHeight:
                    AIyStart3 -= AIyStart_Change #Force AI goes up
                if AIxStart4 < 0:
                    AIxStart4 += AIxStart_Change #Force AI goes right
                if AIxStart4 > displayWidth - blockWidth:
                    AIxStart4 -= AIxStart_Change #Force AI goes left
                if AIyStart4 < 0:
                    AIyStart4 += AIyStart_Change #Force AI goes down
                if AIyStart4 > displayHeight - blockHeight:
                    AIyStart4 -= AIyStart_Change #Force AI goes up

                    

                
                j = weighted_choice([("v",vWeight), ("b",bWeight), ("n",nWeight), ("m",mWeight)])
                l = weighted_choice([("v",vWeight), ("b",bWeight), ("n",nWeight), ("m",mWeight)])
                if j=='v':
                    vWeight + random.randint(1,100)
                    bWeight - random.randint(1,100)
                    nWeight - random.randint(1,100)
                    mWeight - random.randint(1,100)
                    AIyStart -= AIyStart_Change #AI goes up
                if j=='b':
                    vWeight - random.randint(1,100)
                    bWeight + random.randint(1,100)
                    nWeight - random.randint(1,100)
                    mWeight - random.randint(1,100)
                    AIyStart += AIyStart_Change #AI goes down
                if j=='n':
                    vWeight - random.randint(1,100)
                    bWeight - random.randint(1,100)
                    nWeight + random.randint(1,100)
                    mWeight - random.randint(1,100)
                    AIxStart += AIxStart_Change #AI goes right
                if j=='m':
                    vWeight - random.randint(1,100)
                    bWeight - random.randint(1,100)
                    nWeight - random.randint(1,100)
                    mWeight + random.randint(1,100)
                    AIxStart -= AIxStart_Change #AI goes left
                if l=='v':
                    vWeight2 + random.randint(1,100)
                    bWeight2 - random.randint(1,100)
                    nWeight2 - random.randint(1,100)
                    mWeight2 - random.randint(1,100)
                    AIyStart2 -= AIyStart_Change #AI goes up
                if l=='b':
                    vWeight2 - random.randint(1,100)
                    bWeight2 + random.randint(1,100)
                    nWeight2 - random.randint(1,100)
                    mWeight2 - random.randint(1,100)
                    AIyStart2 += AIyStart_Change #AI goes down
                if l=='n':
                    vWeight2 - random.randint(1,100)
                    bWeight2 - random.randint(1,100)
                    nWeight2 + random.randint(1,100)
                    mWeight2 - random.randint(1,100)
                    AIxStart2 += AIxStart_Change #AI goes right
                if l=='m':
                    vWeight2 - random.randint(1,100)
                    bWeight2 - random.randint(1,100)
                    nWeight2 - random.randint(1,100)
                    mWeight2 + random.randint(1,100)
                    AIxStart2 -= AIxStart_Change #AI goes left

                if AIxStart < 0:
                    AIxStart += AIxStart_Change #Force AI goes right
                if AIxStart > displayWidth - blockWidth:
                    AIxStart -= AIxStart_Change #Force AI goes left
                if AIyStart < 0:
                    AIyStart += AIyStart_Change #Force AI goes down
                if AIyStart > displayHeight - blockHeight:
                    AIyStart -= AIyStart_Change #Force AI goes up
                if AIxStart2 < 0:
                    AIxStart2 += AIxStart_Change #Force AI goes right
                if AIxStart2 > displayWidth - blockWidth:
                    AIxStart2 -= AIxStart_Change #Force AI goes left
                if AIyStart2 < 0:
                    AIyStart2 += AIyStart_Change #Force AI goes down
                if AIyStart2 > displayHeight - blockHeight:
                    AIyStart2 -= AIyStart_Change #Force AI goes up

                pygame.display.update()

                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameOverMenu()
                if event.key == pygame.K_UP:
                    yStart -= yStart_Change
                    
                if event.key == pygame.K_DOWN:
                    yStart += yStart_Change
                    
                if event.key == pygame.K_LEFT:
                    xStart -= xStart_Change
                    
                if event.key == pygame.K_RIGHT:
                    xStart += xStart_Change
                    

            if xStart < 0 or xStart > displayWidth - PlayerBlockWidth:
                GameOverMenu()
            if yStart < 0 or yStart > displayHeight - PlayerBlockHeight:
                GameOverMenu()
            
            if mainloop == True:
                pygame.display.flip()
        if player.colliderect(enemy):
            GameOverMenu()
        if player.colliderect(enemy2):
            GameOverMenu()
        if player.colliderect(enemy3):
            GameOverMenu()
        if player.colliderect(enemy4):
            GameOverMenu()
        text = "Score: {1:.3f}".format(clock.get_fps(), score)
        pygame.display.set_caption(text)
        clock.tick(FPS)
            


    
def MainMenu():
    mainloop = False
    resolution = [800, 800]
    msg = 'Welcome to Austins Game.\nUse the arrow keys to move your black square\nAvoid going off of the edge of the map\nAvoid colliding with other rectangles'
    buttons = ['Quit', 'PLAY GAME', 'Scores']
    picture = None
    loop = True
    while loop == True:
        title = 'Austins Game'
        selection = easygui.buttonbox(msg, title, buttons, picture)
        if selection == "Quit":
            easygui.msgbox("bye-bye")
            loop = False
            pygame.quit()
        elif selection == "PLAY GAME":
            ScreenStuff()
        elif selection == 'Scores':
            easygui.msgbox(highscores)

def GameOverMenu():
    mainloop = False
    screen.fill(black)
    highscores.append(score)
    if len(highscores) > 5:
        highscores.remove(min(highscores))
    pickle.dump(highscores, open("highscores.p", "wb"))
    pygame.mixer.music.stop()
    pygame.display.update()
    resolution = [800,800]
    msg = ('GAME OVER. Your score was: ' + str(score))
    buttons = ['Quit', 'PLAY AGAIN']
    picture = None
    loop = True
    while loop == True:
        title = 'Austins Game'
        selection = easygui.buttonbox(msg, title, buttons, picture)
        if selection == "Quit":
            easygui.msgbox("bye-bye")
            loop = False
            pygame.quit()
        elif selection == "PLAY AGAIN":
            ScreenStuff()
    
MainMenu()
pygame.quit()
