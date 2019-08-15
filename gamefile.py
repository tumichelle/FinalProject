import pygame


pygame.init()

display_width = 700
display_height = 391
black = (0,0,0)
white = (255, 255, 255)
background_colour = (0,10,0)

# music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Escape from: UNEMPLOYMENT')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#intro screen

def text_objects(text, font):
    textSurface = font.render(text, True,white )
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.SysFont("DisposableDroidBB copy.ttf", 10)

        TextSurf, TextRect = text_objects('Escape from Unemployment', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

game_intro ()
