import classDefs
from classDefs import *
import time

pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
blue = (0,0,255)

#music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

game_display = pygame.display.set_mode((display_width,display_height))

largeText = pygame.font.SysFont("DisposableDroidBB.ttf", 50)
mediumText = pygame.font.SysFont("DisposableDroidBB.ttf", 35)
startText = pygame.font.SysFont("DisposableDroidBB.ttf", 75)
steakText = pygame.font.SysFont("DisposableDroidBB.ttf", 60)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)
nameText = pygame.font.SysFont("DisposableDroidBB.ttf", 25)
hugeText = pygame.font.SysFont("DisposableDroidBB.ttf", 100)

mouse = pygame.mouse.get_pos()


#checks if button is clicked, does action
def button_check(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            button['action']()

#changes button when moused over
def button_draw(button, font):
    mouse = pygame.mouse.get_pos()
    if button['rect'].collidepoint(mouse):
        color = button['ic']
    else:
        color = button['ac']

    pygame.draw.rect(game_display, color, button['rect'])

    image, rect = textWhite(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)


def textWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textRed(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()


#quit game function
def quit_game():
    pygame.quit()
    quit()

#main intro page (with buttons to about and instructions)
def game_intro():

    background_image = pygame.image.load("SteakStart.png")
    game_display.blit(background_image, [0, 0])
    TextSurf, TextRect = textWhite('RAISING THE', largeText)
    TextRect.center = ((350),(45))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textWhite('STEAKS', steakText)
    TextRect.center = ((345),(180))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()


    buttons = [
        {
            'msg': 'INSTRUCTIONS',
            'rect': pygame.Rect(25, 310, 190, 60),
            'ac': black,
            'ic': red,
            'action': instructions_loop,
        },
        {
            'msg': 'ABOUT',
            'rect': pygame.Rect(530, 310, 90, 60),
            'ac': black,
            'ic': red,
            'action': about_loop,
        },
        {
            'msg': 'START',
            'rect': pygame.Rect(280, 305, 140, 70),
            'ac': black,
            'ic': blue,
            'action': levels_loop,
        }
    ]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])
                button_check(buttons[2])

        button_draw(buttons[0], mediumText)
        button_draw(buttons[1], mediumText)
        button_draw(buttons[2], largeText)

        pygame.display.update()

#instructions page with back button
def instructions_loop():
    background_image = pygame.image.load("THEMOTHERFRICKINGINTROANDABOUT.png")
    game_display.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('INSTRUCTIONS', largeText)
    TextRect.center = ((355),(73))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(582, 318, 80, 40),
            'ac': black,
            'ic': red,
            'action': game_intro,
        }
    ]

    #Instructional Text, Brought to you by AJ
    TextSurf, TextRect = textWhite("OBJECTIVE: GATHER 600 POINTS TO 'RAISE THE STEAKS'", smallText)
    TextRect.center = ((270),(140))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("AVOID THE OBSTACLES USING THE ARROW KEY", smallText)
    TextRect.center = ((230),(170))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("THIS GAME TEACHES RISK VERSUS REWARD, EARNING: ", smallText)
    TextRect.center = ((260),(200))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("100 POINTS FOR LEVEL 1 ", smallText)
    TextRect.center = ((270),(230))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("200 POINTS FOR LEVEL 2 ", smallText)
    TextRect.center = ((270),(260))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("300 POINTS FOR LEVEL 3 ", smallText)
    TextRect.center = ((270),(290))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("PLOT TWIST: THE NUMBER OF LIVES YOU GET IS RANDOMIZED ", smallText)
    TextRect.center = ((280),(320))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GOOD LUCK RAISING THE STEAKS! ", mediumText)
    TextRect.center = ((270),(350))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])

        button_draw(buttons[0], mediumText)
        pygame.display.update()

#about page with back button
def about_loop():
    background_image = pygame.image.load("THEMOTHERFRICKINGINTROANDABOUT.png")
    game_display.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('ABOUT', largeText)
    TextRect.center = ((350),(73))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(582, 318, 80, 40),
            'ac': black,
            'ic': red,
            'action': game_intro,
        }
    ]

#michelle's bio
    michelle = pygame.image.load("michelle.jpeg")
    game_display.blit(michelle, (20,130))
    TextSurf, TextRect = textWhite("MICHELLE TU", nameText)
    TextRect.center = ((210),(140))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 12", smallText)
    TextRect.center = ((210),(180))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("LEXINGTON", smallText)
    TextRect.center = ((210),(200))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("HIGH SCHOOL", smallText)
    TextRect.center = ((210),(220))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

