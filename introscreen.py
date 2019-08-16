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

mouse = pygame.mouse.get_pos()

gameDisplay = pygame.display.set_mode((display_width,display_height))



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def textStartcolor(text, font):
    textStart = font.render(text, True, red)
    return textStart, textStart.get_rect()

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
        TextSurf, TextRect = text_objects('ESCAPE FROM', largeText)
        TextRect.center = ((350),(35))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

        TextSurf, TextRect = text_objects('UNEMPLOYMENT', unimployedText)
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


game_intro()
while True:
    button('Instructions',125,330,190,90)
    button('About',550,330,190,90)
