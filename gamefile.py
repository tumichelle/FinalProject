import pygame

pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)

#music
#pygame.mixer.music.load('GameMusic.mp3')
#pygame.mixer.music.play(-1)

gameDisplay = pygame.display.set_mode((display_width,display_height))

def text_objects(text, font):
    textSurface = font.render(text, True,white )
    return textSurface, textSurface.get_rect()
def textStartcolor(text, font):
    textStart = font.render(text, True, red )
    return textStart, textStart.get_rect()

def game_intro():
    intro = True


    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        background_image = pygame.image.load("BackgroundIntro.png")
        gameDisplay.blit(background_image, [0, 0])

        largeText = pygame.font.SysFont("DisposableDroidBB copy.ttf", 50)
        mediumText = pygame.font.SysFont("DisposableDroidBB copy.ttf", 40)
        startText = pygame.font.SysFont("DisposableDroidBB copy.ttf", 75)

        TextSurf, TextRect = text_objects('Escape from Unemployment', largeText)
        TextRect.center = ((350),(120))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

#start button
        if 260+180 > mouse [0] > 260 and 150+90 > mouse [1] > 150:
            pygame.draw.rect(gameDisplay, red, [260, 150, 180,90], 5)
            TextSurf, TextRect = textStartcolor('START', startText)
            TextRect.center = ((350),(200))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

        else:
            pygame.draw.rect(gameDisplay, white, [260, 150, 180,90], 5)
            TextSurf, TextRect = text_objects('START', startText)
            TextRect.center = ((350),(200))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

#about button
        if 550+20 > mouse [0] > 550 and 320+90 > mouse [1] > 320:
            TextSurf, TextRect = text_objects('About', mediumText)
            TextRect.center = ((550),(320))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
        else:
            TextSurf, TextRect = textStartcolor('About', mediumText)
            TextRect.center = ((550),(320))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

#Instructions Button
        if 150+20 > mouse [0] > 150 and 320+90 > mouse [1] > 320:
            TextSurf, TextRect = text_objects('Instructions', mediumText)
            TextRect.center = ((150),(320))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
        else:
            TextSurf, TextRect = textStartcolor('Instructions', mediumText)
            TextRect.center = ((150),(320))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
game_intro ()
