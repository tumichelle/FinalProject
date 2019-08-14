import pygame

pygame.init()
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

#open/close window
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
