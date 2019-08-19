import pygame

pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)

#music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

largeText = pygame.font.SysFont("DisposableDroidBB.ttf", 50)
mediumText = pygame.font.SysFont("DisposableDroidBB.ttf", 35)
startText = pygame.font.SysFont("DisposableDroidBB.ttf", 75)
unimployedText = pygame.font.SysFont("DisposableDroidBB.ttf", 70)
smallText = pygame.font.SysFont("DisposableDroidBB.ttf", 20)

mouse = pygame.mouse.get_pos()

gameDisplay = pygame.display.set_mode((display_width,display_height))



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def textStartcolor(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()


'''
def button (msg,x,y,w,h, action = None):
    click = pygame.mouse.get_pressed()
    print (click)
    while action == None:
        if x+w > mouse [0] > x and y+h > mouse [1] > y:
            TextSurf, TextRect = textStartcolor(msg, mediumText)
            TextRect.center = ((x),(y))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

            if click[0] == 1 and action != None:
                action()
        else:
            TextSurf, TextRect = text_objects(msg, mediumText)
            TextRect.center = ((x),(y))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
'''


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()

        background_image = pygame.image.load("StartBackground.png")
        gameDisplay.blit(background_image, [0, 0])
        TextSurf, TextRect = text_objects('RAISING THE', largeText)
        TextRect.center = ((350),(35))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

        TextSurf, TextRect = text_objects('STEAKS', unimployedText)
        TextRect.center = ((345),(180))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
#start button
        if 260+180 > mouse [0] > 260 and 305+60 > mouse [1] > 305:
            pygame.draw.rect(gameDisplay, red, [260, 305, 180, 60], 5)
            TextSurf, TextRect = textStartcolor('START', startText)
            TextRect.center = ((350),(335))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

        else:
            pygame.draw.rect(gameDisplay, white, [260, 305, 180, 60], 5)
            TextSurf, TextRect = text_objects('START', startText)
            TextRect.center = ((350),(335))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

        #about button
        if 530+190 > mouse [0] > 530 and 320+90 > mouse [1] > 320:
            TextSurf, TextRect = textStartcolor('About', mediumText)
            TextRect.center = ((575),(335))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                background_image = pygame.image.load("aboutpage.png")
                gameDisplay.blit(background_image, [0, 0])
                TextSurf, TextRect = text_objects('About', largeText)
                TextRect.center = ((350),(35))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('We aim to show the disparity within racial priviledge', smallText)
                TextRect.center = ((240),(100))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Specifically, through unemployement rates', smallText)
                TextRect.center = ((320),(140))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('The number of obstacles generated correlate with carefully researched data.', smallText)
                TextRect.center = ((350),(200))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Through this game, we hope to raise awareness to this problem', smallText)
                TextRect.center = ((340),(240))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Source.', mediumText)
                TextRect.center = ((380),(280))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Economic Policy Institute, Collegeboard, and Bureau Labor of Stats', smallText)
                TextRect.center = ((320),(320))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Created by GWC Summer Immersion, Boston Akamai 2019', smallText)
                TextRect.center = ((500),(365))
                gameDisplay.blit(TextSurf, TextRect)
                pygame.display.update()
        else:
            TextSurf, TextRect = text_objects('About', mediumText)
            TextRect.center = ((545),(347))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()

#Instructions Button
        if 25+190 > mouse [0] > 25 and 310+90 > mouse [1] > 310:
            TextSurf, TextRect = textStartcolor('Instructions', mediumText)
            TextRect.center = ((125),(335))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                background_image = pygame.image.load("instruction.png")
                gameDisplay.blit(background_image, [0, 0])
                TextSurf, TextRect = text_objects('Instructions', largeText)
                TextRect.center = ((350),(35))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Your objective is to get the job.', smallText)
                TextRect.center = ((220),(80))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Use the arrow keys to jump or slide to avoid obstacles.', smallText)
                TextRect.center = ((320),(140))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects('Good Luck!', mediumText)
                TextRect.center = ((160),(200))
                gameDisplay.blit(TextSurf, TextRect)
                pygame.display.update()
        else:
            TextSurf, TextRect = text_objects('Instructions', mediumText)
            TextRect.center = ((125),(335))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()


game_intro()
