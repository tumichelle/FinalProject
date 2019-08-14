import pygame


pygame.init()
# music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

background_colour = (120,10,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
