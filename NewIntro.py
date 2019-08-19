import pygame

pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)

#music


largeText = pygame.font.SysFont("DisposableDroidBB.ttf", 50)
mediumText = pygame.font.SysFont("DisposableDroidBB.ttf", 35)
startText = pygame.font.SysFont("DisposableDroidBB.ttf", 75)
unemployedText = pygame.font.SysFont("DisposableDroidBB.ttf", 70)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)

mouse = pygame.mouse.get_pos()

gameDisplay = pygame.display.set_mode((display_width,display_height))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button_check(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            button['action']()

def button_draw(button):
    font = mediumText
    mouse = pygame.mouse.get_pos()
    if button['rect'].collidepoint(mouse):
        color = button['ac']
    else:
        color = button['ic']

    pygame.draw.rect(game_display, color, button['rect'])

    image, rect = text_objects(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)

def game_intro():

    background_image = pygame.image.load("StartBackground.png")
    gameDisplay.blit(background_image, [0, 0])
    TextSurf, TextRect = text_objects('RAISING THE', largeText)
    TextRect.center = ((350),(35))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    TextSurf, TextRect = text_objects('STEAKS', unemployedText)
    TextRect.center = ((345),(180))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


    buttons = [
        {
            'msg': 'INSTRUCTIONS',
            'rect': pygame.Rect(25, 310, 190, 90),
            'ac': red,
            'ic': white,
            'action': instructions_loop,
        },
        {
            'msg': 'ABOUT',
            'rect': pygame.Rect(530, 320, 90, 90),
            'ac': red,
            'ic': white,
            'action': about_loop,
        }
    ]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])

        button_draw(buttons[0])
        button_draw(buttons[1])

        pygame.display.update()


def instructions_loop():
    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(530, 320, 90, 90),
            'ac': red,
            'ic': white,
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


def about_loop():
    buttons = [
        {
            'msg': 'BACK',
            'rect': pygame.Rect(530, 320, 90, 90),
            'ac': red,
            'ic': white,
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

# --- main ---

pygame.init()

game_display = pygame.display.set_mode((display_width, display_height))
game_display_rect = game_display.get_rect()

game_intro()
