import pygame

pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
blue = (0,0,255)

#music

game_display = pygame.display.set_mode((display_width,display_height))

largeText = pygame.font.SysFont("DisposableDroidBB.ttf", 50)
mediumText = pygame.font.SysFont("DisposableDroidBB.ttf", 35)
startText = pygame.font.SysFont("DisposableDroidBB.ttf", 75)
steakText = pygame.font.SysFont("DisposableDroidBB.ttf", 60)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)

mouse = pygame.mouse.get_pos()

def textWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textRed(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()

#checks if button is clicked, does action
def button_check(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            button['action']()

#changes button when moused over
def button_draw(button):
    font = mediumText
    mouse = pygame.mouse.get_pos()
    if button['rect'].collidepoint(mouse):
        color = button['ic']
    else:
        color = button['ac']

    pygame.draw.rect(game_display, color, button['rect'])

    image, rect = textWhite(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)

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

        button_draw(buttons[0])
        button_draw(buttons[1])
        button_draw(buttons[2])

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

        button_draw(buttons[0])
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])

        button_draw(buttons[0])
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
            'msg': 'LEVEL 1',
            'rect': pygame.Rect(62, 150, 340, 40),
            'ac': black,
            'ic': (135,206,235),
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 2',
            'rect': pygame.Rect(62, 225, 340, 40),
            'ac': black,
            'ic': (30,144,255),
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 3',
            'rect': pygame.Rect(62, 300, 340, 40),
            'ac': black,
            'ic': (0,0,139),
            'action': game_intro,
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

        button_draw(buttons[0])
        button_draw(buttons[1])
        button_draw(buttons[2])
        button_draw(buttons[3])
        pygame.display.update()


# --- main ---

pygame.init()

game_display_rect = game_display.get_rect()

game_intro()