#leia's bio
    leia = pygame.image.load("aj.jpeg")
    game_display.blit(leia, (300,130))
    TextSurf, TextRect = textWhite("AJ CHAU", nameText)
    TextRect.center = ((500),(140))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 11", smallText)
    TextRect.center = ((500),(180))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("ALUM OF SOULE", smallText)
    TextRect.center = ((500),(200))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("EARLY CHILDHOOD CENTER", smallText)
    TextRect.center = ((510),(220))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

#ellie's bio
    ellie = pygame.image.load("ellie.jpeg")
    game_display.blit(ellie, (20,270))
    TextSurf, TextRect = textWhite("ELLIE", nameText)
    TextRect.center = ((210),(290))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("KLIBANER-SCHIFF", nameText)
    TextRect.center = ((210),(310))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 11", smallText)
    TextRect.center = ((210),(340))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("MAIMONIDES", smallText)
    TextRect.center = ((210),(360))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

#aj's bio
    aj = pygame.image.load("leia.jpeg")
    game_display.blit(aj, (300,270))
    TextSurf, TextRect = textWhite("LEIA PAYANO", nameText)
    TextRect.center = ((480),(290))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 12", smallText)
    TextRect.center = ((480),(330))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("KIPP ACADEMY", smallText)
    TextRect.center = ((480),(350))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])

        button_draw(buttons[0], mediumText)
        pygame.display.update()

#levels page after pressing start button
def levels_loop():
    background_image = pygame.image.load("MichellePleaseStop.png")
    game_display.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('CHOOSE A DIFFICULTY', largeText)
    TextRect.center = ((355),(73))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(582, 318, 80, 40),
            'ac': black,
            'ic': red,
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 1 (+100pts)',
            'rect': pygame.Rect(62, 150, 340, 40),
            'ac': black,
            'ic': (135,206,235),
            'action': level1,
        },
        {
            'msg': 'LEVEL 2 (+200pts)',
            'rect': pygame.Rect(62, 225, 340, 40),
            'ac': black,
            'ic': (30,144,255),
            'action': level2,
        },
        {
            'msg': 'LEVEL 3 (+300pts)',
            'rect': pygame.Rect(62, 300, 340, 40),
            'ac': black,
            'ic': (0,0,139),
            'action': level3,
        }
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])
                button_check(buttons[2])
                button_check(buttons[3])

        button_draw(buttons[0], mediumText)
        button_draw(buttons[1], mediumText)
        button_draw(buttons[2], mediumText)
        button_draw(buttons[3], mediumText)
        pygame.display.update()




def level1():
    play(60,70)

def level2():
    play(50,60)

def level3():
    play(40,50)


def play(leva,levb):
    time = 0
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

        buttons = [
            {
                'msg': 'MAIN MENU',
                'rect': pygame.Rect(480, 318, 180, 40),
                'ac': black,
                'ic': red,
                'action': game_intro,
            },
            {
                'msg': 'REPLAY',
                'rect': pygame.Rect(50, 318, 140, 40),
                'ac': black,
                'ic': red,
                'action': levels_loop,
            }
            ]


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
            while True:
                TextSurf, TextRect = textWhite("YOU LOSE", hugeText)
                TextRect.center = ((350),(140))
                game_display.blit(TextSurf, TextRect)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit_game()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        button_check(buttons[0])
                        button_check(buttons[1])

                button_draw(buttons[0], mediumText)
                button_draw(buttons[1], mediumText)
                pygame.display.update()


    def finishscreen():
        run = True
        finish = pygame.image.load('levelcomplete.png')
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            win.blit(finish,[0,0])
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
        time += 1
        redrawWindow()
        for objectt in objects:
            if objectt.collide(runner.hitbox):
                runner.falling = True
                objects.pop(objects.index(objectt))
                if die == 0:
                    if lifenum == 1:
                        live1 = False
                        losescreen()
                        time = 0
                    elif lifenum == 2:
                        live2 = False
                    elif lifenum == 3:
                        live3 = False
                    die += 1
                elif die == 1:
                    if lifenum == 2:
                        live1 = False
                        losescreen()
                        time = 0
                    elif lifenum == 3:
                        live2 = False
                    die += 1
                elif die == 2:
                    live1 = False
                    losescreen()
                    time = 0
            elif time >= 1000:
                objects.pop(objects.index(objectt))
            if time >= 1010:
                finishscreen()


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



# --- main ---

pygame.init()

game_display_rect = game_display.get_rect()

game_intro()
