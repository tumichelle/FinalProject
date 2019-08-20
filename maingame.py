import classDefs
from classDefs import *
import time

pygame.init()



def level1():
    play(60,70)

def level2():
    play(50,60)

def level3():
    play(40,50)



def play(leva,levb):
    W, H = 700, 391
    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Raising the Stakes')

    bg = pygame.image.load('GameBackground.png').convert()
    bgX = 0
    bgX2 = bg.get_width()
    clock = pygame.time.Clock()
    lives = pygame.image.load('lives.png')
    #ygame.time.set_timer(USEREVENT+2, random.randrange(tick * levela,tick * levelb)) #can change this to make level harder

    def life1():
        win.blit(pygame.transform.scale(lives, (25,25)), (660,10))

    def life2():
        win.blit(pygame.transform.scale(lives, (25,25)), (630,10))

    def life3():
        win.blit(pygame.transform.scale(lives, (25,25)), (600,10))

    def redrawWindow():
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2,0))
        if lifenum == 1:
            if live1 == True:
                life1()
        elif lifenum == 2:
            if live1 == True:
                life1()
            if live2 == True:
                life2()
        elif lifenum == 3:
            if live1 == True:
                life1()
            if live2 == True:
                life2()
            if live3 == True:
                life3()
        runner.draw(win)
        for x in objects:
                x.draw(win)
        pygame.display.update()

    def losescreen():
        global lifenum, die, live1, live2, live3, objects, speed, lose
        lifenum = random.randint(1,3)
        die = 0
        live1 = True
        live2 = True
        live3 = True
        objects = []
        speed = 30
        run = True
        lose = pygame.image.load('LoseScreen.png')
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     run = False
            win.blit(lose, [0,0])
            # largefont = pygame.font.SysFont('DisposableDroidBB.tff', 100)
            # youlose = largefont.render('YOU LOSE',1,(255,255,255))
            # win.blit(youlose,(180,100))
            pygame.display.update()



    flyind = random.randint(0,2)
    groundind = random.randint(0,3)
    runner = player(200, 160, 63, 111)
    pygame.time.set_timer(USEREVENT+1, 500)
    speed = 30
    run = True
    lifenum = random.randint(1,3)
    die = 0
    live1 = True
    live2 = True
    live3 = True


    objects = []
    tick = 0
    while run:
        tick += 1
        redrawWindow()
        for objectt in objects:
            if objectt.collide(runner.hitbox):
                runner.falling = True
                objects.pop(objects.index(objectt))
                if die == 0:
                    if lifenum == 1:
                        live1 = False
                        losescreen()
                    elif lifenum == 2:
                        live2 = False
                    elif lifenum == 3:
                        live3 = False
                    die += 1
                elif die == 1:
                    if lifenum == 2:
                        live1 = False
                        losescreen()
                    elif lifenum == 3:
                        live2 = False
                    die += 1
                elif die == 2:
                    live1 = False
                    losescreen()


            else:
                runner.falling = False

            objectt.x -= 12
            if objectt.x < objectt.width * -1:
                objects.pop(objects.index(objectt))

        bgX -= 13
        bgX2 -= 13
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()


        #print(pygame.event.get())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == USEREVENT+1:
                speed += 1

        if (tick%(random.randint(leva,levb))) == 0:
            r = random.randint(1,11)
            if r == 1:
                objects.append(bush1(710,230,44,64))
            elif r == 2:
                objects.append(bush2(710,232,60,75))
            elif r == 3 or r == 9:
                objects.append(trashcan(710,220,50,60))
            elif r == 4 or r == 10:
                objects.append(dog(710,240,75,45))
            elif r == 5:
                objects.append(birds1(710,150,120,50))
            elif r == 6:
                objects.append(birds2(710,150,120,50))
            elif r == 7:
                objects.append(birds3(710,150,120,50))
            elif r == 8 or r == 11:
                objects.append(firehydrant(710,230,55,65))
            tick = 0





        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not (runner.jumping):
                runner.jumping = True

        if keys[pygame.K_DOWN]:
            if not (runner.sliding):
                runner.sliding = True

        clock.tick(speed)
