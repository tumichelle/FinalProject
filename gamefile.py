import pygame


pygame.init()
# music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

background_colour = (0,10,0)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Escape from: UNEMPLOYMENT')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
