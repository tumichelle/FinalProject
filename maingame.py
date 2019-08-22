import classDefs
from classDefs import *

pygame.init()

black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
blue = (0,0,255)
purple = (153,50,204)
gray = (192,192,192)
darkgray = (33,33,33)
pygame.display.set_caption('Raising the Steaks')

#music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

#sets font size
largeText = pygame.font.SysFont("DisposableDroidBB.ttf", 50)
mediumText = pygame.font.SysFont("DisposableDroidBB.ttf", 35)
startText = pygame.font.SysFont("DisposableDroidBB.ttf", 75)
steakText = pygame.font.SysFont("DisposableDroidBB.ttf", 60)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)
nameText = pygame.font.SysFont("DisposableDroidBB.ttf", 25)
hugeText = pygame.font.SysFont("DisposableDroidBB.ttf", 100)

mouse = pygame.mouse.get_pos()

#sets window
W, H = 700, 391
win = pygame.display.set_mode((W,H))


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

    pygame.draw.rect(win, color, button['rect'])

    image, rect = textWhite(button['msg'], font)
    rect.center = button['rect'].center
    win.blit(image, rect)


def textWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textRed(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()

def textBlack(text, font):
    textStart = font.render(text, True, black)
    return textStart, textStart.get_rect()

def textGray(text, font):
    textStart = font.render(text, True, gray)
    return textStart, textStart.get_rect()

#quit game function
def quit_game():
    pygame.quit()
    quit()

#main intro page (with buttons to about and instructions)
def game_intro():

    background_image = pygame.image.load("SteakStart.png")
    win.blit(background_image, [0, 0])
    TextSurf, TextRect = textWhite('RAISING THE', largeText)
    TextRect.center = ((350),(45))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textWhite('STEAKS', steakText)
    TextRect.center = ((345),(180))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textGray("TOTAL SCORE:", nameText)
    TextRect.center = ((630),(20))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textGray(str(sum(points)) + " pts", mediumText)
    TextRect.center = ((630),(41))
    win.blit(TextSurf, TextRect)
    pygame.display.update()


    buttons = [
        {
            'msg': 'INSTRUCTIONS',
            'rect': pygame.Rect(42, 310, 190, 60),
            'ac': black,
            'ic': red,
            'action': instructions_loop,
        },
        {
            'msg': 'ABOUT',
            'rect': pygame.Rect(515, 310, 90, 60),
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
        },
        {
            'msg': ' ',
            'rect': pygame.Rect(0, 50, 20, 20),
            'ac': darkgray,
            'ic': purple,
            'action': winscreen,
        },
        {
            'msg': ' ',
            'rect': pygame.Rect(0, 100, 20, 20),
            'ac': darkgray,
            'ic': blue,
            'action': zero,
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
                button_check(buttons[4])

        button_draw(buttons[0], mediumText)
        button_draw(buttons[1], mediumText)
        button_draw(buttons[2], largeText)
        button_draw(buttons[3], mediumText)
        button_draw(buttons[4], mediumText)

        pygame.display.update()

#instructions page with back button
def instructions_loop():
    background_image = pygame.image.load("INTROANDABOUT.png")
    win.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('INSTRUCTIONS', largeText)
    TextRect.center = ((355),(73))
    win.blit(TextSurf, TextRect)
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
    TextSurf, TextRect = textWhite("OBJECTIVE: GATHER 400 POINTS TO 'RAISE THE STEAKS'", smallText)
    TextRect.center = ((270),(140))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("AVOID THE OBSTACLES USING THE UP AND DOWN ARROW KEYS", smallText)
    TextRect.center = ((270),(170))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("            WIN        LOSE", smallText)
    TextRect.center = ((270),(205))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("LEVEL 1  +100pts   -50pts", smallText)
    TextRect.center = ((270),(230))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite(" LEVEL 2  +200pts   -100pts", smallText)
    TextRect.center = ((270),(260))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite(" LEVEL 3  +300pts   -150pts", smallText)
    TextRect.center = ((270),(290))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("PLOT TWIST: THE NUMBER OF LIVES YOU GET IS RANDOMIZED ", smallText)
    TextRect.center = ((270),(325))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GOOD LUCK RAISING THE STEAKS! ", mediumText)
    TextRect.center = ((270),(360))
    win.blit(TextSurf, TextRect)
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
    win.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('ABOUT', largeText)
    TextRect.center = ((352),(73))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(580, 318, 80, 40),
            'ac': black,
            'ic': red,
            'action': game_intro,
        }
    ]

#michelle's bio
    michelle = pygame.image.load("michelle.jpeg")
    win.blit(michelle, (20,130))
    TextSurf, TextRect = textWhite("MICHELLE TU", nameText)
    TextRect.center = ((210),(140))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 12", smallText)
    TextRect.center = ((210),(180))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("LEXINGTON", smallText)
    TextRect.center = ((210),(200))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("HIGH SCHOOL", smallText)
    TextRect.center = ((210),(220))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

#leia's bio
    leia = pygame.image.load("aj.jpeg")
    win.blit(leia, (300,130))
    TextSurf, TextRect = textWhite("AJ CHAU", nameText)
    TextRect.center = ((500),(140))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 11", smallText)
    TextRect.center = ((500),(180))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("ALUM OF SOULE", smallText)
    TextRect.center = ((500),(200))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("EARLY CHILDHOOD CENTER", smallText)
    TextRect.center = ((510),(220))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

#ellie's bio
    ellie = pygame.image.load("ellie.jpeg")
    win.blit(ellie, (20,270))
    TextSurf, TextRect = textWhite("ELLIE", nameText)
    TextRect.center = ((210),(290))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("KLIBANER-SCHIFF", nameText)
    TextRect.center = ((210),(310))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 11", smallText)
    TextRect.center = ((210),(340))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("MAIMONIDES", smallText)
    TextRect.center = ((210),(360))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

#aj's bio
    aj = pygame.image.load("leia.jpeg")
    win.blit(aj, (300,270))
    TextSurf, TextRect = textWhite("LEIA PAYANO", nameText)
    TextRect.center = ((480),(290))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("GRADE 12", smallText)
    TextRect.center = ((480),(330))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    TextSurf, TextRect = textWhite("KIPP ACADEMY", smallText)
    TextRect.center = ((480),(350))
    win.blit(TextSurf, TextRect)
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
    win.blit(background_image, [0, 0])

    TextSurf, TextRect = textWhite('CHOOSE A DIFFICULTY', largeText)
    TextRect.center = ((355),(73))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textGray("TOTAL SCORE:", mediumText)
    TextRect.center = ((560),(180))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = textGray(str(sum(points)) + " pts", largeText)
    TextRect.center = ((560),(220))
    win.blit(TextSurf, TextRect)
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

#starts level 1
def level1():
    print(1)
    play(40,50,1)

#starts level 2
def level2():
    print(2)
    play(35,45,2)

#starts level 3
def level3():
    print(3)
    play(30,35,3)

points = []

def zero():
    points.clear()
    game_intro()


#winscreen
def winscreen():
    buttons = [
        {
            'msg': 'MAIN MENU',
            'rect': pygame.Rect(505, 335, 180, 40),
            'ac': black,
            'ic': red,
            'action': game_intro,
        }
    ]
    run = True
    winner = pygame.image.load('WinScreen.png')
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])

        win.blit(winner,[0,0])
        button_draw(buttons[0], mediumText)
        pygame.display.update()

        TextSurf, TextRect = textBlack("YOU", hugeText)
        TextRect.center = ((150),(260))
        win.blit(TextSurf, TextRect)
        pygame.display.update()

        TextSurf, TextRect = textBlack("WIN!", hugeText)
        TextRect.center = ((550),(260))
        win.blit(TextSurf, TextRect)
        pygame.display.update()

