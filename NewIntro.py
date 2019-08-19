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
unemployedText = pygame.font.SysFont("DisposableDroidBB.ttf", 70)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)

mouse = pygame.mouse.get_pos()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

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

    image, rect = text_objects(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)

#quit game function
def quit_game():
    pygame.quit()
    quit()

#main intro page (with buttons to about and instructions)
def game_intro():

    background_image = pygame.image.load("StartBackground.png")
    game_display.blit(background_image, [0, 0])
    TextSurf, TextRect = text_objects('RAISING THE', largeText)
    TextRect.center = ((350),(35))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = text_objects('STEAKS', unemployedText)
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
    font = mediumText
    background_image = pygame.image.load("trippyinstructionsandabout.png")
    game_display.blit(background_image, [0, 0])

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(590, 310, 80, 60),
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

#about page with back button
def about_loop():
    font = mediumText
    background_image = pygame.image.load("trippyinstructionsandabout.png")
    game_display.blit(background_image, [0, 0])

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(590, 310, 80, 60),
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
    background_image = pygame.image.load("trippylevelspage.png")
    game_display.blit(background_image, [0, 0])

    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(590, 310, 80, 60),
            'ac': black,
            'ic': red,
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 1',
            'rect': pygame.Rect(590, 310, 80, 60),
            'ac': black,
            'ic': red,
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 2',
            'rect': pygame.Rect(590, 310, 80, 60),
            'ac': black,
            'ic': red,
            'action': game_intro,
        },
        {
            'msg': 'LEVEL 3',
            'rect': pygame.Rect(590, 310, 80, 60),
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