lives = pygame.image.load('lives.png')
#contains entire game
def play(leva,levb,hard):

    #some nice random variables to set everything up
    global points
    lev = hard
    time = 0

    #sets up background
    bg = pygame.image.load('GameBackground.png').convert()
    bgX = 0
    bgX2 = bg.get_width()
    clock = pygame.time.Clock()

    #makes background show up/scroll and character and hearts show
    def redrawWindow():
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2,0))
        if lifenum == 1:
            if live1 == True:
                win.blit(pygame.transform.scale(lives, (30,30)), (84,12))
        elif lifenum == 2:
            if live1 == True:
                win.blit(pygame.transform.scale(lives, (30,30)), (124,12))
            if live2 == True:
                win.blit(pygame.transform.scale(lives, (30,30)), (164,12))
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
        TextSurf, TextRect = textBlack("DISTANCE LEFT: " + (str(int((502 - time)/5))) + " M", nameText)
        TextRect.center = ((570,30))
        win.blit(TextSurf, TextRect)

        TextSurf, TextRect = textBlack("LEVEL " + str(lev), mediumText)
        TextRect.center = ((350),(30))
        win.blit(TextSurf, TextRect)

        TextSurf, TextRect = textBlack("LIVES: ", nameText)
        TextRect.center = ((50),(30))
        win.blit(TextSurf, TextRect)
        pygame.display.update()

    #losescreen
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
        if lev == 1:
            minus = (-50)
        elif lev == 2:
            minus = (-100)
        elif lev == 3:
            minus = (-150)

        buttons = [
            {
                'msg': 'REPLAY',
                'rect': pygame.Rect(480, 318, 140, 40),
                'ac': black,
                'ic': red,
                'action': levels_loop,
            },
            {
                'msg': 'MAIN MENU',
                'rect': pygame.Rect(50, 318, 180, 40),
                'ac': black,
                'ic': red,
                'action': game_intro,
            }
            ]


        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            win.blit(lose, [0,0])
            pygame.display.update()
            while True:
                TextSurf, TextRect = textWhite("YOU LOSE", hugeText)
                TextRect.center = ((350),(140))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textGray("TOTAL SCORE:", nameText)
                TextRect.center = ((630),(20))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textGray(str(sum(points)) + " pts", mediumText)
                TextRect.center = ((630),(41))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textWhite((str(minus) + " pts"), steakText)
                TextRect.center = ((350),(240))
                win.blit(TextSurf, TextRect)
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

    #finishscreen
    def finishscreen():
        run = True
        finish = pygame.image.load('completelevel.png')
        win.blit(finish, [0,0])
        pygame.display.update()
        if hard == 1:
            plus = (100)
        elif hard == 2:
            plus = (200)
        elif hard == 3:
            plus = (300)

        buttons = [
            {
                'msg': 'REPLAY',
                'rect': pygame.Rect(534, 306, 130, 50),
                'ac': black,
                'ic': purple,
                'action': levels_loop,
            },
            {
                'msg': 'MAIN MENU',
                'rect': pygame.Rect(22, 305, 158, 50),
                'ac': black,
                'ic': purple,
                'action': game_intro,
            }
            ]

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            while True:
                TextSurf, TextRect = textBlack("GREAT WORK!", startText)
                TextRect.center = ((350),(40))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textBlack("KEEP PLAYING TO RAISE THE STEAKS", mediumText)
                TextRect.center = ((350),(115))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textBlack("BY WINNING 400pts", mediumText)
                TextRect.center = ((350),(170))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textBlack("TOTAL SCORE:", mediumText)
                TextRect.center = ((350),(300))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textBlack(str(sum(points)) + " pts", largeText)
                TextRect.center = ((350),(340))
                win.blit(TextSurf, TextRect)
                pygame.display.update()

                TextSurf, TextRect = textGray(("+" + str(plus) + " pts"), mediumText)
                TextRect.center = ((350),(220))
                win.blit(TextSurf, TextRect)
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

    #some more fun random variables to make the code work
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

    #main loop that fr makes stuff happen
    while run:
        tick += 1
        time += 1
        redrawWindow()

        #checks if objects are colliding or if dude is out of lives, takes away
        #points and calls the losescreen if the guy is dead
        for objectt in objects:
            if objectt.collide(runner.hitbox):
                runner.falling = True
                objects.pop(objects.index(objectt))
                if die == 0:
                    if lifenum == 1:
                        live1 = False
                        time = 0
                        if lev == 1:
                            points.append(-50)
                        elif lev == 2:
                            points.append(-100)
                        elif lev == 3:
                            points.append(-150)
                        losescreen()
                    elif lifenum == 2:
                        live2 = False
                    elif lifenum == 3:
                        live3 = False
                    die += 1
                elif die == 1:
                    if lifenum == 2:
                        live1 = False
                        time = 0
                        if lev == 1:
                            points.append(-50)
                        elif lev == 2:
                            points.append(-100)
                        elif lev == 3:
                            points.append(-150)
                        losescreen()
                    elif lifenum == 3:
                        live2 = False
                    die += 1
                elif die == 2:
                    live1 = False
                    time = 0
                    if lev == 1:
                        points.append(-50)
                    elif lev == 2:
                        points.append(-100)
                    elif lev == 3:
                        points.append(-150)
                    losescreen()
                else:
                    runner.falling = False

            #makes obstacles disappear a hot sec before the game ends so that
            #you can't lose and finish at the exact same time
            elif time >= 500:
                objects.pop(objects.index(objectt))

            objectt.x -= 12
            if objectt.x < objectt.width * -1:
                objects.pop(objects.index(objectt))

        #ends game, gives points, calls finish screen or win screen
        if time >= 502:
            if lev == 1:
                points.append(100)
            elif lev == 2:
                points.append(200)
            elif lev == 3:
                points.append(300)
            if sum(points) < 400:
                finishscreen()
            else:
                winscreen()

        #makes background actually scroll
        bgX -= 13
        bgX2 -= 13
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        #lets you quit the game (x out)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == USEREVENT+1:
                speed += 1

        #generates random obstacles based on level
        if (tick % (random.randint(leva,levb))) == 0:
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

        #checks if keys are pressed to jump/slide
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not (runner.jumping):
                runner.jumping = True

        if keys[pygame.K_DOWN]:
            if not (runner.sliding):
                runner.sliding = True

        #sets speed
        clock.tick(20)




# --- main ---

pygame.init()

win_rect = win.get_rect()

game_intro()
